import st
from .. import *


@ui_extension
class ListWidget(QListWidget, StringPropertyInterface, IndexPropertyInterface, ItemsPropertyInterface):
    # string property methods overriding
    def get_string_value(self):
        return self.currentItem().text()

    def set_string_value(self, value=None):
        texts = self.items.value
        assert isinstance(texts, list)
        if value in texts:
            self.setCurrentRow(texts.index(value))
        else:
            self.items.add(value)
            self.setCurrentRow(self.items.count - 1)

    def set_string_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.currentTextChanged.connect(self.string.changed.emit)

    # index property methods overriding
    def get_index_value(self):
        return self.currentRow()

    def set_index_value(self, value=None):
        self.setCurrentRow(value)

    def set_index_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.currentRowChanged.connect(self.index.changed.emit)

    # items property methods overriding
    def get_items_value(self):
        return st.foreach(lambda i, s=self: s.item(i).text(), range(self.items.count))

    def set_items_value(self, value=None):
        value = value or []

        self.clear()
        self.addItems(value)
        self.items.changed.emit(value)

    def set_items_changed_connection(self):
        pass

    def get_items_count(self):
        return self.count()

    def set_items_add(self, *items):
        self.addItems(items)
        self.items.changed.emit(self.items.value)

    @property
    def items(self):
        return self.get_items_object()
