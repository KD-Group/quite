import unittest
import quite


class MyTestCase(unittest.TestCase):
    def test_push_button_text(self):
        with quite.EventLoop(0.1):
            push_button = quite.PushButton()
            push_button.show()
            times = []

            @quite.connect_with(push_button.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                times.append(len(times))

            push_button.string.value = 'first'
            push_button.string.value = 'second'
            self.assertEqual(len(times), 2)

    def test_push_button_triggered(self):
        with quite.EventLoop(0.10):
            push_button = quite.PushButton()
            push_button.show()
            times = []

            @quite.connect_with(push_button.excited)
            def button_clicked():
                if len(times) == 0:
                    self.assertEqual(push_button.string.value, 'first')
                elif len(times) == 1:
                    self.assertEqual(push_button.string.value, 'second')
                times.append(len(times))

            push_button.string.value = 'first'
            push_button.click()
            push_button.string.value = 'second'
            push_button.click()
            self.assertEqual(len(times), 2)


if __name__ == '__main__':
    unittest.main()
