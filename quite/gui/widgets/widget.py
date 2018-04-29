from .. import QWidget
from .. import Painter
from .. import ui_extension
from .. import QCloseEvent, EventLoop
from .. import ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface


@ui_extension
class Widget(QWidget, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):
    def __init__(self, parent=None, *args):
        if getattr(parent, 'w', None) is not None:
            parent = parent.w
        super().__init__(parent, *args)

    def closeEvent(self, event: QCloseEvent):
        self.closed.emit()
        event.accept()

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)

    @property
    def background_color(self):
        return self.create(lambda: None)

    @background_color.setter
    def background_color(self, value):
        self.assign(value)
        self.update()

    @property
    def size(self) -> (int, int):
        return self.width(), self.height()

    def paintEvent(self, *args, **kwargs):
        painter = Painter(self)

        if self.background_color is not None:
            painter.fillRect(self.rect(), self.background_color)
        self.paint(painter)

    def paint(self, painter: Painter):
        pass
