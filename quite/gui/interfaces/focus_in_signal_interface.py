from . import BaseInterface
from .. import SignalSender


class FocusInSignalInterface(BaseInterface):
    @property
    def focus_in(self) -> SignalSender:
        return self.create(SignalSender)
