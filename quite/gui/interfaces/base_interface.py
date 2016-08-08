class BaseInterface:
    @property
    def name(self) -> str:
        # noinspection PyUnresolvedReferences
        return self.objectName()

    def set_focus(self):
        # noinspection PyUnresolvedReferences
        return self.setFocus()
