from . import SignalSender


class ValueModel:
    def __init__(self):
        self.changed = SignalSender()

    @property
    def value(self):
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)

    def get_value(self):
        pass

    def set_value(self, value=None):
        pass

    def clear(self):
        self.set_value()