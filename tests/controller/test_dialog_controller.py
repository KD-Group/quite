import os
import quite
import unittest


class MyTestCase(unittest.TestCase):
    def test_create_dialog_dialog(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '4.dialog.controller.ui')

        c = quite.DialogController(None, ui_file_path)
        self.assertTrue(isinstance(c.w, quite.Dialog))
        self.assertTrue(isinstance(c.button('quit'), quite.PushButton))
        quite.later(0.1, c.w.close)
        c.exec()


if __name__ == '__main__':
    unittest.main()
