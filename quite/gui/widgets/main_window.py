from .. import *


@ui_extension
class MainWindow(QMainWindow, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):
    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)
