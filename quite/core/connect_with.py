from . import *


def connect_with(signal: SignalSender, *args):
    def pack_func(func):
        signal.connect(func, *args)
        return func
    return pack_func
