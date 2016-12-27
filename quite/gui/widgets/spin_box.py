import prett
from .. import *


@ui_extension
class SpinBox(QSpinBox, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'SpinBox'):
            self.parent = parent

        def get_value(self):
            return str(self.parent.value())

        def set_value(self, value):
            self.parent.setValue(int(value or 0))

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.valueChanged[str].connect(self.check_change)
