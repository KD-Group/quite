from .. import *
from . import BaseInterface


class ExcitedSignalInterface(BaseInterface):
    @property
    def excited(self) -> SignalSender:
        if getattr(self, 'excited_', None) is None:
            setattr(self, 'excited_', SignalSender())
            self.set_excited_signal_connection()
        return getattr(self, 'excited_')

    def set_excited_signal_connection(self):
        pass
