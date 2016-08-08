import unittest
import st
import quite


class MyTestCase(unittest.TestCase):
    def test_list_widget_row(self):
        with quite.EventLoop(0.1) as event:
            list_widget = quite.ListWidget()
            list_widget.show()
            executed = [False]

            @quite.connect_with(list_widget.text.changed)
            def text_changed(text):
                self.assertEqual(text, '1')
                executed[0] = True

            list_widget.items.value = st.foreach(str, range(10))
            list_widget.index.value = 1
            self.assertTrue(executed[0])

    def test_list_widget_items(self):
        with quite.EventLoop(0.1) as event:
            list_widget = quite.ListWidget()
            list_widget.show()
            executed = [False]
            items = st.foreach(str, range(10))

            @quite.connect_with(list_widget.items.changed)
            def items_changed(items_now):
                self.assertEqual(items, items_now)
                executed[0] = True

            list_widget.items.value = items
            self.assertTrue(executed[0])

    def test_list_widget_set_text(self):
        with quite.EventLoop(0.1):
            list_widget = quite.ListWidget()
            list_widget.show()
            times = []

            @quite.connect_with(list_widget.text.changed)
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

            list_widget.text.set_value('first')
            list_widget.text.set_value('second')
            list_widget.text.set_value('first')
            self.assertEqual(len(times), 3)
            self.assertEqual(list_widget.items.count, 2)

            list_widget.items.clear()
            self.assertEqual(len(times), 4)
            self.assertEqual(list_widget.items.count, 0)

if __name__ == '__main__':
    unittest.main()
