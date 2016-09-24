from .. import *
from . import BaseInterface


class ClosedSignalInterface(BaseInterface):
    @property
    def closed(self) -> SignalSender:
        return self.create(SignalSender)
