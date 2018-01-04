import prett
from .. import *


@ui_extension
class TableWidget(QTableWidget, ExcitedSignalInterface,
                  prett.WidgetStringInterface, prett.WidgetIndexInterface, prett.WidgetStringListInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.doubleClicked.connect(st.zero_para(self.excited.emit))

    def set_just_show_mode(self):
        self.verticalHeader().hide()
        self.resizeColumnsToContents()
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def set_headers(self, headers: list):
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

    def auto_scaling_column(self):
        self.resizeColumnsToContents()
        col_count = self.columnCount()
        col_width = sum(list([self.columnWidth(i) for i in range(col_count)]))
        total_col_width = self.width() - self.verticalScrollBar().width()
        for i in range(col_count):
            self.setColumnWidth(i, self.columnWidth(i) / col_width * total_col_width)

    def resizeEvent(self, *args, **kwargs):
        self.auto_scaling_column()

    class TableWidgetItem:
        def __init__(self, parent: 'TableWidget'):
            self.parent = parent

        @property
        def row_count(self):
            return self.parent.rowCount()

        @property
        def col_count(self):
            return self.parent.columnCount()

        def item_text(self, row, col):
            return self.parent.item(row, col).text()

    class StringItem(TableWidgetItem, prett.WidgetStringItem):
        """get/set current table row text"""

        def get_value(self):
            if self.parent.index.value >=0 :
                current_row = self.parent.currentRow()
                col_count = self.parent.columnCount()
                return ' '.join(list(self.item_text(current_row, i) for i in range(col_count)))
            return None

        def set_value(self, value):
            assert isinstance(value, str)
            value_list = value.split(' ')
            if len(value_list) is not self.col_count:
                raise ValueError('Value length must equal to column count')

            texts = self.parent.string_list.value
            assert isinstance(texts, list)
            if value is None:
                self.parent.index.value = 0
            elif value in texts:
                self.parent.index.value = texts.index(value)
            else:
                self.parent.setRowCount(self.row_count + 1)
                for i in range(self.col_count):
                    table_item = QTableWidgetItem(value_list[i])
                    table_item.setTextAlignment(Qt.AlignCenter)
                    self.parent.setItem(self.row_count - 1, i, table_item)
                self.parent.index.value = self.row_count - 1

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.currentCellChanged.connect(self.check_change)

    class IndexItem(TableWidgetItem, prett.IndexItem):
        """get/set current select row"""

        def get_value(self):
            return self.parent.currentRow()

        def set_value(self, value):
            value = value or 0
            self.parent.selectRow(value)

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.currentCellChanged(self.check_change)

    class StringsItem(TableWidgetItem, prett.StringsItem):
        """ get all tablewidget item text"""

        def get_value(self):
            table_texts = []
            for row in range(self.row_count):
                row_texts = ''
                for col in range(self.col_count):
                    row_texts += self.item_text(row, col) + ' '
                table_texts.append(row_texts.strip())
            return table_texts

        def set_value(self, value):
            value = value or []
            assert isinstance(value, list)

            self.parent.clearContents()
            self.parent.setRowCount(len(value))
            for row_string, i in zip(value, range(len(value))):
                self.parent.setRowCount(i)
                self.parent.string.value = row_string
            self.check_change()
