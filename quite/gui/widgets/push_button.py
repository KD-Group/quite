from .. import *


@ui_extension
class PushButton(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)

        self.plain_text = self.text
        self.text = PushButtonText(self)

        self.changed = SignalSender()
        # noinspection PyUnresolvedReferences
        self.clicked.connect(self.changed.emit)
        self.triggered = self.changed


class PushButtonText(ValueModel):
    def __init__(self, parent: PushButton):
        super().__init__(parent)

    def get_value(self):
        return self.parent.plain_text()

    def set_value(self, value=None):
        self.parent.setText(value or '')
        self.changed.emit(self.value)
