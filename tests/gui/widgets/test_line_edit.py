import unittest
import quite


class MyTestCase(unittest.TestCase):
    def test_line_edit_text(self):
        with quite.EventLoop(0.1):
            line_edit = quite.LineEdit()
            line_edit.show()
            times = []

            @quite.connect_with(line_edit.text.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                times.append(len(times))

            line_edit.text.value = 'first'
            line_edit.text.value = 'second'
            self.assertEqual(len(times), 2)


if __name__ == '__main__':
    unittest.main()
