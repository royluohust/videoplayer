from PySide2.QtCore import *
from PySide2.QtWidgets import *
class Slider(QSlider):
    ClickedValue = Signal()
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.x = event.pos().x()
            self.value_=round((self.maximum() - self.minimum()) * self.x / self.width() + self.minimum())
            self.setValue(self.value_)
            self.ClickedValue.emit()
        else:
            return super().mousePressEvent(event)