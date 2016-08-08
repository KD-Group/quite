from .. import *


@ui_extension
class LineEdit(QLineEdit, StringPropertyInterface):
    def get_string_value(self):
        return self.text()

    def set_string_value(self, value=None):
        self.setText(value or '')

    def set_string_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.textChanged.connect(self.string.changed.emit)
