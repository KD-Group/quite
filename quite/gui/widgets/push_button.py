from .. import *


@ui_extension
class PushButton(QPushButton, ExcitedSignalInterface, StringPropertyInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.clicked.connect(self.excited.emit)

    def get_string_value(self):
        return self.text()

    def set_string_value(self, value=None):
        self.setText(value or '')
        self.string.changed.emit(self.string.value)

    def set_string_changed_connection(self):
        pass
