import st
import os
import codecs
from . import load_qrc
from .. import ext_classes
from .. import Widget, scaling
from .. import QByteArray, QBuffer, QIODevice
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
        if child.text != '16777215':
            child.text = str(int(int(child.text) * ratio))
    for child in tree.iter('height'):
        if child.text != '16777215':
            child.text = str(int(int(child.text) * ratio))
    for child in tree.iter('property'):
        name = child.attrib.get('name', None)
        if name == 'spacing' or name[-6:] == 'Margin' and len(child):
            number = child[0]
            number.text = str(int(int(number.text) * ratio))
    ui_content = ElementTree.tostring(tree, encoding='unicode')
    ui_content = ui_content.replace(' />\n', '/>\n')
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ui_content + '\n'


def load_ui(parent=None, filename=None) -> Widget:
    assert isinstance(filename, str)

    ui_content = get_ui_content(filename)
    if scaling.ratio != 1.0:
        ui_content = process_scaling(ui_content, scaling.ratio)
    return UiLoader().load(ui_content, parent)


def auto_generate_cache(dir_path: str):
    assert isinstance(dir_path, str)
    if not os.path.isdir(dir_path):
        raise ValueError('Paramter Must be Dir Path')
    for root_dir, _, files in os.walk(os.path.abspath(dir_path)):
        for file in files:
            if os.path.splitext(file)[1] == '.ui':
                load_ui(None, os.path.join(root_dir, file))
            if os.path.splitext(file)[1] == '.qrc':
                load_qrc(os.path.join(root_dir, file))


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
