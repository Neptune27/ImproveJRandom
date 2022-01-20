# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomWordWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_wordRandom(object):
    def setupUi(self, wordRandom):
        if not wordRandom.objectName():
            wordRandom.setObjectName(u"wordRandom")
        wordRandom.resize(721, 600)
        self.actionSubmit = QAction(wordRandom)
        self.actionSubmit.setObjectName(u"actionSubmit")
        self.actionReset = QAction(wordRandom)
        self.actionReset.setObjectName(u"actionReset")
        self.actionRegenerate = QAction(wordRandom)
        self.actionRegenerate.setObjectName(u"actionRegenerate")
        self.centralwidget = QWidget(wordRandom)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralLayout = QHBoxLayout(self.centralwidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.questionListWidget = QListWidget(self.centralwidget)
        self.questionListWidget.setObjectName(u"questionListWidget")
        font = QFont()
        font.setPointSize(9)
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
        self.menuFile.addAction(self.actionRegenerate)

        self.retranslateUi(wordRandom)

        QMetaObject.connectSlotsByName(wordRandom)
    # setupUi

    def retranslateUi(self, wordRandom):
        wordRandom.setWindowTitle(QCoreApplication.translate("wordRandom", u"Random Word", None))
        self.actionSubmit.setText(QCoreApplication.translate("wordRandom", u"Submit", None))
        self.actionReset.setText(QCoreApplication.translate("wordRandom", u"Reset", None))
        self.actionRegenerate.setText(QCoreApplication.translate("wordRandom", u"Regenerate", None))
        self.answerDButton.setText(QCoreApplication.translate("wordRandom", u"D", None))
        self.answerCButton.setText(QCoreApplication.translate("wordRandom", u"C", None))
        self.answerBButton.setText(QCoreApplication.translate("wordRandom", u"B", None))
        self.answerAButton.setText(QCoreApplication.translate("wordRandom", u"A", None))
        self.menuFile.setTitle(QCoreApplication.translate("wordRandom", u"File", None))
    # retranslateUi

