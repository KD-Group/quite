from .. import *


class DoubleSpinBox(QDoubleSpinBox, DoublePropertyInterface, StringPropertyInterface):
    # double property methods overriding
    def get_double_value(self):
        return self.value()

    def set_double_value(self, value=None):
        self.setValue(value)

    def set_double_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.valueChanged[float].connect(self.double.changed.emit)

    # string property methods overriding
    def get_string_value(self):
        return str(self.double.value)

    def set_string_value(self, value=None):
        self.double.value = float(value)

    def set_string_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.valueChanged[str].connect(self.string.changed.emit)
