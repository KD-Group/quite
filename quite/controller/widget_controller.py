from .. import *


class WidgetController:
    def __init__(self, parent=None, constructor=None):
        assert constructor is not None

        if isinstance(parent, WidgetController):
            parent = parent.w

        self.w = constructor(parent)

    # actions
    def close(self):
        self.w.close()

    def show(self):
        self.w.show()

    def hide(self):
        self.w.hide()
