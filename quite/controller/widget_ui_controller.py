import st
from . import WidgetController
from ..gui import Label, PushButton
from ..gui import LineEdit, DateEdit
from ..gui import ListWidget, ComboBox
from ..gui import Widget, DockWidget
from ..gui import GroupBox, SpinBox
from ..gui import DoubleSpinBox, TableWidget
from ..gui import Action, SignalSender
from .. import load_ui


class WidgetUiController(WidgetController):
    def __init__(self, parent=None, ui_file: str = None):
        assert ui_file is not None

        super().__init__(parent, st.partial_back(load_ui, ui_file))

    def label(self, name=None) -> Label:
        return self.__get_widget__('label', name)

    def button(self, name=None) -> PushButton:
        return self.__get_widget__('button', name)

    def edit(self, name=None) -> LineEdit:
        return self.__get_widget__('edit', name)

    def date_edit(self, name=None) -> DateEdit:
        return self.__get_widget__('date_edit', name)

    def list(self, name=None) -> ListWidget:
        return self.__get_widget__('list', name)

    def combo(self, name=None) -> ComboBox:
        return self.__get_widget__('combo', name)

    def container(self, name=None) -> Widget:
        if name is None:
            return self.w
        return self.__get_widget__('container', name)

    def dock(self, name=None) -> DockWidget:
        return self.__get_widget__('dock', name)

    def group(self, name=None) -> GroupBox:
        return self.__get_widget__('group', name)

    def spin(self, name=None) -> SpinBox:
        return self.__get_widget__('spin', name)

    def table(self, name=None) -> TableWidget:
        return self.__get_widget__('table', name)

    def double(self, name=None) -> DoubleSpinBox:
        return self.__get_widget__('double', name)

    def action(self, name=None) -> Action:
        obj = self.__get_widget__('action', name)
        if getattr(obj, 'excited', None) is None:
            obj.excited = SignalSender()
            obj.triggered.connect(obj.excited.emit)

            def set_enabled(status=True):
                obj.setEnabled(status)

            def set_disabled(status=True):
                obj.setEnabled(not status)

            def click():
                if obj.isEnabled():
                    obj.trigger()

            obj.click = click
            obj.set_enabled = set_enabled
            obj.set_disabled = set_disabled
        return obj

    def widget(self, name=None) -> Widget:
        return self.container(name).center_widget

    def __get_widget__(self, type_name, obj_name):
        return getattr(self.w, type_name + '_' + obj_name, None) or getattr(self.w, obj_name + '_' + type_name)
