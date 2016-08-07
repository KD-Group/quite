import st
from .. import *


@ui_extension
class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text = ListWidgetText(self)
        self.index = ListWidgetIndex(self)
        self.items = ListWidgetItems(self)

        self.closed = SignalSender()

    def closeEvent(self, *_):
        self.closed.emit()


# noinspection PyUnresolvedReferences
class ListWidgetIndex(ValueModel):
    def __init__(self, parent: ListWidget):
        super().__init__(parent)
        self.parent = parent
        self.parent.currentRowChanged.connect(self.changed.emit)

    def get_value(self):
        return self.parent.currentRow()

    def set_value(self, value=None):
        self.parent.setCurrentRow(value)


# noinspection PyUnresolvedReferences
class ListWidgetText(ValueModel):
    def __init__(self, parent: ListWidget):
        super().__init__(parent)
        self.parent.currentTextChanged.connect(self.changed.emit)

    def get_value(self):
        return self.parent.currentItem().value()

    def set_value(self, value=None):
        texts = self.parent.items.value
        assert isinstance(texts, list)
        if value in texts:
            self.parent.setCurrentRow(texts.index(value))
        else:
            self.parent.items.add(value)
            self.parent.setCurrentRow(self.parent.items.count - 1)


class ListWidgetItems(ValueModel):
    def __init__(self, parent: ListWidget):
        super().__init__(parent)

    @property
    def count(self):
        return self.parent.count()

    def add(self, *items):
        self.parent.addItems(items)
        self.changed.emit(self.value)

    def get_value(self):
        return st.foreach(lambda i, s=self: s.parent.item(i).text(), range(self.parent.count()))

    def set_value(self, value=None):
        value = [] if value is None else value

        self.parent.clear()
        self.parent.addItems(value)
        self.changed.emit(value)
