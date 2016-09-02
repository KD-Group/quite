import os
import quite
import unittest


class MyTestCase(unittest.TestCase):
    def test_create_widget_dialog(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '3.widget.controller.ui')

        with quite.EventLoop(timeout=.10):
            c = quite.WidgetUiController(None, ui_file_path)
            c.show()
            self.assertTrue(isinstance(c.w, quite.Widget))

            self.assertTrue(isinstance(c.button('add'), quite.PushButton))
            self.assertTrue(isinstance(c.combo('index'), quite.ComboBox))
            self.assertTrue(isinstance(c.edit('number'), quite.LineEdit))
            self.assertTrue(isinstance(c.list('numbers'), quite.ListWidget))


if __name__ == '__main__':
    unittest.main()
