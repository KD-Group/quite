import st
import os
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
        if child.text != '16777215':
            child.text = str(int(int(child.text) * ratio))
    for child in tree.iter('height'):
        if child.text != '16777215':
            child.text = str(int(int(child.text) * ratio))
    for child in tree.iter("property"):
        name = child.attrib.get('name', None)
        if name == 'spacing' or name[-6:] == 'Margin' and len(child):
            number = child[0]
            number.text = str(int(int(number.text) * ratio))
    ui_content = ElementTree.tostring(tree, encoding='unicode')
    ui_content = ui_content.replace(' />\n', '/>\n')
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ui_content + '\n'


def load_ui(parent=None, filename=None, widget_to_dialog=False) -> Widget:
    assert isinstance(filename, str)
    if scaling.ratio != 1.0:
        scaling_filename = '{}@{:.1f}.ui'.format(filename[:-3], scaling.ratio)
        file_exists = os.path.exists(filename)
        scaling_file_exists = os.path.exists(scaling_filename)
        if file_exists and scaling_file_exists:
            file_time = os.stat(filename).st_mtime
            scaling_file_time = os.stat(scaling_filename).st_mtime

            with codecs.open(filename, 'r', 'utf-8') as file:
                file_content = file.read()
            with codecs.open(scaling_filename, 'r', 'utf-8') as scaling_file:
                scaling_file_content = scaling_file.read()

            if file_time > scaling_file_time:
                processed_content = process_scaling(file_content, scaling.ratio)
                if processed_content != scaling_file_content:
                    with codecs.open(scaling_filename, 'w', 'utf-8') as scaling_file:
                        scaling_file.write(processed_content)
            else:
                processed_scaling_content = process_scaling(scaling_file_content, 1.0 / scaling.ratio)
                if processed_scaling_content != file_content:
                    with codecs.open(filename, 'w', 'utf-8') as file:
                        file.write(processed_scaling_content)
        elif file_exists:
            with codecs.open(filename, 'r', 'utf-8') as file:
                with codecs.open(scaling_filename, 'w', 'utf-8') as scaling_file:
                    scaling_file.write(process_scaling(file.read(), scaling.ratio))
        elif scaling_file_exists:
            with codecs.open(scaling_filename, 'r', 'utf-8') as scaling_file:
                with codecs.open(filename, 'w', 'utf-8') as file:
                    file.write(process_scaling(scaling_file.read(), 1.0 / scaling.ratio))

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
