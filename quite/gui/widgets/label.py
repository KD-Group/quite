import prett
from .. import QLabel, Qt
from .. import ui_extension
from .. import BaseInterface


@ui_extension
class Label(QLabel, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'Label'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            self.parent.setText(value or '')

    def set_clickable_text(self, show_text, call_data, call_func):
        self.setText("<a href=\"{}\">{}</a>".format(call_data, show_text))
        self.setTextFormat(Qt.RichText)
        self.linkActivated.connect(call_func)
