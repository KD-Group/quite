from . import QObject, Signal


class SignalWrapper(QObject):
    signal = Signal(object)


class SignalSender:
    def __init__(self):
        self.signal = SignalWrapper()
        self.last_emit = None

    def emit(self, *args):
        self.last_emit = args
        return self.signal.signal.emit(args)

    def connect(self, func, *args):
        def slot_func(data, *_):
            return func(*(args + data))
        slot_func.__name__ = func.__name__

        self.signal.signal.connect(slot_func)
        if self.last_emit is not None:
            slot_func(self.last_emit)

    @property
    def has_emitted(self):
        return self.last_emit is not None
