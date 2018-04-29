from .. import QDockWidget
from .. import ui_extension
from .. import ContainerAbilityInterface


@ui_extension
class DockWidget(QDockWidget, ContainerAbilityInterface):
    pass
