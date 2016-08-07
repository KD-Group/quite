import st
from .. import *


@ui_extension
class ComboBox(QComboBox):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

        self.text = ComboBoxText(self)
        self.index = ComboBoxIndex(self)
        self.items = ComboBoxItems(self)


# noinspection PyUnresolvedReferences
class ComboBoxText(ValueModel):
    def __init__(self, parent: ComboBox):
        super().__init__(parent)
        self.parent = parent
        self.parent.currentIndexChanged[str].connect(self.changed.emit)

    def get_value(self):
        return self.parent.currentText()

    def set_value(self, value=None):
        texts = self.parent.items.value
        assert isinstance(texts, list)
        if value in texts:
            self.parent.setCurrentIndex(texts.index(value))
        else:
            self.parent.items.add(value)
            self.parent.setCurrentIndex(self.parent.items.count - 1)


# noinspection PyUnresolvedReferences
class ComboBoxIndex(ValueModel):
    def __init__(self, parent: ComboBox):
        super().__init__(parent)
        self.parent = parent
        self.parent.currentIndexChanged[int].connect(self.changed.emit)

    def get_value(self):
        return self.parent.currentIndex()

    def set_value(self, value=None):
        self.parent.setCurrentIndex(value)


class ComboBoxItems(ValueModel):
    def __init__(self, parent: ComboBox):
        super().__init__(parent)
        self.parent = parent

    @property
    def count(self):
        return self.parent.count()

    def add(self, *items):
        self.parent.addItems(items)
        self.changed.emit(self.value)

    def get_value(self):
        return st.foreach(self.parent.itemText, range(self.count))

    def set_value(self, value=None):
        value = [] if value is None else value

        self.parent.clear()
        self.parent.addItems(value)
        self.changed.emit(value)
