from . import SignalSender


class ValueModel:
    def __constructor__(self):
        pass

    @property
    def value(self):
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)

    @property
    def changed(self):
        obj = getattr(self, 'changed_', None)
        if obj is None:
            obj = SignalSender()
            setattr(self, 'changed_', obj)
            self.set_changed_connection()
        return obj

    def set_changed_connection(self):
        pass

    def get_value(self):
        pass

    def set_value(self, value=None):
        pass

    def clear(self):
        self.set_value()

    def connect(self, b):
        """:type b: ValueModel"""
        self.changed.connect(b.set_value)
        b.changed.connect(self.set_value)
        b.value = self.value
