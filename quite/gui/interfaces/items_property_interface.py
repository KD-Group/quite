from .. import *
from . import BaseInterface


class ItemsValueModel(ValueModel):
    def add(self, *items):
        pass

    @property
    def count(self):
        return None


class ItemsPropertyInterface(BaseInterface):
    @property
    def items(self) -> ItemsValueModel:
        return self.get_items_object()

    def get_items_object(self) -> ItemsValueModel:
        if getattr(self, 'items_', None) is None:
            setattr(self, 'items_', ItemsProperty(self))
            self.set_items_changed_connection()
        return getattr(self, 'items_')

    def get_items_value(self):
        assert self != self

    def set_items_value(self, value=None):
        assert self != self
        assert value != value

    def set_items_add(self, *items):
        assert self != self

    def set_items_changed_connection(self):
        assert self != self

    def get_items_count(self):
        assert self != self


class ItemsProperty(ValueModel):
    def __init__(self, parent: ItemsPropertyInterface):
        super().__init__()
        self.parent = parent

    def get_value(self):
        return self.parent.get_items_value()

    def set_value(self, value=None):
        self.parent.set_items_value(value)

    def clear(self):
        self.set_value()

    def add(self, *items):
        self.parent.set_items_add(*items)

    @property
    def count(self):
        return self.parent.get_items_count()
