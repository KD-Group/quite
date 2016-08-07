import sys
from ..core import *
from PySide.QtGui import *

# noinspection PyArgumentList
if not QApplication.instance():
    if getattr(sys, 'frozen', None):
        # noinspection PyArgumentList
        QApplication.addLibraryPath(QDir.currentPath())

    # noinspection PyTypeChecker,PyCallByClass
    QApplication.setStyle("cleanlooks")
    QApplication([])
