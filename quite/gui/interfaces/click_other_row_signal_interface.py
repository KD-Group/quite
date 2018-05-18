from . import BaseInterface
from .. import SignalSender


class ClickOtherRowSignalInterface(BaseInterface):
    @property
    def click_other_row(self) -> SignalSender:
        return self.create(SignalSender, finished_with=self.set_click_other_row_signal_connection)

    def set_click_other_row_signal_connection(self):
        pass
