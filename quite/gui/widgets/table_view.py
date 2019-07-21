import prett
import typing

from .. import ExcitedSignalInterface, RowChangedSignalInterface
from .. import QTableView, QAbstractTableModel
from .. import Qt, QAbstractItemView, QTableWidgetItem
from .. import ui_extension


@ui_extension
class TableView(QTableView, ExcitedSignalInterface,
                prett.WidgetDictInterface, prett.WidgetIndexInterface, prett.WidgetDictListInterface,
                RowChangedSignalInterface):

    def set_row_changed_signal_connection(self):
        self.clicked.connect(self.row_changed_signal)

    def row_changed_signal(self):
        self.row_changed.emit_if_changed(self.selectedIndexes()[0].row())

    @property
    def model(self):
        if getattr(self, "_model", None) is None:
            self._model = self.Model(self)
            self.setModel(self._model)
        return self._model

    class Model(QAbstractTableModel):
        def __init__(self, parent, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = []
            self.headers = []

        def rowCount(self, parent):
            return len(self.mylist)

        def columnCount(self, parent=None):
            return len(self.headers)

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != Qt.DisplayRole:
                return None
            return self.mylist[index.row()][self.headers[index.column()]]

        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.headers[col]
            return None

        def set_data(self, data):
            self.mylist = data
            # sel.setData(data)

        def set_headers(self, headers):
            self.headers = headers

        def get_by_indexes(self, indexes):
            res = []
            for index in indexes:
                res.append(self.mylist[index])
            return res

    def set_headers(self, headers):
        self.model.set_headers(headers)

    def set_data(self, data):
        self.model.set_data(data)
        self.model.reset()

    def set_column_hidden(self, header):
        self.set_column_visible(header, False)

    def set_column_show(self, header):
        self.set_column_visible(header, True)

    def set_column_visible(self, header, is_visible: True):
        if header not in self.model.headers:
            raise ValueError("header_name doesn't match headers label")
        if is_visible:
            self.showColumn(self.model.headers.index(header))
        else:
            self.hideColumn(self.model.headers.index(header))

    def set_just_show_mode(self):
        self.verticalHeader().hide()
        self.resizeColumnsToContents()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def set_select_rows_mode(self):
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setStyleSheet("selection-background-color: lightBlue;selection-color: black;")
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def get_selected_list(self) -> typing.List[dict]:
        selected_ids = list(map(lambda x: x.row(), self.selectedIndexes()))
        selected_ids = list(set(selected_ids))
        selected_list = self.model.get_by_indexes(selected_ids)
        return selected_list

    def get_selected_list_without_hidden_col(self) -> typing.List[dict]:
        selected_list = self.get_selected_list()
        header_labels = self.model.headers
        hidden_columns = []
        for column_name in header_labels:
            if self.isColumnHidden(header_labels.index(column_name)):
                hidden_columns.append(column_name)
        for row in selected_list:
            for hidden_col in hidden_columns:
                if hidden_col in row.keys():
                    del row[hidden_col]
        return selected_list

    @property
    def col_count(self):
        return self.model.columnCount()
