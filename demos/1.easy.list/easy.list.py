import os
import quite


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    ui_file_path = os.path.join(current_path, 'res', 'easy.list.ui')

    w = quite.load_ui(ui_file_path)
    assert isinstance(w.string_edit, quite.LineEdit)
    assert isinstance(w.string_list, quite.ListWidget)
    assert isinstance(w.add_button, quite.PushButton)
    assert isinstance(w.clear_button, quite.PushButton)

    quite.Shortcut('ctrl+w', w).excited.connect(w.close)

    @quite.connect_with(w.add_button.excited, w.string_edit, w.string_list)
    def add_string_to_list(string_edit: quite.LineEdit, string_list: quite.ListWidget):
        string_list.items.add(string_edit.string.value)
        string_list.index.value = string_list.items.count - 1
        string_edit.string.value = ''
        string_edit.set_focus()

    @quite.connect_with(w.clear_button.excited, w.string_edit, w.string_list)
    def clear_string_list(string_edit: quite.LineEdit, string_list: quite.ListWidget):
        string_list.items.clear()
        string_edit.string.value = ''
        string_edit.set_focus()

    @quite.connect_with(w.string_list.index.changed)
    def print_current_index_of_list(index):
        print('current index is', index)

    w.string_edit.set_focus()
    w.exec()
