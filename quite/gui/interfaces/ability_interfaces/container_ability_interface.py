from .. import BaseInterface
from ... import run_deferred_function
from PySide.QtCore import QSize


class ContainerAbilityInterface(BaseInterface):
    def set_central_widget(self, w):
        return run_deferred_function('set_central_widget', self, w)

    def set_square_widget(self, w, spacing=0):
        return run_deferred_function('set_square_widget', self, w, spacing)

    def set_layout_spacing(self, spacing):
        return run_deferred_function('set_layout_spacing', self, spacing)

    def export_to_image(self, filename: str, export_size=QSize(1060, 730)):
        if filename.lower().endswith('.pdf'):
            return self.export_to_pdf(filename, export_size)
        else:
            return self.export_to_bitmap(filename, export_size)

    def export_to_pdf(self, filename, export_size=QSize(1060, 730)):
        return run_deferred_function('export_to_pdf', self, filename, export_size)

    def export_to_bitmap(self, filename, export_size=QSize(1060, 730)):
        return run_deferred_function('export_to_bitmap', self, filename, export_size)
