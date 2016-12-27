import prett
from .. import *


@ui_extension
class Label(QLabel, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'Label'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            self.parent.setText(value or '')
