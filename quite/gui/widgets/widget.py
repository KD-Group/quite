from .. import *


@ui_extension
class Widget(QWidget):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

        self.closed = SignalSender()

    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)

    @classmethod
    def class_exec(cls, *args):
        return cls(*args).exec()
