ext_classes = set()


def ui_extension(cls):
    if getattr(cls, 'parent_class', None) is None:
        cls.parent_class = cls.__bases__[0]
    ext_classes.add(cls)
    return cls
