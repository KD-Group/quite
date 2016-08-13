from .. import *
from . import BaseInterface


class DoublePropertyInterface(BaseInterface):
    @property
    def double(self) -> ValueModel:
        if getattr(self, 'double_', None) is None:
            setattr(self, 'double_', DoubleProperty(self))
            self.set_double_changed_connection()
        return getattr(self, 'double_')

    def get_double_value(self):
        assert self != self

    def set_double_value(self, value=None):
        assert self != self
        assert value != value

    def set_double_changed_connection(self):
        assert self != self


class DoubleProperty(ValueModel):
    def __init__(self, parent: DoublePropertyInterface):
        super().__init__()
        self.parent = parent

    def get_value(self):
        return self.parent.get_double_value()

    def set_value(self, value=None):
        self.parent.set_double_value(value)
