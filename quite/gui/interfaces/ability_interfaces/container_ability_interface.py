from .. import BaseInterface
from ... import run_deferred_function


class ContainerAbilityInterface(BaseInterface):
    def set_central_widget(self, w):
        return run_deferred_function('set_central_widget', self, w)
