from . import WidgetUiController
from ..gui import Shortcut
from PySide.QtCore import Qt


class DialogUiController(WidgetUiController):
    def __init__(self, parent=None, ui_file=None):
        super().__init__(parent, ui_file)

        Shortcut('ctrl+w', self.w).excited.connect(self.w.close)

    def exec(self):
        return self.w.exec()

    def setWindowMinimizeButtonHint(self):
        self.w.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

    @classmethod
    def class_exec(cls, *args, **kwargs):
        return cls(*args, **kwargs).exec()
