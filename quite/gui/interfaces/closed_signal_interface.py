from .. import *
from . import BaseInterface


class ClosedSignalInterface(BaseInterface):
    @property
    def closed(self) -> SignalSender:
        return self.create(SignalSender)

    @property
    def cannot_closed(self) -> SignalSender:
        return self.create(SignalSender)

    @property
    def can_close(self) -> bool:
        return self.create(lambda: True)

    @can_close.setter
    def can_close(self, value):
        self.assign(value)
