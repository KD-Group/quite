from . import WidgetController
from ..gui import *


class DialogController(WidgetController):
    def __init__(self, parent=None, ui_file=None):
        super().__init__(parent, ui_file)

        Shortcut('ctrl+w', self.w).excited.connect(self.w.close)

    def exec(self):
        return self.w.exec()

    @classmethod
    def class_exec(cls, *args):
        return cls(*args).exec()
