from .. import EventLoop
from .. import QMainWindow
from .. import QCloseEvent
from .. import ui_extension
from .. import ClassExecInterface
from .. import ClosedSignalInterface
from .. import ContainerAbilityInterface


@ui_extension
class MainWindow(QMainWindow, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):
    def closeEvent(self, event: QCloseEvent):
        if self.can_close:
            self.closed.emit()
            event.accept()
        else:
            self.cannot_closed.emit()
            event.ignore()

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)
