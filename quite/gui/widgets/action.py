from .. import *


@ui_extension
class Action(QAction):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

        self.changed = SignalSender()
        self.triggered.connect(self.changed.emit)
        self.triggered = self.changed
