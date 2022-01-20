# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomWordWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import json
import math
import random
from functools import partial
from typing import List

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from pynput import keyboard

import fileBrowserDialog
import jsonController
import randomController
from randomWordDialog import Ui_Settings


class Ui_wordRandom(object):
    def setupUi(self, wordRandom: QMainWindow):
        if not wordRandom.objectName():
            wordRandom.setObjectName(u"wordRandom")
        # wordRandom.resize(720, 600)
        self.actionSubmit = QAction(wordRandom)
        self.actionSubmit.setObjectName(u"actionSubmit")
        self.actionReset = QAction(wordRandom)
        self.actionReset.setObjectName(u"actionReset")
        self.actionRegenerate = QAction(wordRandom)
        self.actionRegenerate.setObjectName(u"actionRegenerate")
        self.actionSubmit_2 = QAction(wordRandom)
        self.actionSubmit_2.setObjectName(u"actionSubmit_2")
        self.actionReset_2 = QAction(wordRandom)
        self.actionReset_2.setObjectName(u"actionReset_2")
        self.actionSettings = QAction(wordRandom)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionCurrent_Words = QAction(wordRandom)
        self.actionCurrent_Words.setObjectName(u"actionCurrent_Words")
        self.actionWrong_Words = QAction(wordRandom)
        self.actionWrong_Words.setObjectName(u"actionWrong_Words")
        self.actionWords_in_Current_Sessions = QAction(wordRandom)
        self.actionWords_in_Current_Sessions.setObjectName(u"actionWords_in_Current_Sessions")
        self.actionWrong_Words_in_Current_Session = QAction(wordRandom)
        self.actionWrong_Words_in_Current_Session.setObjectName(u"actionWrong_Words_in_Current_Session")
        self.actionWords_in_Current_Session = QAction(wordRandom)
        self.actionWords_in_Current_Session.setObjectName(u"actionWords_in_Current_Session")
        self.actionAuto_Save_Words = QAction(wordRandom)
        self.actionAuto_Save_Words.setObjectName(u"actionAuto_Save_Words")
        self.actionAuto_Save_Words.setCheckable(True)
        self.actionAuto_Save_Words.setChecked(True)
        self.actionAuto_Save_Wrong_Words = QAction(wordRandom)
        self.actionAuto_Save_Wrong_Words.setObjectName(u"actionAuto_Save_Wrong_Words")
        self.actionAuto_Save_Wrong_Words.setCheckable(True)
        self.actionAuto_Save_Wrong_Words.setChecked(True)
        self.actionAuto_Save_Right_Words = QAction(wordRandom)
        self.actionAuto_Save_Right_Words.setObjectName(u"actionAuto_Save_Right_Words")
        self.actionAuto_Save_Right_Words.setCheckable(True)
        self.actionAuto_Save_Right_Words.setChecked(True)
        self.actionRight_Words = QAction(wordRandom)
        self.actionRight_Words.setObjectName(u"actionRight_Words")
        self.actionRight_Words_in_Current_Session = QAction(wordRandom)
        self.actionRight_Words_in_Current_Session.setObjectName(u"actionRight_Words_in_Current_Session")
        self.centralwidget = QWidget(wordRandom)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralLayout = QHBoxLayout(self.centralwidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.questionListWidget = QListWidget(self.centralwidget)
        self.questionListWidget.setObjectName(u"questionListWidget")
        font = QFont()
        font.setPointSize(14)
        self.questionListWidget.setFont(font)

        self.centralLayout.addWidget(self.questionListWidget)

        self.answerAndQuestionWidget = QWidget(self.centralwidget)
        self.answerAndQuestionWidget.setObjectName(u"answerAndQuestionWidget")
        self.answerAndQuestionWidgetLayout = QVBoxLayout(self.answerAndQuestionWidget)
        self.answerAndQuestionWidgetLayout.setSpacing(0)
        self.answerAndQuestionWidgetLayout.setObjectName(u"answerAndQuestionWidgetLayout")
        self.answerAndQuestionWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.questionWidget = QWidget(self.answerAndQuestionWidget)
        self.questionWidget.setObjectName(u"questionWidget")
        self.questionWidgetLayout = QHBoxLayout(self.questionWidget)
        self.questionWidgetLayout.setSpacing(6)
        self.questionWidgetLayout.setObjectName(u"questionWidgetLayout")
        self.questionWidgetLayout.setContentsMargins(0, 0, 0, 9)
        self.questionBrowser = QTextBrowser(self.questionWidget)
        self.questionBrowser.setObjectName(u"questionBrowser")
        font1 = QFont()
        font1.setPointSize(17)
        self.questionBrowser.setFont(font1)

        self.questionWidgetLayout.addWidget(self.questionBrowser)

        self.answerAndQuestionWidgetLayout.addWidget(self.questionWidget)

        self.answersWidget = QWidget(self.answerAndQuestionWidget)
        self.answersWidget.setObjectName(u"answersWidget")
        self.answersWidgetLayout = QGridLayout(self.answersWidget)
        self.answersWidgetLayout.setObjectName(u"answersWidgetLayout")
        self.answersWidgetLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.answersWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.answerDButton = QPushButton(self.answersWidget)
        self.answerDButton.setObjectName(u"answerDButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerDButton.sizePolicy().hasHeightForWidth())
        self.answerDButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(18)
        self.answerDButton.setFont(font2)

        self.answersWidgetLayout.addWidget(self.answerDButton, 1, 1, 1, 1)

        self.answerCButton = QPushButton(self.answersWidget)
        self.answerCButton.setObjectName(u"answerCButton")
        sizePolicy.setHeightForWidth(self.answerCButton.sizePolicy().hasHeightForWidth())
        self.answerCButton.setSizePolicy(sizePolicy)
        self.answerCButton.setFont(font2)

        self.answersWidgetLayout.addWidget(self.answerCButton, 1, 0, 1, 1)

        self.answerBButton = QPushButton(self.answersWidget)
        self.answerBButton.setObjectName(u"answerBButton")
        sizePolicy.setHeightForWidth(self.answerBButton.sizePolicy().hasHeightForWidth())
        self.answerBButton.setSizePolicy(sizePolicy)
        self.answerBButton.setFont(font1)

        self.answersWidgetLayout.addWidget(self.answerBButton, 0, 1, 1, 1)

        self.answerAButton = QToolButton(self.answersWidget)
        self.answerAButton.setObjectName(u"answerAButton")
        sizePolicy.setHeightForWidth(self.answerAButton.sizePolicy().hasHeightForWidth())
        self.answerAButton.setSizePolicy(sizePolicy)
        self.answerAButton.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(17)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.answerAButton.setFont(font3)
        self.answerAButton.setFocusPolicy(Qt.StrongFocus)
        self.answerAButton.setAcceptDrops(False)

        self.answersWidgetLayout.addWidget(self.answerAButton, 0, 0, 1, 1)

        self.answersWidgetLayout.setRowStretch(0, 1)
        self.answersWidgetLayout.setRowStretch(1, 1)
        self.answersWidgetLayout.setColumnStretch(0, 1)
        self.answersWidgetLayout.setColumnStretch(1, 1)

        self.answerAndQuestionWidgetLayout.addWidget(self.answersWidget)

        self.answerAndQuestionWidgetLayout.setStretch(0, 1)
        self.answerAndQuestionWidgetLayout.setStretch(1, 1)

        self.centralLayout.addWidget(self.answerAndQuestionWidget)

        self.centralLayout.setStretch(0, 1)
        self.centralLayout.setStretch(1, 7)
        wordRandom.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(wordRandom)
        self.statusbar.setObjectName(u"statusbar")
        wordRandom.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(wordRandom)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 721, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave = QMenu(self.menubar)
        self.menuSave.setObjectName(u"menuSave")
        self.menuAuto_Save = QMenu(self.menuSave)
        self.menuAuto_Save.setObjectName(u"menuAuto_Save")
        self.menuCurrent = QMenu(self.menuSave)
        self.menuCurrent.setObjectName(u"menuCurrent")
        self.menuSession = QMenu(self.menuSave)
        self.menuSession.setObjectName(u"menuSession")
        wordRandom.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.actionSubmit_2)
        self.menuFile.addAction(self.actionReset_2)
        self.menuFile.addAction(self.actionSettings)
        self.menuSave.addAction(self.menuCurrent.menuAction())
        self.menuSave.addAction(self.menuSession.menuAction())
        self.menuSave.addAction(self.menuAuto_Save.menuAction())
        self.menuAuto_Save.addAction(self.actionAuto_Save_Words)
        self.menuAuto_Save.addAction(self.actionAuto_Save_Wrong_Words)
        self.menuAuto_Save.addAction(self.actionAuto_Save_Right_Words)
        self.menuCurrent.addAction(self.actionWrong_Words)
        self.menuCurrent.addAction(self.actionRight_Words)
        self.menuCurrent.addAction(self.actionCurrent_Words)
        self.menuSession.addAction(self.actionWrong_Words_in_Current_Session)
        self.menuSession.addAction(self.actionWords_in_Current_Session)
        self.menuSession.addAction(self.actionRight_Words_in_Current_Session)

        self.retranslateUi(wordRandom)

        QMetaObject.connectSlotsByName(wordRandom)
        self.wordRandomObject = wordRandom
        # self.activation

    # setupUi

    def retranslateUi(self, wordRandom):
        wordRandom.setWindowTitle(QCoreApplication.translate("wordRandom", u"Random Word", None))
        self.actionSubmit.setText(QCoreApplication.translate("wordRandom", u"Submit", None))
        self.actionReset.setText(QCoreApplication.translate("wordRandom", u"Reset", None))
        self.actionRegenerate.setText(QCoreApplication.translate("wordRandom", u"Regenerate", None))
        self.actionSubmit_2.setText(QCoreApplication.translate("wordRandom", u"Submit", None))
        self.actionReset_2.setText(QCoreApplication.translate("wordRandom", u"Reset", None))
        self.actionSettings.setText(QCoreApplication.translate("wordRandom", u"Settings", None))
        self.actionCurrent_Words.setText(QCoreApplication.translate("wordRandom", u"Current Words", None))
        self.actionWrong_Words.setText(QCoreApplication.translate("wordRandom", u"Wrong Words", None))
        self.actionWords_in_Current_Sessions.setText(
            QCoreApplication.translate("wordRandom", u"Words in Current Sessions", None))
        self.actionWrong_Words_in_Current_Session.setText(
            QCoreApplication.translate("wordRandom", u"Wrong Words in Current Session", None))
        self.actionWords_in_Current_Session.setText(
            QCoreApplication.translate("wordRandom", u"Words in Current Session", None))
        self.actionAuto_Save_Words.setText(QCoreApplication.translate("wordRandom", u"Auto Save Words", None))
        self.actionAuto_Save_Wrong_Words.setText(
            QCoreApplication.translate("wordRandom", u"Auto Save Wrong Words", None))
        self.actionAuto_Save_Right_Words.setText(
            QCoreApplication.translate("wordRandom", u"Auto Save Right Words", None))
        self.actionRight_Words.setText(QCoreApplication.translate("wordRandom", u"Right Words", None))
        self.actionRight_Words_in_Current_Session.setText(
            QCoreApplication.translate("wordRandom", u"Right Words in Current Session", None))
        self.answerDButton.setText(QCoreApplication.translate("wordRandom", u"D", None))
        self.answerCButton.setText(QCoreApplication.translate("wordRandom", u"C", None))
        self.answerBButton.setText(QCoreApplication.translate("wordRandom", u"B", None))
        self.answerAButton.setText(QCoreApplication.translate("wordRandom", u"A", None))
        self.menuFile.setTitle(QCoreApplication.translate("wordRandom", u"File", None))
        self.menuSave.setTitle(QCoreApplication.translate("wordRandom", u"Save", None))
        self.menuAuto_Save.setTitle(QCoreApplication.translate("wordRandom", u"Auto Save", None))
        self.menuCurrent.setTitle(QCoreApplication.translate("wordRandom", u"Current", None))
        self.menuSession.setTitle(QCoreApplication.translate("wordRandom", u"Session", None))

    # retranslateUi
    def keyboardOnRelease(self, key):
        if self.wordRandomObject.isActiveWindow():
            try:
                if key == keyboard.Key.enter:
                    self.setCommit()
            except AttributeError:
                pass
            try:
                if key.vk == 97 or key.vk == 49:
                    self.buttonClicked('A')
                elif key.vk == 98 or key.vk == 50:
                    self.buttonClicked('B')
                elif key.vk == 99 or key.vk == 51:
                    self.buttonClicked('C')
                elif key.vk == 100 or key.vk == 52:
                    self.buttonClicked('D')
                elif key.vk == 82:
                    self.prepareQuestion(self.questionAllList)
                # elif key.char == keyboard.Key.enter:
                #     self.setCommit()
            except AttributeError:
                pass

    def customConnect(self, questionList, kanjiBrowser):
        self.mainSettings = jsonController.Settings()
        self.wordsInSession = {}
        self.currentWords = {}
        # self.wordsInSession = ''
        # self.wrongWordInSession = ''
        # self.rightWordInSession = ''
        # self.currentWords = ''
        # self.currentWrongWords = ''
        # self.currentRightWords = ''
        self.autoSaveInit()

        self.wordRandomObject.resizeEvent = partial(self.mainObjResizeEvent,)
        self.wordRandomObject.resize(720, 600)

        self.answerAButton.clicked.connect(partial(self.resizeTextToFit, 'A', self.answerAButton))
        self.questionListWidget.currentItemChanged.connect(self.itemPosChanged)
        self.questionListWidget.clicked.connect(self.itemPosChanged)
        self.questionList = questionList
        self.kanjiBrowser = kanjiBrowser

        self.prepareQuestion(self.questionList)

        self.answerAButton.clicked.connect(partial(self.buttonClicked, 'A'))
        self.answerBButton.clicked.connect(partial(self.buttonClicked, 'B'))
        self.answerCButton.clicked.connect(partial(self.buttonClicked, 'C'))
        self.answerDButton.clicked.connect(partial(self.buttonClicked, 'D'))

        self.wordRandomObject.closeEvent = self.closeEvent

        # File action bar
        self.actionSubmit_2.triggered.connect(self.setCommit)
        self.actionSettings.triggered.connect(self.randomWordSetting)
        self.actionReset_2.triggered.connect(partial(self.prepareQuestion, self.questionAllList))

        # Save action bar
        self.actionCurrent_Words.triggered.connect(partial(self.saveWord, self.currentWords, 0, 'Current Words'))
        self.actionRight_Words.triggered.connect(partial(self.saveWord, self.currentWords, 1, 'Current Right Words'))
        self.actionWrong_Words.triggered.connect(partial(self.saveWord, self.currentWords, 2, 'Current Wrong Words'))

        self.actionWords_in_Current_Session.triggered.connect(
            partial(self.saveWord, self.wordsInSession, 0, 'Words In Session'))
        self.actionRight_Words_in_Current_Session.triggered.connect(
            partial(self.saveWord, self.wordsInSession, 1, 'Right Words In Session'))
        self.actionWrong_Words_in_Current_Session.triggered.connect(
            partial(self.saveWord, self.wordsInSession, 2, 'Wrong Words In Session'))

        # Autosave Init
        self.actionAuto_Save_Words.setChecked(self.mainSettings.autoSaveWords)
        self.actionAuto_Save_Right_Words.setChecked(self.mainSettings.autoSaveRightWords)
        self.actionAuto_Save_Wrong_Words.setChecked(self.mainSettings.autoSaveWrongWords)

        # Autosave Connect
        self.actionAuto_Save_Words.triggered.connect(
            partial(self.setSettings, 'autoSaveWords', self.actionAuto_Save_Words))
        self.actionAuto_Save_Right_Words.triggered.connect(
            partial(self.setSettings, 'autoSaveRightWords', self.actionAuto_Save_Right_Words))
        self.actionAuto_Save_Wrong_Words.triggered.connect(
            partial(self.setSettings, 'autoSaveWrongWords', self.actionAuto_Save_Wrong_Words))

        self.colorYellow = QColor('#DEA00B')
        self.colorGreen = QColor('#00ad0c')
        self.colorRed = QColor('#F5011F')
        self.colorWhite = QColor('#ffffff')
        self.colorBlue = QColor('#0053FA')

        self.keyboardListener = keyboard.Listener(on_release=self.keyboardOnRelease)
        self.keyboardListener.start()

    def closeEvent(self, event):
        self.keyboardListener.stop()
        del self.wordRandomObject
        del self

    def prepareQuestion(self, questionList: List, **kwargs):
        random.shuffle(questionList)
        self.questionAllList = questionList
        self.commit = False
        self.questionListWidget.clear()
        try:
            with open('./Data/questionType.json', 'r', encoding='UTF-8') as questionFile:
                self.var = json.loads(questionFile.read())
        except Exception as ex:
            jsonController.setTypeToFile('kanji', 'english', len=0)
        self.questionType = self.var['questionType']
        self.answerType = self.var['answerType']
        self.questionLength = self.var['len']
        self.answerList, self.questionList = randomController.randomWordInWordList(questionList,
                                                                                   len=self.questionLength)

        # Add current random word for save
        self.currentWords = {jpObject.kanji: None for jpObject in self.answerList}

        self.answer = [[i, 0] for i in range(len(self.answerList))]
        self.questionListWidget.addItems([f'Câu {i + 1}' for i in range(len(self.answerList))])
        self.wordRandomObject.setWindowTitle(
            f"Random {self.questionType.capitalize()} - {self.answerType.capitalize()},"
            f" Lenght: {len(self.questionList)}, Total: {len(self.questionAllList)}")

        self.questionListWidget.setCurrentRow(0)

    def randomWordSetting(self):
        try:
            self.wordRandomSettingDialog = QDialog()
            self.wordRandomSettingDialog.setAttribute(Qt.WA_DeleteOnClose)
            self.wordRandomSetting = Ui_Settings()
            self.wordRandomSetting.setupUi(self.wordRandomSettingDialog)
            self.wordRandomSetting.len = len(self.questionAllList)
            self.wordRandomSetting.customConnect(self)
            self.wordRandomSettingDialog.show()
        except Exception as ex:
            print(ex)

    def itemPosChanged(self):
        # print(f'[INFO] Row currently selected is: {self.questionListWidget.currentIndex().row()}')
        if self.commit and self.questionType == 'kanji':
            self.kanjiBrowser.toIndexText(self.questionBrowser.toPlainText())
        index = self.questionListWidget.currentIndex().row()
        self.setTextQuestion(index, f'{self.questionType}')
        self.setTextButton('A', f'{self.answerType}', self.answerAButton, index)
        self.setTextButton('B', f'{self.answerType}', self.answerBButton, index)
        self.setTextButton('C', f'{self.answerType}', self.answerCButton, index)
        self.setTextButton('D', f'{self.answerType}', self.answerDButton, index)
        self.setButtonStyle(index)
        if self.questionListWidget.currentIndex().row() < 0:
            self.questionListWidget.setCurrentRow(0)

    def setTextQuestion(self, index, type):
        self.questionBrowser.setText(getattr(self.answerList[index], f'{type}'))

    def setTextButton(self, whichButton: str, type, button: QPushButton, index):
        if whichButton == 'A':
            button.setText(self.resizeTextToFit(getattr(self.questionList[index][0], f'{type}'), button))
        elif whichButton == 'B':
            button.setText(self.resizeTextToFit(getattr(self.questionList[index][1], f'{type}'), button))
        elif whichButton == 'C':
            button.setText(self.resizeTextToFit(getattr(self.questionList[index][2], f'{type}'), button))
        elif whichButton == 'D':
            button.setText(self.resizeTextToFit(getattr(self.questionList[index][3], f'{type}'), button))

    def setButtonStyle(self, index):
        if self.answer[index][1] == 'A':
            self.answerAButton.setStyleSheet("background-color: #DEA00B")
            self.answerBButton.setStyleSheet("")
            self.answerCButton.setStyleSheet("")
            self.answerDButton.setStyleSheet("")
        elif self.answer[index][1] == 'B':
            self.answerAButton.setStyleSheet("")
            self.answerBButton.setStyleSheet("background-color: #DEA00B")
            self.answerCButton.setStyleSheet("")
            self.answerDButton.setStyleSheet("")
        elif self.answer[index][1] == 'C':
            self.answerAButton.setStyleSheet("")
            self.answerBButton.setStyleSheet("")
            self.answerCButton.setStyleSheet("background-color: #DEA00B")
            self.answerDButton.setStyleSheet("")
        elif self.answer[index][1] == 'D':
            self.answerAButton.setStyleSheet("")
            self.answerBButton.setStyleSheet("")
            self.answerCButton.setStyleSheet("")
            self.answerDButton.setStyleSheet("background-color: #DEA00B")
        else:
            self.answerAButton.setStyleSheet("")
            self.answerBButton.setStyleSheet("")
            self.answerCButton.setStyleSheet("")
            self.answerDButton.setStyleSheet("")

        if self.commit:
            try:
                if self.answer[index][0].kanji != self.answerList[index].kanji:
                    if self.answer[index][1] == 'A':
                        self.answerAButton.setStyleSheet("background-color: #F5011F")
                    elif self.answer[index][1] == 'B':
                        self.answerBButton.setStyleSheet("background-color: #F5011F")
                    elif self.answer[index][1] == 'C':
                        self.answerCButton.setStyleSheet("background-color: #F5011F")
                    elif self.answer[index][1] == 'D':
                        self.answerDButton.setStyleSheet("background-color: #F5011F")
                if self.answerList[index].kanji == self.questionList[index][0].kanji:
                    self.answerAButton.setStyleSheet("background-color: #27FF0D")
                elif self.answerList[index].kanji == self.questionList[index][1].kanji:
                    self.answerBButton.setStyleSheet("background-color: #27FF0D")
                elif self.answerList[index].kanji == self.questionList[index][2].kanji:
                    self.answerCButton.setStyleSheet("background-color: #27FF0D")
                elif self.answerList[index].kanji == self.questionList[index][3].kanji:
                    self.answerDButton.setStyleSheet("background-color: #27FF0D")
            except AttributeError:
                self.answerAButton.setStyleSheet("background-color: #F5011F")
                self.answerBButton.setStyleSheet("background-color: #F5011F")
                self.answerCButton.setStyleSheet("background-color: #F5011F")
                self.answerDButton.setStyleSheet("background-color: #F5011F")

    def setCommit(self):

        self.commit = True

        for index in range(self.questionListWidget.count()):
            try:
                if self.answer[index][0].kanji == self.answerList[index].kanji:
                    self.questionListWidget.item(index).setForeground(self.colorGreen)
                    # self.currentRightWords += self.answerList[index].kanji
                    self.currentWords[self.answerList[index].kanji] = True
                    try:
                        if self.wordsInSession[self.answerList[index].kanji] == 2:
                            pass
                        else:
                            self.wordsInSession[self.answerList[index].kanji] = 1
                    except KeyError:
                        self.wordsInSession[self.answerList[index].kanji] = 1
                else:
                    self.questionListWidget.item(index).setForeground(self.colorRed)
                    self.currentWords[self.answerList[index].kanji] = 2
                    self.wordsInSession[self.answerList[index].kanji] = 2
                    # if self.answerList[index].kanji not in self.currentWrongWords:
                    #     self.currentWrongWords += self.answerList[index].kanji
            except AttributeError:
                self.questionListWidget.item(index).setForeground(self.colorBlue)
                self.currentWords[self.answerList[index].kanji] = 3
                self.wordsInSession[self.answerList[index].kanji] = 3
                # if self.answerList[index].kanji not in self.currentWrongWords:
                # self.currentWrongWords += self.answerList[index].kanji
        self.updateIndex()

        # for text in self.currentWrongWords:
        #     if text not in self.wrongWordInSession:
        #         self.wrongWordInSession += text
        #
        # for text in self.currentRightWords:
        #     if text not in self.rightWordInSession:
        #         self.rightWordInSession += text
        self.autoSaveSave()

        # print(f"-------------------------\n[INFO] {self.wordsInSession=}\n[INFO] {self.currentWords=} \n-------------------------\n ")

    def updateIndex(self):
        """
        This method make key listener not crash when set it to setCommit method, idk why it crash, maybe something
        incompatible with keyboardListener and TextBrowser.setText, so, calling it by IndexChanged method instead
        """
        currentIndex = self.questionListWidget.currentIndex().row()
        self.questionListWidget.setCurrentRow(currentIndex + 1)
        self.questionListWidget.setCurrentRow(currentIndex)

    def resizeTextToFit(self, text, button: QPushButton):
        if text is None:
            text = 'None'
        witdh = button.width()
        y = len(text) * 17 / witdh
        if y > 1:
            chunk = math.ceil(y)
            index = round(len(text) / chunk)
            for i in range(chunk - 1):
                starting = index * (i + 1)
                while starting < index * (i + 2):
                    if starting >= len(text):
                        break
                    if text[starting] == ' ':
                        text = text[:starting + 1] + '\n' + text[starting + 1:]
                        break
                    starting += 1

        return text

    def buttonClicked(self, whichButton):
        index = self.questionListWidget.currentIndex().row()
        try:
            if self.commit is False:
                if whichButton == 'A':
                    self.answer[index][0] = self.questionList[index][0]
                    self.answer[index][1] = 'A'
                elif whichButton == 'B':
                    self.answer[index][0] = self.questionList[index][1]
                    self.answer[index][1] = 'B'
                elif whichButton == 'C':
                    self.answer[index][0] = self.questionList[index][2]
                    self.answer[index][1] = 'C'
                elif whichButton == 'D':
                    self.answer[index][0] = self.questionList[index][3]
                    self.answer[index][1] = 'D'
                self.questionListWidget.item(index).setForeground(self.colorYellow)
            else:
                if whichButton == 'A':
                    self.kanjiBrowser.toIndexText(self.questionList[index][0].kanji)
                elif whichButton == 'B':
                    self.kanjiBrowser.toIndexText(self.questionList[index][1].kanji)
                elif whichButton == 'C':
                    self.kanjiBrowser.toIndexText(self.questionList[index][2].kanji)
                elif whichButton == 'D':
                    self.kanjiBrowser.toIndexText(self.questionList[index][3].kanji)
        except AttributeError:
            self.questionListWidget.setCurrentRow(0)
        if self.commit is False:
            if index + 2 > self.questionListWidget.count():
                index = 0
                self.questionListWidget.setCurrentRow(index)
            else:
                self.questionListWidget.setCurrentRow(index + 1)

    def saveWord(self, dictList: dict, options, heading=None):
        fileBrowserDialog.SaveDialog(dictList, options, heading)

    def autoSaveInit(self):
        self.autoSaveWords = fileBrowserDialog.AutoSave(self.mainSettings.words, None)
        self.autoSaveRightWords = fileBrowserDialog.AutoSave(self.mainSettings.correctWords, True)
        self.autoSaveWrongWords = fileBrowserDialog.AutoSave(self.mainSettings.wrongWords, False)

    def autoSaveSave(self):
        if self.actionAuto_Save_Words.isChecked():
            self.autoSaveWords.text = self.currentWords
            self.autoSaveWords.save()
        if self.actionAuto_Save_Right_Words.isChecked():
            self.autoSaveRightWords.text = self.currentWords
            self.autoSaveRightWords.save()
        if self.actionAuto_Save_Wrong_Words.isChecked():
            self.autoSaveWrongWords.text = self.currentWords
            self.autoSaveWrongWords.save()

    def setSettings(self, attribute, typed: QAction) -> None:
        changes = typed.isChecked()
        setattr(self.mainSettings, attribute, changes)
        self.mainSettings.commitToFile()

    def mainObjResizeEvent(self, func):
        self.itemPosChanged()
        # print(func)