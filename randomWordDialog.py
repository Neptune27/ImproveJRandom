# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomWordDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import jsonController


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(561, 70)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QSize(561, 70))
        Settings.setMaximumSize(QSize(561, 70))

        self.horizontalLayout = QHBoxLayout(Settings)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.questionTypeWidget = QWidget(Settings)
        self.questionTypeWidget.setObjectName(u"questionTypeWidget")
        self.questionLayout = QVBoxLayout(self.questionTypeWidget)
        self.questionLayout.setObjectName(u"questionLayout")
        self.questionLayout.setContentsMargins(0, 0, 0, 0)
        self.questionLabel = QLabel(self.questionTypeWidget)
        self.questionLabel.setObjectName(u"questionLabel")

        self.questionLayout.addWidget(self.questionLabel)

        self.questionComboBox = QComboBox(self.questionTypeWidget)
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.setObjectName(u"questionComboBox")

        self.questionLayout.addWidget(self.questionComboBox)

        self.horizontalLayout.addWidget(self.questionTypeWidget)

        self.answerTypeWidget = QWidget(Settings)
        self.answerTypeWidget.setObjectName(u"answerTypeWidget")
        self.answerLayout = QVBoxLayout(self.answerTypeWidget)
        self.answerLayout.setObjectName(u"answerLayout")
        self.answerLayout.setContentsMargins(0, 0, 0, 0)
        self.answerLabel = QLabel(self.answerTypeWidget)
        self.answerLabel.setObjectName(u"answerLabel")

        self.answerLayout.addWidget(self.answerLabel)

        self.answerComboBox = QComboBox(self.answerTypeWidget)
        self.answerComboBox.addItem("")
        self.answerComboBox.addItem("")
        self.answerComboBox.addItem("")
        self.answerComboBox.addItem("")
        self.answerComboBox.addItem("")
        self.answerComboBox.addItem("")
        self.answerComboBox.setObjectName(u"answerComboBox")

        self.answerLayout.addWidget(self.answerComboBox)

        self.horizontalLayout.addWidget(self.answerTypeWidget)

        self.numQuestionWidget = QWidget(Settings)
        self.numQuestionWidget.setObjectName(u"numQuestionWidget")
        self.numQuestionLayout = QVBoxLayout(self.numQuestionWidget)
        self.numQuestionLayout.setObjectName(u"numQuestionLayout")
        self.numQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.numQuestionLabel = QLabel(self.numQuestionWidget)
        self.numQuestionLabel.setObjectName(u"numQuestionLabel")

        self.numQuestionLayout.addWidget(self.numQuestionLabel)

        self.numQuestionComboBox = QComboBox(self.numQuestionWidget)
        self.numQuestionComboBox.setObjectName(u"numQuestionComboBox")

        self.numQuestionLayout.addWidget(self.numQuestionComboBox)

        self.horizontalLayout.addWidget(self.numQuestionWidget)

        self.quitAcceptWidget = QWidget(Settings)
        self.quitAcceptWidget.setObjectName(u"quitAcceptWidget")
        self.acceptQuitLayout = QVBoxLayout(self.quitAcceptWidget)
        self.acceptQuitLayout.setSpacing(0)
        self.acceptQuitLayout.setObjectName(u"acceptQuitLayout")
        self.acceptQuitLayout.setContentsMargins(0, 0, 0, 0)
        self.quitButton = QPushButton(self.quitAcceptWidget)
        self.quitButton.setObjectName(u"quitButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy1)

        self.acceptQuitLayout.addWidget(self.quitButton)

        self.acceptButton = QPushButton(self.quitAcceptWidget)
        self.acceptButton.setObjectName(u"acceptButton")
        sizePolicy1.setHeightForWidth(self.acceptButton.sizePolicy().hasHeightForWidth())
        self.acceptButton.setSizePolicy(sizePolicy1)

        self.acceptQuitLayout.addWidget(self.acceptButton)

        self.horizontalLayout.addWidget(self.quitAcceptWidget)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
        self.mainObject = Settings
        self.var = {}
        self.len = 0
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.questionLabel.setText(QCoreApplication.translate("Settings", u"Question Type", None))
        self.questionComboBox.setItemText(0, QCoreApplication.translate("Settings", u"Kanji", None))
        self.questionComboBox.setItemText(1, QCoreApplication.translate("Settings", u"Phi\u00ean \u00c2m", None))
        self.questionComboBox.setItemText(2, QCoreApplication.translate("Settings", u"English", None))
        self.questionComboBox.setItemText(3, QCoreApplication.translate("Settings", u"Ti\u1ebfng Vi\u1ec7t", None))
        self.questionComboBox.setItemText(4, QCoreApplication.translate("Settings", u"Kun", None))
        self.questionComboBox.setItemText(5, QCoreApplication.translate("Settings", u"On", None))

        self.answerLabel.setText(QCoreApplication.translate("Settings", u"Answer Type", None))
        self.answerComboBox.setItemText(0, QCoreApplication.translate("Settings", u"Kanji", None))
        self.answerComboBox.setItemText(1, QCoreApplication.translate("Settings", u"Phi\u00ean \u00c2m", None))
        self.answerComboBox.setItemText(2, QCoreApplication.translate("Settings", u"English", None))
        self.answerComboBox.setItemText(3, QCoreApplication.translate("Settings", u"Ti\u1ebfng Vi\u1ec7t", None))
        self.answerComboBox.setItemText(4, QCoreApplication.translate("Settings", u"Kun", None))
        self.answerComboBox.setItemText(5, QCoreApplication.translate("Settings", u"On", None))

        self.numQuestionLabel.setText(QCoreApplication.translate("Settings", u"Number of Questions", None))
        self.quitButton.setText(QCoreApplication.translate("Settings", u"Quit", None))
        self.acceptButton.setText(QCoreApplication.translate("Settings", u"Accept", None))

    # retranslateUi

    def customConnect(self, RanWordObject):
        self.ranwordObject = RanWordObject
        self.addNumQuestion(self.len)
        self.acceptButton.clicked.connect(self.acceptClicked)
        self.quitButton.clicked.connect(self.quitClicked)
        self.var = jsonController.readType(self.len, len(self.ranwordObject.questionAllList))
        self.setComboBox(self.var['questionType'], self.questionComboBox)
        self.setComboBox(self.var['answerType'], self.answerComboBox)
        self.numQuestionComboBox.setCurrentIndex(int(self.var['len']))

    def setComboBox(self, var: str, button: QComboBox):
        if var == 'kanji':
            button.setCurrentIndex(0)
        elif var == 'mean':
            button.setCurrentIndex(1)
        elif var == 'english':
            button.setCurrentIndex(2)
        elif var == 'vietnamese':
            button.setCurrentIndex(3)
        elif var == 'kun':
            button.setCurrentIndex(4)
        elif var == 'on':
            button.setCurrentIndex(5)
        else:
            raise NotImplementedError('setComboBox not implemented this function')

    def acceptClicked(self):
        if self.numQuestionComboBox.currentText() == 'All':
            len = 0
        else:
            len = int(self.numQuestionComboBox.currentText())
        questionType = self.setType(self.questionComboBox)
        answerType = self.setType(self.answerComboBox)
        jsonController.setTypeToFile(questionType, answerType, len=len)
        self.ranwordObject.prepareQuestion(self.ranwordObject.questionAllList)
        self.mainObject.accept()

    def setType(self, button: QComboBox):
        if button.currentIndex() == 1:
            return 'mean'
        elif button.currentIndex() == 3:
            return 'vietnamese'
        else:
            return str(button.currentText()).lower()

    def quitClicked(self):
        self.mainObject.close()

    def addNumQuestion(self, len):
        self.numQuestionComboBox.clear()
        self.numQuestionComboBox.addItem("All")
        for index in range(len):
            self.numQuestionComboBox.addItem(f"{index + 1}")
