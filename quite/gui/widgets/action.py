from .. import QAction
from .. import ui_extension
from .. import ExcitedSignalInterface


@ui_extension
class Action(QAction, ExcitedSignalInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.triggered.connect(self.excited.emit)

    def click(self):
        if self.isEnabled():
            self.trigger()
