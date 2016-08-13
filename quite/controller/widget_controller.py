from .. import *


class WidgetController:
    def __init__(self, parent=None, ui_file: str=None):
        assert ui_file is not None

        self.w = load_ui(ui_file, parent)

    def label(self, name=None) -> Label:
        return getattr(self.w, 'label_' + name)

    def button(self, name=None) -> PushButton:
        return getattr(self.w, 'button_' + name)

    def edit(self, name=None) -> LineEdit:
        return getattr(self.w, 'edit_' + name)

    def list(self, name=None) -> ListWidget:
        return getattr(self.w, 'list_' + name)

    def combo(self, name=None) -> ComboBox:
        return getattr(self.w, 'combo_' + name)
