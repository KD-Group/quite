class BaseInterface:
    @property
    def name(self) -> str:
        # noinspection PyUnresolvedReferences
        return self.objectName()

    def set_focus(self):
        # noinspection PyUnresolvedReferences
        return self.setFocus()

    def set_enabled(self, status=True):
        # noinspection PyUnresolvedReferences
        return self.setEnable(status)

    def set_disabled(self, status=False):
        # noinspection PyUnresolvedReferences
        return self.setEnable(not status)
