from .. import BaseInterface
from ... import run_deferred_function


class ContainerAbilityInterface(BaseInterface):
    def set_central_widget(self, w):
        return run_deferred_function('set_central_widget', self, w)

    def set_square_widget(self, w, spacing=0):
        return run_deferred_function('set_square_widget', self, w, spacing)

    def export_to_pdf(self, filename):
        return run_deferred_function('export_to_pdf', self, filename)