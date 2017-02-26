import st
import codecs
from .. import *
from xml.etree import ElementTree
from PySide.QtUiTools import QUiLoader


@st.make_cache
def get_ui_content(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()
    for cls in ext_classes:
        text = text.replace(cls.__bases__[0].__name__, cls.__name__)
    return text


def process_scaling(ui_content: str, ratio: float) -> str:
    tree = ElementTree.fromstring(ui_content)
    for child in tree.iter('width'):
        child.text = str(min(int(int(child.text) * ratio), 16777215))
    for child in tree.iter('height'):
        child.text = str(min(int(int(child.text) * ratio), 16777215))
    for child in tree.iter("property"):
        name = child.attrib.get('name', None)
        if name == 'spacing' or name[-6:] == 'Margin' and len(child):
            number = child[0]
            number.text = str(int(int(number.text) * ratio))
    return ElementTree.tostring(tree).decode()


def load_ui(parent=None, filename=None, widget_to_dialog=False) -> Widget:
    assert filename is not None

    ui_content = get_ui_content(filename)
    if widget_to_dialog is True:
        tree = ElementTree.fromstring(ui_content)
        first_widget = tree.find('widget')
        if first_widget.attrib.get('class') == 'Widget':
            first_widget.attrib['class'] = 'Dialog'
        ui_content = ElementTree.tostring(tree).decode()
    if scaling.ratio != 1.0:
        ui_content = process_scaling(ui_content, scaling.ratio)
    return UiLoader().load(ui_content, parent)


@st.singleton
class UiLoader:
    def __init__(self):
        self.loader = QUiLoader()
        for cls in ext_classes:
            self.loader.registerCustomWidget(cls)

    def load(self, text, parent=None):
        byte_array = QByteArray(text.encode())
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.ReadWrite)

        ui = self.loader.load(buffer, parent)
        buffer.close()
        return ui
