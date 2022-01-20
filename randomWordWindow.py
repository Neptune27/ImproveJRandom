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

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import SQLController
import jsonController
import randomController
from randomWordDialog import Ui_Settings


class Ui_wordRandom(object):
    def setupUi(self, wordRandom):
        if not wordRandom.objectName():
            wordRandom.setObjectName(u"wordRandom")
        wordRandom.resize(721, 600)
        self.actionSubmit = QAction(wordRandom)
        self.actionSubmit.setObjectName(u"actionSubmit")
        self.actionReset = QAction(wordRandom)
        self.actionReset.setObjectName(u"actionReset")
        self.actionSettings = QAction(wordRandom)
        self.actionSettings.setObjectName(u"actionSettings")
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
        self.menubar = QMenuBar(wordRandom)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 721, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        wordRandom.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wordRandom)
        self.statusbar.setObjectName(u"statusbar")
        wordRandom.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSubmit)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionSettings)

        self.retranslateUi(wordRandom)

        QMetaObject.connectSlotsByName(wordRandom)
        self.customConnect()
        self.a = SQLController.getAllObjects()

    # setupUi

    def retranslateUi(self, wordRandom):
        wordRandom.setWindowTitle(QCoreApplication.translate("wordRandom", u"MainWindow", None))
        self.actionSubmit.setText(QCoreApplication.translate("wordRandom", u"Submit", None))
        self.actionReset.setText(QCoreApplication.translate("wordRandom", u"Reset", None))
        self.actionSettings.setText(QCoreApplication.translate("wordRandom", u"Settings", None))
        self.answerDButton.setText(QCoreApplication.translate("wordRandom", u"D", None))
        self.answerCButton.setText(QCoreApplication.translate("wordRandom", u"C", None))
        self.answerBButton.setText(QCoreApplication.translate("wordRandom", u"B", None))
        self.answerAButton.setText(QCoreApplication.translate("wordRandom", u"A", None))
        self.menuFile.setTitle(QCoreApplication.translate("wordRandom", u"File", None))

    # retranslateUi

    def customConnect(self):
        self.answerAButton.clicked.connect(partial(self.resizeTextToFit, 'A', self.answerAButton))
        self.questionListWidget.currentItemChanged.connect(self.itemPosChanged)
        self.questionListWidget.clicked.connect(self.itemPosChanged)
        self.questionList = SQLController.getAllObjects()
        self.actionReset.triggered.connect(partial(self.prepareQuestion, self.questionList))
        self.prepareQuestion(self.questionList)

        self.answerAButton.clicked.connect(partial(self.buttonClicked, 'A'))
        self.answerBButton.clicked.connect(partial(self.buttonClicked, 'B'))
        self.answerCButton.clicked.connect(partial(self.buttonClicked, 'C'))
        self.answerDButton.clicked.connect(partial(self.buttonClicked, 'D'))

        self.actionSubmit.triggered.connect(self.setCommit)
        self.actionSettings.triggered.connect(self.randomWordSetting)

        self.colorYellow = QColor('#DEA00B')
        self.colorGreen = QColor('#00ad0c')
        self.colorRed = QColor('#F5011F')
        self.colorWhite = QColor('#ffffff')

    def prepareQuestion(self, questionList: list, **kwargs):
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
        self.answer = [[i, 0] for i in range(len(self.answerList))]
        self.questionListWidget.addItems([f'Câu {i + 1}' for i in range(len(self.answerList))])
        self.questionListWidget.setCurrentRow(0)

    def randomWordSetting(self):
        try:
            self.wordRandomSettingDialog = QDialog()
            self.wordRandomSettingDialog.setAttribute(Qt.WA_DeleteOnClose)
            self.wordRandomSetting = Ui_Settings()
            self.wordRandomSetting.setupUi(self.wordRandomSettingDialog)
            self.wordRandomSetting.len = len(self.questionAllList)
            self.wordRandomSetting.customConnect()
            self.wordRandomSettingDialog.show()
        except Exception as ex:
            print(ex)

    def itemPosChanged(self):
        index = self.questionListWidget.currentIndex().row()
        self.setTextQuestion(index, f'{self.questionType}')
        self.setTextButton('A', f'{self.answerType}', self.answerAButton, index)
        self.setTextButton('B', f'{self.answerType}', self.answerBButton, index)
        self.setTextButton('C', f'{self.answerType}', self.answerCButton, index)
        self.setTextButton('D', f'{self.answerType}', self.answerDButton, index)
        self.setButtonStyle(index)

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
                else:
                    self.questionListWidget.item(index).setForeground(self.colorRed)
            except AttributeError:
                self.questionListWidget.item(index).setForeground(self.colorRed)
        self.questionListWidget.setCurrentRow(0)

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
        if self.commit is False:
            self.questionListWidget.item(index).setForeground(self.colorYellow)
        if index + 2 > self.questionListWidget.count():
            index = 0
            self.questionListWidget.setCurrentRow(index)
        else:
            self.questionListWidget.setCurrentRow(index + 1)
