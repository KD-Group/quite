import st
import codecs
from .. import *
from PySide.QtUiTools import QUiLoader


@st.make_cache
def get_ui_content(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()
    for cls in ext_classes:
        text = text.replace(cls.__bases__[0].__name__, cls.__name__)
    return text


def load_ui(parent=None, filename=None, widget_to_dialog=False) -> Widget:
    assert filename is not None

    ui_content = get_ui_content(filename)
    if widget_to_dialog is True:
        assert isinstance(ui_content, str)

        first_class_pos = ui_content.index('class="')
        first_class = ui_content[first_class_pos + 7:ui_content.index('"', first_class_pos + 7)]

        if first_class == 'Widget':
            ui_content = ui_content.replace('class="Widget"', 'class="Dialog"', 1)
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
