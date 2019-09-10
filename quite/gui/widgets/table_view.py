import prett
import typing
import functools
from .. import ExcitedSignalInterface, RowChangedSignalInterface
from .. import QTableView, QAbstractTableModel
from .. import Qt, QAbstractItemView, QtGui
from .. import ui_extension


@ui_extension
class TableView(QTableView, ExcitedSignalInterface,
                prett.WidgetDictInterface, prett.WidgetIndexInterface, prett.WidgetDictListInterface,
                RowChangedSignalInterface):
    menuItems = []

    def addMenuItem(self, name, func):
        self.menuItems.append((name, func))

    def contextMenuEvent(self, event):
        if len(self.menuItems) != 0:
            menu = QtGui.QMenu(self)
            for item in self.menuItems:
                name = item[0]
                func = item[1]
                action = QtGui.QAction(name, self)
                pos = event.pos()
                # use lambda will lead to always exec finally func bug, use is ok
                action.triggered.connect(functools.partial(func, pos))
                menu.addAction(action)
            menu.exec_(QtGui.QCursor.pos())

    def set_row_changed_signal_connection(self):
        self.clicked.connect(self.row_changed_signal)

    def row_changed_signal(self):
        if len(self.selectedIndexes()) != 0:
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

        def rowCount(self, parent=None):
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

        def get_data(self, row, col):
            return self.mylist[row][self.headers[col]]

    def set_headers(self, headers):
        self.model.set_headers(headers)

    def set_data(self, data):
        self.model.set_data(data)
        self.model.reset()
        # fix column from hide to show, but not show in view
        # because origin column size is 0
        self.auto_resize_column_width()

    def get_data(self, row, col):
        data = self.model.get_data(row, col)
        return data

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
        self.auto_resize = True
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
    def auto_resize(self):
        return getattr(self, 'resize', False)

    @auto_resize.setter
    def auto_resize(self, value: bool):
        setattr(self, 'resize', value)

    def auto_resize_column_width(self):
        if self.auto_resize:
            self.resizeColumnsToContents()
            col_count = self.col_count
            col_width = sum(list([self.columnWidth(i) for i in range(col_count)]))
            if col_width < self.width():
                for i in range(col_count):
                    self.setColumnWidth(i, self.columnWidth(i) / col_width * self.width())

    def resizeEvent(self, event):
        super(QTableView, self).resizeEvent(event)
        self.auto_resize_column_width()

    @property
    def col_count(self):
        return self.model.columnCount()

    @property
    def row_count(self):
        return self.model.rowCount()

    def select_rows(self, rows):
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        selected_row = list(map(lambda x: x.row(), self.selectedIndexes()))
        for row in rows:
            if row not in selected_row:
                self.selectRow(row)

    def unselect_rows(self, rows):
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        selected_row = list(map(lambda x: x.row(), self.selectedIndexes()))
        for row in rows:
            if row in selected_row:
                self.selectRow(row)
