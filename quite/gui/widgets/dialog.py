from .. import *


@ui_extension
class Dialog(QDialog, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):
    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self, *args):
        super().exec_(*args)
