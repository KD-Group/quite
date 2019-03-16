import os
import re
import subprocess
from . import WidgetController
from PySide.QtGui import QFileDialog, QMessageBox, QPushButton, QIcon


class FileDialogController(WidgetController):
    def set_view_icon(self, path):
        self.view_icon_path = path

    def set_finished_icon(self, path):
        self.finished_icon_path = path

    def export_location_dialog(self, export_dir, default_filename, export_format, filename_suffix=None) -> str:
        # export_path = setting.current.saved_export_path.string.value
        # default_filename = project.current.sample_id.string.value
        # if project.current.operator.string.value:
        #     default_filename += '-' + project.current.operator.string.value
        if filename_suffix:
            default_filename += '-' + filename_suffix
        default_filename = re.sub(r'[/\\:*?"<>|]', '-', default_filename)
        default_filename = os.path.join(export_dir, default_filename)

        export_format_filter = "{0} (*.{1})".format(export_format.upper(), export_format)
        filename = QFileDialog.getSaveFileName(self.w, '请选择导出文件夹', default_filename, export_format_filter)
        if isinstance(filename, tuple):
            filename = filename[0]
        assert isinstance(filename, str)
        filename = filename.replace('/', '\\')
        return filename

    def export_finished_dialog(self, export_ok, filename):
        if export_ok:
            msg_box = QMessageBox(self.w)
            msg_box.setWindowTitle('导出成功')
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText('报告导出成功，路径为：{0}'.format(filename))

            if getattr(self, "view_icon_path", None):
                view_button = QPushButton(QIcon(getattr(self, 'view_icon_path')), '查看', msg_box)
            else:
                view_button = QPushButton('查看', msg_box)
            if getattr(self, "finished_icon_path", None):
                finished_button = QPushButton(QIcon(getattr(self, "finished_icon_path")), '完成', msg_box)
            else:
                finished_button = QPushButton('完成', msg_box)
            msg_box.addButton(view_button, msg_box.NoRole)
            msg_box.addButton(finished_button, msg_box.NoRole)
            msg_box.setDefaultButton(finished_button)
            msg_box.exec_()

            if view_button == msg_box.clickedButton():
                subprocess.Popen('explorer /select,"{0}"'.format(filename))
        else:
            self.warning('导出失败！\n请检查文件权限后重新导出')
