from .. import *


@ui_extension
class Shortcut(QShortcut, ExcitedSignalInterface):
    def __init__(self, key, *args):
        if isinstance(key, str):
            key = QKeySequence(key)
        super().__init__(key, *args)

    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.activated.connect(self.excited.emit)
