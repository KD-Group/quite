import unittest
import os
import sys
import quite


class MyTestCase(unittest.TestCase):
    @unittest.skipIf(condition=(sys.platform != "win32"), reason="RCC Just For Windows")
    def test_load_text_file_in_qrc(self):
        file_path = os.path.join(os.path.dirname(__file__), 'res/test.qrc')
        quite.load_qrc(file_path)

        file_1 = quite.QFile(':/text/test.txt')
        self.assertTrue(file_1.open(quite.QIODevice.ReadOnly | quite.QIODevice.Text))
        text_in_rc_file_1 = file_1.readAll()
        file_1.close()

        test_file_path = os.path.join(os.path.dirname(__file__), 'res/test.txt')
        file_2 = quite.QFile(test_file_path)
        self.assertTrue(file_2.open(quite.QIODevice.ReadOnly | quite.QIODevice.Text))
        text_in_rc_file_2 = file_2.readAll()
        file_2.close()

        self.assertEqual(text_in_rc_file_1, text_in_rc_file_2)


if __name__ == '__main__':
    unittest.main()
