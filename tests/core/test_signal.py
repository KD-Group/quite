import unittest
import quite


class MyTestCase(unittest.TestCase):
    def test_signal(self):
        signal = quite.SignalSender()
        executed = [False]

        def slot():
            self.assertEqual(True, True)
            executed[0] = True
        signal.connect(slot)

        signal.emit()
        self.assertTrue(executed[0])

    def test_signal_with_parameters(self):
        signal = quite.SignalSender()
        executed = [False]

        def slot(a: int, b: int, c: int):
            self.assertEqual(a, 1)
            self.assertEqual(b, 2)
            self.assertEqual(c, 3)
            executed[0] = True
        signal.connect(slot)

        signal.emit(1, 2, 3)
        self.assertTrue(executed[0])


if __name__ == '__main__':
    unittest.main()
