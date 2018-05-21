from . import BaseInterface
from .. import SignalSender


class RowChangedSignalInterface(BaseInterface):
    @property
    def row_changed(self) -> SignalSender:
        return self.create(SignalSender, finished_with=self.set_row_changed_signal_connection)

    def set_row_changed_signal_connection(self):
        pass
