from functools import partial
from typing import List

import deep_translator.exceptions
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from deep_translator import GoogleTranslator, DeepL

# from importlib import reload
import APIInput
# import kanjiBrowserGUI
# import SQLController
# import wordController
import SQLController
import kanjiBrowserGUI
from jsonController import Settings

setting = Settings()


class Ui_TranslateWindow(object):
    def setupUi(self, TranslateWindow):
        if not TranslateWindow.objectName():
            TranslateWindow.setObjectName(u"TranslateWindow")
        TranslateWindow.resize(800, 600)
        self.actionSet_DeepL_API_Key = QAction(TranslateWindow)
        self.actionSet_DeepL_API_Key.setObjectName(u"actionSet_DeepL_API_Key")
        self.centralwidget = QWidget(TranslateWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textInputWidget = QWidget(self.centralwidget)
        self.textInputWidget.setObjectName(u"textInputWidget")
        self.verticalLayout = QVBoxLayout(self.textInputWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.translationMode = QComboBox(self.textInputWidget)
        self.translationMode.setObjectName(u"translationMode")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translationMode.sizePolicy().hasHeightForWidth())
        self.translationMode.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.translationMode)

        self.font = QFont()
        self.font.setPointSize(18)

        self.inputTextEdit = QPlainTextEdit(self.textInputWidget)
        self.inputTextEdit.setObjectName(u"inputTextEdit")
        self.inputTextEdit.setFont(self.font)

        self.verticalLayout.addWidget(self.inputTextEdit)

        self.horizontalLayout.addWidget(self.textInputWidget)

        self.textOutputWidget = QWidget(self.centralwidget)
        self.textOutputWidget.setObjectName(u"textOutputWidget")
        self.verticalLayout_2 = QVBoxLayout(self.textOutputWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.languageMode = QComboBox(self.textOutputWidget)
        self.languageMode.setObjectName(u"languageMode")

        self.verticalLayout_2.addWidget(self.languageMode)

        self.outputTextEdit = QPlainTextEdit(self.textOutputWidget)
        self.outputTextEdit.setObjectName(u"outputTexEdit")
        self.outputTextEdit.setFont(self.font)

        self.verticalLayout_2.addWidget(self.outputTextEdit)

        self.horizontalLayout.addWidget(self.textOutputWidget)

        TranslateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TranslateWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        TranslateWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TranslateWindow)
        self.statusbar.setObjectName(u"statusbar")
        TranslateWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOption.menuAction())
        self.menuOption.addAction(self.actionSet_DeepL_API_Key)

        self.retranslateUi(TranslateWindow)
        QMetaObject.connectSlotsByName(TranslateWindow)

        self.TranslateWindow: QMainWindow = TranslateWindow

    # setupUi

    def retranslateUi(self, TranslateWindow):
        TranslateWindow.setWindowTitle(QCoreApplication.translate("TranslateWindow", u"Translate Window", None))
        self.actionSet_DeepL_API_Key.setText(QCoreApplication.translate("TranslateWindow", u"Set DeepL API Key", None))
        self.menuOption.setTitle(QCoreApplication.translate("TranslateWindow", u"Option", None))

    # retranslateUi

    def customConnect(self, kanjiBrowser: kanjiBrowserGUI.Ui_kanjiIndex):
        self.languageSetup = 0

        self.translationMode.addItem('Google Translator')
        # self.translationMode.addItem('DeepL Translator')
        self.translationMode.currentTextChanged.connect(self.setLanguageMode)
        self.languageMode.currentTextChanged.connect(partial(self.languageController, force=True, ))
        self.setLanguageMode()

        self.oldText = ''
        self.oldTextCursor = ''
        self.selectedState = False
        self.selectedOldText = ''

        self.kanjiBrowser = kanjiBrowser
        self.timerCursor = QTimer()
        self.timerCursor.setInterval(500)
        self.timerCursor.timeout.connect(self.getCursorSelected)
        self.timerCursor.start()

        self.timerTranslate = QTimer()
        self.timerTranslate.setInterval(3000)
        self.timerTranslate.timeout.connect(self.showSelected)
        self.timerTranslate.start()

        self.actionSet_DeepL_API_Key.triggered.connect(self.setDeepLAPIKey)
        # self.TranslateWindow.close()
        self.TranslateWindow.closeEvent = partial(self.closeWindow, self.TranslateWindow.closeEvent)

    def setDeepLAPIKey(self):
        self.oldText = self.inputTextEdit.toPlainText()
        self.apiInputWindow = QDialog()
        self.apiInputDialog = APIInput.Ui_Dialog()
        self.apiInputWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.apiInputDialog.setupUi(self.apiInputWindow)
        self.apiInputDialog.customConnect(setting)
        self.apiInputWindow.show()

    def getCursorSelected(self):
        try:
            self.cursor = self.inputTextEdit.textCursor()
            if self.cursor.selectionStart() == self.cursor.selectionEnd():
                text = self.inputTextEdit.toPlainText()[self.cursor.selectionStart() - 1:self.cursor.selectionEnd()]
                self.selectedState = False
            else:
                text = self.inputTextEdit.toPlainText()[self.cursor.selectionStart():self.cursor.selectionEnd()]
                self.selectedState = True
                self.oldTextCursor = text
            if self.selectedOldText != text:
                if len(text) == 1:
                    if self.oldTextCursor.count(text) >= 1:
                        self.kanjiBrowser.toIndexText(text, list=self.oldTextCursor)
                    else:
                        # self.translate()
                        if self.oldTextCursor != self.simpleFormat(self.oldText):
                            self.oldTextCursor = self.simpleFormat(self.oldText)
                            self.kanjiBrowser.toIndexText(text, list=self.oldTextCursor)
                        else:
                            self.kanjiBrowser.toIndexText(text)
                elif len(text) == 0:
                    pass
                else:
                    self.kanjiBrowser.fillterWord(self.simpleFormat(text), searched=True, absolute=True)
                self.selectedOldText = text
                # self.kanjiBrowser.toIndexText(text)
        except RuntimeError:
            self.timerCursor.stop()

    def simpleFormat(self, text):
        return text.strip().replace('\n', '').replace('　', '').replace(' ', '')

    def showSelected(self, *args, **kwargs):
        try:
            if self.selectedState is False:
                newTexts = self.inputTextEdit.toPlainText()
                if (self.oldText != newTexts and newTexts.strip() != '') or (
                        kwargs.get('force') and newTexts.strip() != ''):
                    self.oldText = newTexts
                    text = self.simpleFormat(self.oldText)
                    self.kanjiBrowser.appendTraslated(text)
                    try:
                        translated_texts = self.translateController(newTexts, 'ja')
                    except deep_translator.exceptions.NotValidPayload:
                        pass
                    self.outputTextEdit.setPlainText('')
                    for translated_text in translated_texts:
                        self.outputTextEdit.appendPlainText(translated_text)
                    self.kanjiBrowser.fillterWord(text, searched=True, absolute=True)
        except RuntimeError as ex:
            print(ex)
            self.timerTranslate.stop()
        except AttributeError:
            pass

    def languageController(self, text, **kwargs):
        # Doing this because I don't really know how to signal 2 functions at once...
        self.showSelected(**kwargs)
        if self.languageSetup != 0:
            setting.googleCurrentLanguage = text
            setting.commitToFile()
        self.languageSetup += 1

    def translateController(self, text, source) -> List:
        modeText = self.translationMode.currentText()
        target = self.languageMode.currentText()
        solution = []
        len_text = len(text)
        partial_texts = []
        if len_text > 1970:
            i = 0
            while i <= len_text:
                prev = i
                if i + 1970 >= len_text:
                    i = len_text + 1
                else:
                    i += 1970
                partial_texts.append(text[prev:i])
        else:
            partial_texts.append(text)

        if modeText == 'Google Translator':
            # solution = GoogleTranslator(source=source, target=target.lower()).translate(text)
            solution = self.translateGoogle(partial_texts, source, target.lower())
            # time.sleep(1)
            # print(solution)
        # elif modeText == 'DeepL Translator':
        #     solution = self.translateDeepL(text, source, target.lower())
        # print(solution)
        return solution

    def closeWindow(self, func, func2):
        # print(a, func)
        # print('a')
        # print(f'{a=}, {func=}')
        self.kanjiBrowser.setWordList(SQLController.getAllObjects())
        # func()

    def setLanguageMode(self):
        modeText = self.translationMode.currentText()
        self.languageMode.clear()
        if modeText == 'Google Translator':
            self.languageMode.addItems(i.capitalize() for i in GoogleTranslator.get_supported_languages())
        elif modeText == 'DeepL Translator':
            for item, _ in DeepL._languages.items():
                self.languageMode.addItem(item.capitalize())
        for i in range(self.languageMode.count()):
            # print(self.languageMode.itemText(i))
            if self.languageMode.itemText(i) == setting.googleCurrentLanguage:
                self.languageMode.setCurrentIndex(i)
                break

    def translateGoogle(self, text: List, source, target) -> List:
        if len(text) == 1:
            return [GoogleTranslator(source=source, target=target).translate(text[0])]
        else:
            batch = GoogleTranslator(source=source, target=target).translate_batch(text)
            return batch

    def translateDeepL(self, text, source, target):
        return DeepL(api_key=setting.deepLAPI, source=source, target=target, use_free_api=True).translate(text)
