import prett
from .. import QSpinBox
from .. import ui_extension
from .. import BaseInterface


@ui_extension
class SpinBox(QSpinBox, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'SpinBox'):
            self.parent = parent

        def get_value(self):
            return str(self.parent.value())

        def set_value(self, value):
            if self.get_value() != value:
                self.parent.setValue(int(value or 0))

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.valueChanged[str].connect(self.check_change)
