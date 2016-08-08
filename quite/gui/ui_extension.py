ext_classes = set()


def ui_extension(cls):
    ext_classes.add(cls)
    return cls
