from .. import *
from . import BaseInterface


class StringPropertyInterface(BaseInterface):
    @property
    def string(self) -> ValueModel:
        if getattr(self, 'string_', None) is None:
            setattr(self, 'string_', StringProperty(self))
            self.set_string_changed_connection()
        return getattr(self, 'string_')

    def get_string_value(self):
        assert self != self

    def set_string_value(self, value=None):
        assert self != self
        assert value != value

    def set_string_changed_connection(self):
        assert self != self


class StringProperty(ValueModel):
    def __init__(self, parent: StringPropertyInterface):
        super().__init__()
        self.parent = parent

    def get_value(self):
        return self.parent.get_string_value()

    def set_value(self, value=None):
        self.parent.set_string_value(value)
