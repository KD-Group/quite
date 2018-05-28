from .. import ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface
from .. import EventLoop
from .. import QCloseEvent
from .. import QDialog
from .. import ui_extension


@ui_extension
class Dialog(QDialog, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):

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

    @property
    def size(self) -> (int, int):
        return self.width(), self.height()
