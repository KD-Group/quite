import st
import prett
from .. import QTableWidget
from .. import ui_extension
from .. import ExcitedSignalInterface
from .. import Qt, QHeaderView, QAbstractItemView, QTableWidgetItem


@ui_extension
class TableWidget(QTableWidget, ExcitedSignalInterface,
                  prett.WidgetDictInterface, prett.WidgetIndexInterface, prett.WidgetDictListInterface):
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

    class DictItem(TableWidgetItem, prett.WidgetDictItem):
        """get/set current table row text"""

        def get_value(self):
            if self.parent.index.value >= 0:
                current_row = self.parent.currentRow()
                col_count = self.parent.columnCount()
                value = dict()
                for i in range(col_count):
                    value[self.parent.horizontalHeaderItem(i).text()] = self.item_text(current_row, i)
                return value
            return None

        def set_value(self, value):
            assert isinstance(value, dict)
            if len(value) is not self.col_count:
                raise ValueError('Value length must equal to column count')

            texts = self.parent.dict_list.value
            assert isinstance(texts, list)
            if value is None:
                self.parent.index.value = 0
            else:
                for key, v in value.items():
                    value[key] = str(v)
                if value in texts:
                    self.parent.index.value = texts.index(value)
                else:
                    header_labels = list(self.parent.horizontalHeaderItem(i).text() for i in range(self.col_count))
                    self.parent.setRowCount(self.row_count + 1)
                    for i in range(self.col_count):
                        item_text = value[header_labels[i]]
                        if item_text is None:
                            raise ValueError("key value doesn't match header label")
                        table_item = QTableWidgetItem(item_text)
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

    class DictListItem(TableWidgetItem, prett.DictListItem):
        """ get all table_widget item text"""

        def get_value(self):
            table_texts = []
            for row in range(self.row_count):
                row_dict = dict()
                for col in range(self.col_count):
                    row_dict[self.parent.horizontalHeaderItem(col).text()] = self.item_text(row, col)
                table_texts.append(row_dict)
            return table_texts

        def set_value(self, value: list):
            value = value or []
            assert isinstance(value, list)

            for i in range(self.row_count):
                self.parent.removeRow(0)
            for row_dict in value:
                self.parent.dict.value = row_dict
            self.check_change()
