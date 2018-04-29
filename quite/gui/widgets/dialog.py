from .. import QDialog
from .. import QCloseEvent
from .. import ui_extension
from .. import ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface


@ui_extension
class Dialog(QDialog, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):
    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self, *args):
        super().exec_(*args)

    @property
    def size(self) -> (int, int):
        return self.width(), self.height()
