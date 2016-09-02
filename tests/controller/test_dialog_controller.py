import os
import quite
import unittest


class MyTestCase(unittest.TestCase):
    def test_create_dialog_dialog(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '4.dialog.controller.ui')

        c = quite.DialogUiController(None, ui_file_path)
        self.assertTrue(isinstance(c.w, quite.Dialog))
        self.assertTrue(isinstance(c.button('quit'), quite.PushButton))
        quite.later(0.1, c.close)
        c.exec()

    def test_create_dialog_by_widget_ui(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '3.widget.controller.ui')

        class WidgetDialogController(quite.DialogUiController):
            def __init__(self, parent=None):
                super().__init__(parent, ui_file_path)

                @quite.connect_with(self.button('add').excited)
                def new_dialog():
                    d = WidgetDialogController(self.w)
                    quite.later(.1, d.close)
                    d.exec()

        c = WidgetDialogController()
        self.assertTrue(isinstance(c.button('add'), quite.PushButton))
        self.assertTrue(isinstance(c.combo('index'), quite.ComboBox))
        self.assertTrue(isinstance(c.edit('number'), quite.LineEdit))
        self.assertTrue(isinstance(c.list('numbers'), quite.ListWidget))
        quite.later(.4, c.close)
        quite.later(.1, c.button('add').click)
        c.exec()


if __name__ == '__main__':
    unittest.main()
