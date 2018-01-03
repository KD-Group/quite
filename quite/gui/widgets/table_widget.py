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

    def resizeEvent(self, *args, **kwargs):
        col_count = self.columnCount()
        col_width = sum(list([self.columnWidth(i) for i in range(col_count)]))
        total_col_width = self.width() - self.verticalScrollBar().width()
        for i in range(col_count):
            self.setColumnWidth(i, self.columnWidth(i) / col_width * total_col_width)

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
                return list([self.parent.item(current_row, i).text() for i in range(col_count)])
            return None

        def set_value(self, value):
            assert isinstance(value, list)
            if len(value) is not self.col_count:
                raise ValueError('Value length must equal to column count')
            row = self.row_count
            self.parent.setRowCount(row + 1)
            for i in range(self.col_count):
                if isinstance(value[i], int or float):
                    table_item = QTableWidgetItem('{:.2f}'.format(value[i]))
                elif isinstance(value[i], str):
                    table_item = QTableWidgetItem(value[i])
                else:
                    raise ValueError('Unsupported type')
                table_item.setTextAlignment(Qt.AlignCenter)
                self.parent.setItem(row, i, table_item)
            self.parent.index.value = row

        def set_row_value(self, value, row=None):
            assert isinstance(value, list)
            if len(value) is not self.col_count:
                raise ValueError('Value length must equal to column count')
            if row is None:
                self.set_value(value)
                return
            else:
                if row > self.row_count:
                    raise ValueError('Insert row count larger than total row count')
                if self.row_count == 0:
                    self.parent.setRowCount(1)
            for i in range(self.col_count):
                if isinstance(value[i], int or float):
                    table_item = QTableWidgetItem('{:.2f}'.format(value[i]))
                elif isinstance(value[i], str):
                    table_item = QTableWidgetItem(value[i])
                else:
                    raise ValueError('Unsupported type')
                table_item.setTextAlignment(Qt.AlignCenter)
                self.parent.setItem(row, i, table_item)
            self.parent.index.value = row

    class IndexItem(TableWidgetItem, prett.IndexItem):
        """get/set current select row"""

        def get_value(self):
            return self.parent.currentRow()

        def set_value(self, value):
            value = value or 0
            self.parent.selectRow(value)

        def set_changed_connection(self):
            self.parent.rowCountChanged(self.check_change)

    class StringsItem(TableWidgetItem, prett.StringsItem):
        """ get all tablewidget item text"""

        def get_value(self):
             return list([self.item_text(row, col) for row in range(self.row_count) for col in range(self.col_count)])
