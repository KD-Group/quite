from .. import *
import pretty


@ui_extension
class LineEdit(QLineEdit, BaseInterface, pretty.WidgetStringInterface):
    class StringItem(pretty.WidgetStringItem):
        def __init__(self, parent: 'LineEdit'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            self.parent.setText(value or '')

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.textChanged.connect(self.string.check_change)
