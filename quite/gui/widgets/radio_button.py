import prett
from .. import ExcitedSignalInterface
from .. import QRadioButton
from .. import ui_extension


@ui_extension
class RatioButton(QRadioButton, ExcitedSignalInterface, prett.WidgetStringInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.clicked.connect(self.excited.emit)

    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'RatioButton'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            self.parent.setText(value or '')
            self.check_change()
