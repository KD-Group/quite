import unittest
import quite


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.table_widget = quite.TableWidget()
        self.table_widget.set_just_show_mode()
        self.table_widget.set_headers(['字符串', '整形', '浮点型'])

    def test_table_widget_string_list(self):
        with quite.EventLoop(0.1) as event:
            self.table_widget.show()
            executed = [False]
            string_list = ["first 1 1.1", "second 2 2.2", "third 3 3.3"]

            @quite.connect_with(self.table_widget.string_list.changed)
            def string_list_changed(string_list_now):
                self.assertEqual(string_list, string_list_now)
                executed[0] = True

            self.table_widget.string_list.value = string_list
            self.assertTrue(executed[0])

if __name__ == '__main__':
    unittest.main()
