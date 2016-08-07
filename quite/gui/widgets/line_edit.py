from .. import *


@ui_extension
class LineEdit(QLineEdit):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

        self.plain_text = self.text
        self.text = LineEditText(self)


class LineEditText(ValueModel):
    def __init__(self, parent: LineEdit):
        super().__init__(parent)
        self.parent.textChanged.connect(self.changed.emit)

    def get_value(self):
        return self.parent.plain_text()

    def set_value(self, value=None):
        self.parent.setText(value or '')
