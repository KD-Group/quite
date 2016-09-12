from . import *
from ..gui import *


class DialogUiController(WidgetUiController):
    def __init__(self, parent=None, ui_file=None):
        super().__init__(parent, ui_file, widget_to_dialog=True)

        Shortcut('ctrl+w', self.w).excited.connect(self.w.close)

    def exec(self):
        return self.w.exec()

    @classmethod
    def class_exec(cls, *args, **kwargs):
        return cls(*args, **kwargs).exec()
