import st
from .. import *


@ui_extension
class ComboBox(QComboBox, StringPropertyInterface, IndexPropertyInterface, ItemsPropertyInterface):
    # string property methods overriding
    def get_string_value(self):
        return self.currentText()

    def set_string_value(self, value=None):
        texts = self.items.value
        assert isinstance(texts, list)
        if value is None:
            self.index.value = 0
        elif value in texts:
            self.setCurrentIndex(texts.index(value))
        else:
            self.items.add(value)
            self.setCurrentIndex(self.items.count - 1)

    def set_string_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.currentIndexChanged[str].connect(self.string.changed.emit)

    # index property methods overriding
    def get_index_value(self):
        return self.currentIndex()

    def set_index_value(self, value=None):
        if value is None or value >= self.items.count:
            value = 0
        self.setCurrentIndex(value)

    def set_index_changed_connection(self):
        self.currentIndexChanged[int].connect(self.index.changed.emit)

    def get_items_value(self):
        return st.foreach(self.itemText, range(self.items.count))

    def set_items_value(self, value=None):
        value = [] if value is None else value

        self.clear()
        self.addItems(value)
        self.items.changed.emit(value)

    def get_items_count(self):
        return self.count()

    def set_items_add(self, *items):
        self.addItems(items)
        self.items.changed.emit(self.items.value)

    def set_items_changed_connection(self):
        pass
