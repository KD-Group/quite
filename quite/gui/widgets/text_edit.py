import prett
from .. import BaseInterface
from .. import QTextEdit
from .. import ui_extension


@ui_extension
class TextEdit(QTextEdit, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'TextEdit'):
            self.parent = parent

        def get_value(self):
            return self.parent.toPlainText()

        def set_value(self, value):
            value = value or ''
            if value != self.get_value():
                self.parent.setText(value)

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.textChanged.connect(self.string.check_change)
