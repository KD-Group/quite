import sys
from . import QDir
from PySide import QtGui
from PySide.QtGui import *  # noqa: F403


# noinspection PyArgumentList
if not QtGui.QApplication.instance():
    if getattr(sys, 'frozen', None):
        # noinspection PyArgumentList
        QtGui.QApplication.addLibraryPath(QDir.currentPath())

    # noinspection PyTypeChecker,PyCallByClass
    QtGui.QApplication.setStyle('cleanlooks')
    QtGui.QApplication([])
