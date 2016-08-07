from .. import *


@ui_extension
class Dialog(QDialog):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

        self.closed = SignalSender()

    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self, *args, **kwargs):
        super().exec_(*args, **kwargs)

    @classmethod
    def class_exec(cls, *args):
        return cls(*args).exec()

