class BaseInterface:
    @property
    def name(self) -> str:
        # noinspection PyUnresolvedReferences
        return self.objectName()

    def set_focus(self):
        # noinspection PyUnresolvedReferences
        return self.setFocus()

    def set_enabled(self):
        # noinspection PyUnresolvedReferences
        return self.setEnable(True)

    def set_disabled(self):
        # noinspection PyUnresolvedReferences
        return self.setEnable(False)
