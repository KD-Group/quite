from .. import *


class WidgetController:
    def __init__(self, parent=None, ui_file: str=None, widget_to_dialog=False):
        assert ui_file is not None

        self.w = load_ui(ui_file, parent, widget_to_dialog=widget_to_dialog)

    def label(self, name=None) -> Label:
        return self.__get_widget__('label', name)

    def button(self, name=None) -> PushButton:
        return self.__get_widget__('button', name)

    def edit(self, name=None) -> LineEdit:
        return self.__get_widget__('edit', name)

    def list(self, name=None) -> ListWidget:
        return self.__get_widget__('list', name)

    def combo(self, name=None) -> ComboBox:
        return self.__get_widget__('combo', name)

    def container(self, name=None) -> ContainerAbilityInterface:
        return self.__get_widget__('container', name)

    # actions
    def close(self):
        self.w.close()

    def show(self):
        self.w.show()

    def hide(self):
        self.w.hide()

    def __get_widget__(self, type_name, obj_name):
        return getattr(self.w, type_name + '_' + obj_name, None) or getattr(self.w, obj_name + '_' + type_name)
