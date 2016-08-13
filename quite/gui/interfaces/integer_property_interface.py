from .. import *
from . import BaseInterface


class IntegerPropertyInterface(BaseInterface):
    @property
    def integer(self) -> ValueModel:
        if getattr(self, 'integer_', None) is None:
            setattr(self, 'integer_', IntegerProperty(self))
            self.set_integer_changed_connection()
        return getattr(self, 'integer_')

    def get_integer_value(self):
        assert self != self

    def set_integer_value(self, value=None):
        assert self != self
        assert value != value

    def set_integer_changed_connection(self):
        assert self != self


class IntegerProperty(ValueModel):
    def __init__(self, parent: IntegerPropertyInterface):
        super().__init__()
        self.parent = parent

    def get_value(self):
        return self.parent.get_integer_value()

    def set_value(self, value=None):
        self.parent.set_integer_value(value)
