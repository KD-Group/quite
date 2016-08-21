import unittest
import quite


class MyTestCase(unittest.TestCase):
    def test_widget_closed_signal(self):
        w = quite.Widget()
        executed = [False]

        @quite.connect_with(w.closed)
        def is_closed():
            executed[0] = True

        quite.later(0.01, w.close)
        w.exec()
        self.assertTrue(executed[0])


if __name__ == '__main__':
    unittest.main()
