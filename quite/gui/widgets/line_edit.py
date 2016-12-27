from .. import *
import prett


@ui_extension
class LineEdit(QLineEdit, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'LineEdit'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            self.parent.setText(value or '')

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.textChanged.connect(self.string.check_change)
