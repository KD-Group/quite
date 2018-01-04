import unittest
import json
import quite


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.table_widget = quite.TableWidget()
        self.table_widget.set_just_show_mode()
        self.table_widget.set_headers(['字符串', '整形', '浮点型'])

    def test_table_widget_set_row(self):
        with quite.EventLoop(0.1):
            self.table_widget.string.value = '["first", 0, 0.1]'
            self.table_widget.string.value = '["second", 1, 1.1]'
            self.table_widget.string.value = '["third", 2, 2.1]'
            for i in range(3):
                self.table_widget.index.value = i
                self.assertEqual(self.table_widget.currentRow(), i)
                self.assertEqual(self.table_widget.index.value, self.table_widget.currentRow())

    def test_table_widget_insert_row(self):
        with quite.EventLoop(0.1):
            for i in range(3):
                self.table_widget.string_item.set_row_value('["%s", %s, %s]' % (i, i, i * 0.1))
                self.assertEqual(self.table_widget.string.value, '["%s", "%.2f", "%.2f"]' % (i, i, i * 0.1))

            for i in range(4, 10):
                with self.assertRaises(ValueError):
                    self.table_widget.string_item.set_row_value('["first", 0, 0.1]', i)

            self.table_widget.string_item.set_row_value('["first", 0, 0.1]', 2)
            self.assertEqual(self.table_widget.index.value, 2)
            self.assertEqual(self.table_widget.string.value, '["first", "0.00", "0.10"]')

    def test_table_widget_set_text(self):
        with quite.EventLoop(0.1):
            times = []

            @quite.connect_with(self.table_widget.string.changed)
            def text_changed(string):
                if len(times) == 0:
                    self.assertEqual(string, '["first", "0.00", "0.10"]')
                if len(times) == 1:
                    self.assertEqual(string, '["second", "1.00", "1.10"]')
                if len(times) == 2:
                    self.assertEqual(string, '["third", "2.00", "2.10"]')
                times.append(len(times))

            self.table_widget.string.value = '["first", 0, 0.1]'
            self.table_widget.string.value = '["second", 1, 1.1]'
            self.table_widget.string.value = '["third", 2, 2.1]'

if __name__ == '__main__':
    unittest.main()
