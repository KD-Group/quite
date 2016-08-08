import unittest
import st
import quite


class MyTestCase(unittest.TestCase):
    def test_combo_box_row(self):
        with quite.EventLoop(0.1):
            combo_box = quite.ComboBox()
            combo_box.show()
            times = []

            @quite.connect_with(combo_box.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, '0')
                elif len(times) == 1:
                    self.assertEqual(text, '1')
                times.append(len(times))

            combo_box.items.value = st.foreach(str, range(10))
            combo_box.index.value = 1
            self.assertEqual(len(times), 2)

    def test_combo_box_items(self):
        with quite.EventLoop(0.1):
            combo_box = quite.ComboBox()
            combo_box.show()
            executed = [False]

            items = st.foreach(str, range(10))

            @quite.connect_with(combo_box.items.changed)
            def items_changed(items_now):
                self.assertEqual(items, items_now)
                executed[0] = True

            combo_box.items.value = items
            self.assertTrue(executed[0])

    def test_combo_box_set_text(self):
        with quite.EventLoop(0.1):
            combo_box = quite.ComboBox()
            combo_box.show()
            times = []

            @quite.connect_with(combo_box.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                elif len(times) == 2:
                    self.assertEqual(text, 'first')
                elif len(times) == 3:
                    self.assertEqual(text, '')
                times.append(len(times))

            combo_box.string.set_value('first')
            combo_box.string.set_value('second')
            combo_box.string.set_value('first')
            self.assertEqual(len(times), 3)
            self.assertEqual(combo_box.items.count, 2)

            combo_box.items.clear()
            self.assertEqual(len(times), 4)
            self.assertEqual(combo_box.items.count, 0)


if __name__ == '__main__':
    unittest.main()
