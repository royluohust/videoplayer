from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtMultimediaWidgets import *
from PySide2.QtMultimedia import *

class myvideowidget(QVideoWidget):
    doubleclicked = Signal()
    def mouseDoubleClickEvent(self, event):
        self.doubleclicked.emit()