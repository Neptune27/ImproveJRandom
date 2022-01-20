from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class SaveDialog(QFileDialog):
    def __init__(self):
        super().__init__()
        saveLoc, _ = self.getSaveFileName(self, "Save", "", "Text file (*.txt)", )
        print(saveLoc)
