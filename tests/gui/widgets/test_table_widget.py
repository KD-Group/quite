import unittest
import quite


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.table_widget = quite.TableWidget()
        self.table_widget.set_just_show_mode()
        self.table_widget.set_headers(['字符串', '整形', '浮点型'])

    def test_table_widget_row(self):
        with quite.EventLoop(0.1):
            self.table_widget.show()
            excuted = [False]

            times = []

            @quite.connect_with(self.table_widget.dict.changed)
            def test_changed(text):
                excuted[0] = True
                times.append(len(times))
                if len(times) == 0:
                    self.assertEqual(text, {'字符串': 'first', '整形': '1', '浮点型': '1.1'})
                elif len(times) == 1:
                    self.assertEqual(text, {'字符串': 'second', '整形': '2', '浮点型': '2.2'})

            self.table_widget.dict_list.value = [{'字符串': 'first', '整形': 1, '浮点型': 1.1},
                                                   {'字符串': 'second', '整形': 2, '浮点型': 2.2}]
            self.assertTrue(excuted[0])

    def test_table_widget_dict_list(self):
        with quite.EventLoop(0.1):
            self.table_widget.show()
            executed = [False]
            dict_list = [{'字符串': 'first', '整形': 1, '浮点型': 1.1},
                           {'字符串': 'second', '整形': 2, '浮点型': 2.2}]

            @quite.connect_with(self.table_widget.dict_list.changed)
            def string_list_changed(dict_list_now):
                self.assertEqual(dict_list, dict_list_now)
                executed[0] = True

            self.table_widget.dict_list.value = dict_list
            self.assertTrue(executed[0])

    def test_table_widget_set_text(self):
        with quite.EventLoop(0.1):
            self.table_widget.show()
            times = []

            @quite.connect_with(self.table_widget.dict.changed)
            def text_changed(dict):
                if len(times) == 0:
                    self.assertEqual(dict, {'字符串': 'first', '整形': '1', '浮点型': '1.1'})
                elif len(times) == 1:
                    self.assertEqual(dict, {'字符串': 'second', '整形': '2', '浮点型': '2.2'})
                elif len(times) == 2:
                    self.assertEqual(dict, {'字符串': 'first', '整形': '1', '浮点型': '1.1'})
                elif len(times) == 3:
                    self.assertEqual(dict, '')
                times.append(len(times))

            self.table_widget.dict.set_value({'字符串': 'first', '整形': 1, '浮点型': 1.1})
            self.table_widget.dict.set_value({'字符串': 'second', '整形': 2, '浮点型': 2.2})
            self.table_widget.dict.set_value({'字符串': 'first', '整形': 1, '浮点型': 1.1})
            self.assertEqual(len(times), 3)
            self.assertEqual(self.table_widget.dict_list.count, 2)


if __name__ == '__main__':
    unittest.main()
