from .. import ClosedSignalInterface, ContainerAbilityInterface
from .. import QCloseEvent
from .. import QDialog
from .. import ui_extension


@ui_extension
class Dialog(QDialog, ClosedSignalInterface, ContainerAbilityInterface):
    keyPressFunc = None

    def keyPressEvent(self, event):
        if self.keyPressFunc is not None:
            self.keyPressFunc(event)
        event.ignore()

    def closeEvent(self, event: QCloseEvent):
        if self.can_close:
            self.closed.emit()
            event.accept()
        else:
            self.cannot_closed.emit()
            event.ignore()

    def exec(self, *args):
        super().exec_(*args)

    @property
    def size(self) -> (int, int):
        return self.width(), self.height()
