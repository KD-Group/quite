import st
import codecs
from .. import *
from PySide.QtUiTools import QUiLoader


def get_ui_content(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()
    for cls in ext_classes:
        text = text.replace(cls.__bases__[0].__name__, cls.__name__)
    return text


def load_ui(filename, parent=None):
    return UiLoader().load(get_ui_content(filename), parent)


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
