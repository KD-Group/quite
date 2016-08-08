from .. import *
from . import BaseInterface


class ClosedSignalInterface(BaseInterface):
    @property
    def closed(self) -> SignalSender:
        if getattr(self, 'closed_', None) is None:
            setattr(self, 'closed_', SignalSender())
        return getattr(self, 'closed_')
