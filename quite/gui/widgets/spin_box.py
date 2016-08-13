from .. import *


class SpinBox(QSpinBox, IntegerPropertyInterface, StringPropertyInterface):
    # integer property methods overriding
    def get_integer_value(self):
        return self.value()

    def set_integer_value(self, value=None):
        self.setValue(value)

    def set_integer_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.valueChanged[int].connect(self.integer.changed.emit)

    # string property methods overriding
    def get_string_value(self):
        return str(self.integer.value)

    def set_string_value(self, value=None):
        self.integer.value = int(value)

    def set_string_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.valueChanged[str].connect(self.string.changed.emit)
