import prett
from .. import QDate
from .. import QDateEdit
from .. import ui_extension
from .. import BaseInterface


@ui_extension
class DateEdit(QDateEdit, BaseInterface, prett.WidgetStringInterface):
    class StringItem(prett.WidgetStringItem):
        def __init__(self, parent: 'DateEdit'):
            self.parent = parent

        def get_value(self):
            return self.parent.text()

        def set_value(self, value):
            value = value or ''
            if value != self.get_value():
                date = value.split('-')
                if len(date) is not 3:
                    raise ValueError('Date format is invalid')
                self.parent.setDate(QDate(int(date[0]), int(date[1]), int(date[2])))

        def set_changed_connection(self):
            # noinspection PyUnresolvedReferences
            self.parent.dateChanged.connect(self.string.check_change)
