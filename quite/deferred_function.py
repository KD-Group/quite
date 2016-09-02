from . import *


@deferred_define
def set_central_widget(self: Widget, widget):
    if isinstance(widget, WidgetController):
        widget = widget.w
    if not isinstance(widget, QWidget):
        raise TypeError('Only Support Widget or Controller')

    if isinstance(self, QMainWindow):
        self.setCentralWidget(widget)
    elif isinstance(self, QDockWidget):
        self.setWidget(widget)
    else:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widget)
        self.setLayout(layout)
