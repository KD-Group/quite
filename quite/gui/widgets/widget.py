from .. import *


@ui_extension
class Widget(QWidget, ClosedSignalInterface, ClassExecInterface):
    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)
