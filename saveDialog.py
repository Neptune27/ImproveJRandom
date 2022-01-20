from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import datetime

NOW_DATE = datetime.datetime


class SaveDialog(QFileDialog):
    def __init__(self, texts):
        super().__init__()
        save_location, _ = self.getSaveFileName(self, "Save", "", "Text file (*.txt)", )
        try:
            with open(save_location, "w", encoding='UTF-8') as save:
                # print(save_location)
                save.write(texts)
        except FileNotFoundError:
            print("[WARNING] File not found: " + save_location)


class AutoSave:
    def __init__(self, text, location):
        self.text = text
        self.location = location

    def save(self):
        with open(f"{self.location}{str(NOW_DATE.now())[:-7]}.txt", 'w', encoding='UTF-8') as loc:
            loc.write(self.text)
