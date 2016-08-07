from .. import *


@ui_extension
class Label(QLabel):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

        self.text = LabelText(self)


class LabelText(ValueModel):
    def __init__(self, parent: Label):
        super().__init__(parent)

    def get_value(self):
        return self.parent.text()

    def set_value(self, value=None):
        self.parent.setText(value or '')
        self.changed.emit(self.value)
