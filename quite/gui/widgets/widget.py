from .. import *


@ui_extension
class Widget(QWidget, ClosedSignalInterface, ClassExecInterface, ContainerAbilityInterface):
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

    def paintEvent(self, *args, **kwargs):
        painter = Painter(self)

        if self.background_color is not None:
            painter.fillRect(self.rect(), self.background_color)
        self.paint(painter)

    def paint(self, painter: Painter):
        pass
