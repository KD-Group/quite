from .. import *


@ui_extension
class DoubleSpinBox(QDoubleSpinBox, ShowedSignalInterface, DoublePropertyInterface, StringPropertyInterface):
    const_base = 100000000000

    def __init__(self, *args):
        super().__init__(*args)
        self.setDecimals(233)

    def show(self):
        super().show()
        self.showed.emit()

    def paintEvent(self, *args):
        super().paintEvent(*args)
        self.showed.emit()

    def validate(self, text: str, pos: int):
        if text == '' or text == '-' or text == '.':
            return QValidator.Intermediate

        try:
            float(text)
            return QValidator.Acceptable
        except ValueError as e:
            return QValidator.Invalid

    def textFromValue(self, value):
        value = round(value * self.const_base) / self.const_base
        text = str(value)

        if self.showed.has_emitted:
            self.string.changed.emit(text)
            self.double.changed.emit(value)
        return text

    def valueFromText(self, text):
        value = float(text)

        if self.showed.has_emitted:
            self.string.changed.emit(text)
            self.double.changed.emit(value)
        return value

    # double property methods overriding
    def get_double_value(self):
        return self.value()

    def set_double_value(self, value=None):
        self.setValue(value)

    def set_double_changed_connection(self):
        pass

    # string property methods overriding
    def get_string_value(self):
        return self.lineEdit().text()

    def set_string_value(self, value=None):
        self.double.value = float(value)

    def set_string_changed_connection(self):
        pass
