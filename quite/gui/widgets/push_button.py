import prett
from .. import QPushButton
from .. import ui_extension
from .. import ExcitedSignalInterface


@ui_extension
class PushButton(QPushButton, ExcitedSignalInterface, prett.WidgetStringInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.clicked.connect(self.excited.emit)

    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'PushButton'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            self.parent.setText(value or '')
            self.check_change()
