class BaseInterface:
    @property
    def name(self) -> str:
        # noinspection PyUnresolvedReferences
        return self.objectName()
