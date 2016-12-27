import st
import prett
from .. import *


@ui_extension
class ListWidget(QListWidget, ExcitedSignalInterface,
                 prett.WidgetStringInterface, prett.WidgetIndexInterface, prett.WidgetStringListInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.doubleClicked.connect(st.zero_para(self.excited.emit))

    class ListWidgetItem:
        def __init__(self, parent: 'ListWidget'):
            self.parent = parent

        @property
        def count(self):
            return self.parent.count()

        def item_text(self, idx):
            return self.parent.item(idx).text()

        def add_text(self, *text):
            self.parent.addItems(text)

    class StringItem(ListWidgetItem, prett.WidgetStringItem):
        def get_value(self):
            if self.parent.index.value >= 0:
                return self.parent.currentItem().text()
            return None

        def set_value(self, value):
            texts = self.parent.string_list.value
            assert isinstance(texts, list)
            if value is None:
                self.parent.index.value = 0
            elif value in texts:
                self.parent.index.value = texts.index(value)
            else:
                self.add_text(value)
                self.parent.index.value = self.count - 1

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.currentTextChanged.connect(self.check_change)

    class IndexItem(ListWidgetItem, prett.IndexItem):
        def get_value(self):
            return self.parent.currentRow()

        def set_value(self, value):
            value = value or 0
            self.parent.setCurrentRow(value)

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.currentRowChanged.connect(self.check_change)

    class StringsItem(ListWidgetItem, prett.StringsItem):
        def get_value(self):
            return st.foreach(self.item_text, range(self.count))

        def set_value(self, value):
            value = value or []

            self.parent.clear()
            self.parent.addItems(value)
            self.check_change()
