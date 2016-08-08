from .. import *
from . import BaseInterface


class IndexPropertyInterface(BaseInterface):
    @property
    def index(self) -> ValueModel:
        if getattr(self, 'index_', None) is None:
            setattr(self, 'index_', IndexProperty(self))
            self.set_index_changed_connection()
        return getattr(self, 'index_')

    def get_index_value(self):
        assert self != self

    def set_index_value(self, value=None):
        assert self != self
        assert value != value

    def set_index_changed_connection(self):
        assert self != self


class IndexProperty(ValueModel):
    def __init__(self, parent: IndexPropertyInterface):
        super().__init__()
        self.parent = parent

    def get_value(self):
        return self.parent.get_index_value()

    def set_value(self, value=None):
        self.parent.set_index_value(value)
