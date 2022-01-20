import traceback
from functools import partial
from multiprocessing import Process, freeze_support
from typing import List

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import InSelectedItemsGUI
import SQLController
import fileBrowserDialog
import progressBarUI
import randomWordWindow
import translateProcess
import translateWindowGUI
import wordController
from classType import JapanWords
from jsonController import Settings

# from importlib import reload

settings = Settings()


class Ui_kanjiIndex(object):
    def setupUi(self, kanjiIndex):
        if not kanjiIndex.objectName():
            kanjiIndex.setObjectName(u"kanjiIndex")
        kanjiIndex.resize(947, 672)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(kanjiIndex.sizePolicy().hasHeightForWidth())
        kanjiIndex.setSizePolicy(sizePolicy)
        kanjiIndex.setWindowTitle(u"Kanji Index")
        self.actionIn_Selected_File = QAction(kanjiIndex)
        self.actionIn_Selected_File.setObjectName(u"actionIn_Selected_File")
        self.actionIn_Selected_Item_s = QAction(kanjiIndex)
        self.actionIn_Selected_Item_s.setObjectName(u"actionIn_Selected_Item_s")
        self.actionApply = QAction(kanjiIndex)
        self.actionApply.setObjectName(u"actionApply")
        self.actionResety = QAction(kanjiIndex)
        self.actionResety.setObjectName(u"actionResety")
        self.actionReset = QAction(kanjiIndex)
        self.actionReset.setObjectName(u"actionReset")
        self.actionDelete = QAction(kanjiIndex)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionIn_Selected_Item_s_In_File = QAction(kanjiIndex)
        self.actionIn_Selected_Item_s_In_File.setObjectName(u"actionIn_Selected_Item_s_In_File")
        self.actionIn_Database = QAction(kanjiIndex)
        self.actionIn_Database.setObjectName(u"actionIn_Database")
        self.actionCurrent_List = QAction(kanjiIndex)
        self.actionCurrent_List.setObjectName(u"actionCurrent_List")
        self.actionAll_Word = QAction(kanjiIndex)
        self.actionAll_Word.setObjectName(u"actionAll_Word")
        self.actionAll_Words = QAction(kanjiIndex)
        self.actionAll_Words.setObjectName(u"actionAll_Words")
        self.actionCurrent_Words_List = QAction(kanjiIndex)
        self.actionCurrent_Words_List.setObjectName(u"actionCurrent_Words_List")
        self.actionAll_Words_List = QAction(kanjiIndex)
        self.actionAll_Words_List.setObjectName(u"actionAll_Words_List")
        self.centralwidget = QWidget(kanjiIndex)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralLayout = QGridLayout(self.centralwidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.mainwidget = QWidget(self.centralwidget)
        self.mainwidget.setObjectName(u"mainwidget")
        self.mainLayout = QGridLayout(self.mainwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.listmainwidget = QWidget(self.mainwidget)
        self.listmainwidget.setObjectName(u"listmainwidget")
        self.listwidgetLayout = QVBoxLayout(self.listmainwidget)
        self.listwidgetLayout.setSpacing(0)
        self.listwidgetLayout.setObjectName(u"listwidgetLayout")
        self.listwidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.fillterLineEdit = QLineEdit(self.listmainwidget)
        self.fillterLineEdit.setObjectName(u"fillterLineEdit")

        self.listwidgetLayout.addWidget(self.fillterLineEdit)

        self.wordListWidget = QListWidget(self.listmainwidget)
        self.wordListWidget.setObjectName(u"wordListWidget")
        font = QFont()
        font.setPointSize(14)
        self.wordListWidget.setFont(font)
        self.wordListWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.wordListWidget.setSelectionRectVisible(False)
        self.wordListWidget.setSortingEnabled(True)

        self.listwidgetLayout.addWidget(self.wordListWidget)


        self.mainLayout.addWidget(self.listmainwidget, 0, 0, 1, 1)

        self.infowidget = QWidget(self.mainwidget)
        self.infowidget.setObjectName(u"infowidget")
        self.infowidgetLayout = QVBoxLayout(self.infowidget)
        self.infowidgetLayout.setObjectName(u"infowidgetLayout")
        self.infowidgetLayout.setContentsMargins(9, 0, 0, 0)
        self.englishphienlevelWidget = QWidget(self.infowidget)
        self.englishphienlevelWidget.setObjectName(u"englishphienlevelWidget")
        self.englishphienlevelWidget.setMaximumSize(QSize(16777215, 40))
        self.englishphienlevelWidgetLayout = QHBoxLayout(self.englishphienlevelWidget)
        self.englishphienlevelWidgetLayout.setObjectName(u"englishphienlevelWidgetLayout")
        self.englishphienlevelWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.englishPlainEdit = QPlainTextEdit(self.englishphienlevelWidget)
        self.englishPlainEdit.setObjectName(u"englishPlainEdit")
        self.englishPlainEdit.setMaximumSize(QSize(16777215, 50))
        self.englishPlainEdit.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(18)
        self.englishPlainEdit.setFont(font1)
        self.englishPlainEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.englishPlainEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.englishphienlevelWidgetLayout.addWidget(self.englishPlainEdit)

        self.phienEdit = QTextEdit(self.englishphienlevelWidget)
        self.phienEdit.setObjectName(u"phienEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.phienEdit.sizePolicy().hasHeightForWidth())
        self.phienEdit.setSizePolicy(sizePolicy1)
        self.phienEdit.setFont(font1)
        self.phienEdit.setStyleSheet(u"align:middle")
        self.phienEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.phienEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.englishphienlevelWidgetLayout.addWidget(self.phienEdit)

        self.levelLineEdit = QLineEdit(self.englishphienlevelWidget)
        self.levelLineEdit.setObjectName(u"levelLineEdit")
        sizePolicy1.setHeightForWidth(self.levelLineEdit.sizePolicy().hasHeightForWidth())
        self.levelLineEdit.setSizePolicy(sizePolicy1)
        self.levelLineEdit.setFont(font1)
        self.levelLineEdit.setAlignment(Qt.AlignCenter)

        self.englishphienlevelWidgetLayout.addWidget(self.levelLineEdit)

        self.englishphienlevelWidgetLayout.setStretch(0, 8)
        self.englishphienlevelWidgetLayout.setStretch(1, 2)
        self.englishphienlevelWidgetLayout.setStretch(2, 1)

        self.infowidgetLayout.addWidget(self.englishphienlevelWidget)

        self.kanjivietnamese = QWidget(self.infowidget)
        self.kanjivietnamese.setObjectName(u"kanjivietnamese")
        sizePolicy1.setHeightForWidth(self.kanjivietnamese.sizePolicy().hasHeightForWidth())
        self.kanjivietnamese.setSizePolicy(sizePolicy1)
        self.kanjivietnameseLayout = QHBoxLayout(self.kanjivietnamese)
        self.kanjivietnameseLayout.setObjectName(u"kanjivietnameseLayout")
        self.kanjivietnameseLayout.setContentsMargins(0, 0, 0, 0)
        self.kanjiEdit = QLineEdit(self.kanjivietnamese)
        self.kanjiEdit.setObjectName(u"kanjiEdit")
        sizePolicy1.setHeightForWidth(self.kanjiEdit.sizePolicy().hasHeightForWidth())
        self.kanjiEdit.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(73)
        self.kanjiEdit.setFont(font2)
        self.kanjiEdit.setAlignment(Qt.AlignCenter)
        self.kanjiEdit.setReadOnly(True)
        self.kanjiEdit.setClearButtonEnabled(False)

        self.kanjivietnameseLayout.addWidget(self.kanjiEdit)

        self.vietnameseBrowser = QPlainTextEdit(self.kanjivietnamese)
        self.vietnameseBrowser.setObjectName(u"vietnameseBrowser")
        self.vietnameseBrowser.setFont(font1)

        self.kanjivietnameseLayout.addWidget(self.vietnameseBrowser)

        self.kanjivietnameseLayout.setStretch(0, 1)
        self.kanjivietnameseLayout.setStretch(1, 1)

        self.infowidgetLayout.addWidget(self.kanjivietnamese)

        self.strokegradeurlswdget = QWidget(self.infowidget)
        self.strokegradeurlswdget.setObjectName(u"strokegradeurlswdget")
        sizePolicy.setHeightForWidth(self.strokegradeurlswdget.sizePolicy().hasHeightForWidth())
        self.strokegradeurlswdget.setSizePolicy(sizePolicy)
        self.strokegradeurlswdgetLayout = QHBoxLayout(self.strokegradeurlswdget)
        self.strokegradeurlswdgetLayout.setObjectName(u"strokegradeurlswdgetLayout")
        self.strokegradeurlswdgetLayout.setContentsMargins(0, 0, 0, 0)
        self.strokegrade = QWidget(self.strokegradeurlswdget)
        self.strokegrade.setObjectName(u"strokegrade")
        self.strokegradeLayout = QVBoxLayout(self.strokegrade)
        self.strokegradeLayout.setObjectName(u"strokegradeLayout")
        self.strokegradeLayout.setContentsMargins(0, 0, 0, 0)
        self.strokeEdit = QPlainTextEdit(self.strokegrade)
        self.strokeEdit.setObjectName(u"strokeEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.strokeEdit.sizePolicy().hasHeightForWidth())
        self.strokeEdit.setSizePolicy(sizePolicy2)
        self.strokeEdit.setMinimumSize(QSize(0, 0))
        self.strokeEdit.setMaximumSize(QSize(16777215, 40))
        self.strokeEdit.setBaseSize(QSize(0, 40))
        self.strokeEdit.setFont(font1)
        self.strokeEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.strokeEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.strokegradeLayout.addWidget(self.strokeEdit)

        self.gradeEdit = QPlainTextEdit(self.strokegrade)
        self.gradeEdit.setObjectName(u"gradeEdit")
        sizePolicy2.setHeightForWidth(self.gradeEdit.sizePolicy().hasHeightForWidth())
        self.gradeEdit.setSizePolicy(sizePolicy2)
        self.gradeEdit.setMinimumSize(QSize(0, 0))
        self.gradeEdit.setMaximumSize(QSize(16777215, 40))
        self.gradeEdit.setBaseSize(QSize(0, 40))
        self.gradeEdit.setFont(font1)
        self.gradeEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gradeEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.strokegradeLayout.addWidget(self.gradeEdit)


        self.strokegradeurlswdgetLayout.addWidget(self.strokegrade)

        self.urlswidget = QWidget(self.strokegradeurlswdget)
        self.urlswidget.setObjectName(u"urlswidget")
        self.urlswidgetLayout = QVBoxLayout(self.urlswidget)
        self.urlswidgetLayout.setObjectName(u"urlswidgetLayout")
        self.urlswidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.jishoUrlEdit = QTextBrowser(self.urlswidget)
        self.jishoUrlEdit.setObjectName(u"jishoUrlEdit")
        sizePolicy2.setHeightForWidth(self.jishoUrlEdit.sizePolicy().hasHeightForWidth())
        self.jishoUrlEdit.setSizePolicy(sizePolicy2)
        self.jishoUrlEdit.setMinimumSize(QSize(0, 0))
        self.jishoUrlEdit.setMaximumSize(QSize(16777215, 40))
        self.jishoUrlEdit.setBaseSize(QSize(0, 40))
        self.jishoUrlEdit.setFont(font1)
        self.jishoUrlEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.jishoUrlEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.jishoUrlEdit.setReadOnly(True)
        self.jishoUrlEdit.setOpenExternalLinks(True)

        self.urlswidgetLayout.addWidget(self.jishoUrlEdit)

        self.maziiUrlEdit = QTextBrowser(self.urlswidget)
        self.maziiUrlEdit.setObjectName(u"maziiUrlEdit")
        sizePolicy2.setHeightForWidth(self.maziiUrlEdit.sizePolicy().hasHeightForWidth())
        self.maziiUrlEdit.setSizePolicy(sizePolicy2)
        self.maziiUrlEdit.setMinimumSize(QSize(0, 0))
        self.maziiUrlEdit.setMaximumSize(QSize(16777215, 40))
        self.maziiUrlEdit.setBaseSize(QSize(0, 40))
        self.maziiUrlEdit.setFont(font1)
        self.maziiUrlEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.maziiUrlEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.maziiUrlEdit.setReadOnly(True)
        self.maziiUrlEdit.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.maziiUrlEdit.setOpenExternalLinks(True)

        self.urlswidgetLayout.addWidget(self.maziiUrlEdit)


        self.strokegradeurlswdgetLayout.addWidget(self.urlswidget)

        self.strokegradeurlswdgetLayout.setStretch(0, 1)
        self.strokegradeurlswdgetLayout.setStretch(1, 1)

        self.infowidgetLayout.addWidget(self.strokegradeurlswdget)

        self.radicalpartonkunwidget = QWidget(self.infowidget)
        self.radicalpartonkunwidget.setObjectName(u"radicalpartonkunwidget")
        sizePolicy1.setHeightForWidth(self.radicalpartonkunwidget.sizePolicy().hasHeightForWidth())
        self.radicalpartonkunwidget.setSizePolicy(sizePolicy1)
        self.radicalpartonkunwidgetLayout = QHBoxLayout(self.radicalpartonkunwidget)
        self.radicalpartonkunwidgetLayout.setObjectName(u"radicalpartonkunwidgetLayout")
        self.radicalpartonkunwidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.radicalpartwidget = QWidget(self.radicalpartonkunwidget)
        self.radicalpartwidget.setObjectName(u"radicalpartwidget")
        self.radicalpartwidgetLayout = QVBoxLayout(self.radicalpartwidget)
        self.radicalpartwidgetLayout.setObjectName(u"radicalpartwidgetLayout")
        self.radicalpartwidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.radicalPlainEdit = QPlainTextEdit(self.radicalpartwidget)
        self.radicalPlainEdit.setObjectName(u"radicalPlainEdit")
        self.radicalPlainEdit.setFont(font1)

        self.radicalpartwidgetLayout.addWidget(self.radicalPlainEdit)

        self.partPlainEdit = QPlainTextEdit(self.radicalpartwidget)
        self.partPlainEdit.setObjectName(u"partPlainEdit")
        self.partPlainEdit.setFont(font1)

        self.radicalpartwidgetLayout.addWidget(self.partPlainEdit)


        self.radicalpartonkunwidgetLayout.addWidget(self.radicalpartwidget)

        self.kunonwidget = QWidget(self.radicalpartonkunwidget)
        self.kunonwidget.setObjectName(u"kunonwidget")
        self.kunonwidgetLayout = QVBoxLayout(self.kunonwidget)
        self.kunonwidgetLayout.setObjectName(u"kunonwidgetLayout")
        self.kunonwidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.kunPlainEdit = QPlainTextEdit(self.kunonwidget)
        self.kunPlainEdit.setObjectName(u"kunPlainEdit")
        font3 = QFont()
        font3.setPointSize(20)
        self.kunPlainEdit.setFont(font3)

        self.kunonwidgetLayout.addWidget(self.kunPlainEdit)

        self.onPlainEdit = QPlainTextEdit(self.kunonwidget)
        self.onPlainEdit.setObjectName(u"onPlainEdit")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.onPlainEdit.setFont(font4)
        self.onPlainEdit.setMouseTracking(False)

        self.kunonwidgetLayout.addWidget(self.onPlainEdit)


        self.radicalpartonkunwidgetLayout.addWidget(self.kunonwidget)


        self.infowidgetLayout.addWidget(self.radicalpartonkunwidget)


        self.mainLayout.addWidget(self.infowidget, 0, 1, 1, 1)

        self.mainLayout.setColumnStretch(0, 1)
        self.mainLayout.setColumnStretch(1, 7)

        self.centralLayout.addWidget(self.mainwidget, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 9)
        self.databaseLocationWidget = QWidget(self.widget_4)
        self.databaseLocationWidget.setObjectName(u"databaseLocationWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.databaseLocationWidget.sizePolicy().hasHeightForWidth())
        self.databaseLocationWidget.setSizePolicy(sizePolicy3)
        self.databaseLocationWidget.setMaximumSize(QSize(16777215, 26))
        self.databaseLocationLayout = QHBoxLayout(self.databaseLocationWidget)
        self.databaseLocationLayout.setObjectName(u"databaseLocationLayout")
        self.databaseLocationLayout.setContentsMargins(0, 0, 0, 0)
        self.databaseLocationButton = QPushButton(self.databaseLocationWidget)
        self.databaseLocationButton.setObjectName(u"databaseLocationButton")
        sizePolicy1.setHeightForWidth(self.databaseLocationButton.sizePolicy().hasHeightForWidth())
        self.databaseLocationButton.setSizePolicy(sizePolicy1)
        self.databaseLocationButton.setIconSize(QSize(100, 16))
        self.databaseLocationButton.setCheckable(False)

        self.databaseLocationLayout.addWidget(self.databaseLocationButton)

        self.databaseLocationAddress = QPlainTextEdit(self.databaseLocationWidget)
        self.databaseLocationAddress.setObjectName(u"databaseLocationAddress")
        font5 = QFont()
        font5.setStyleStrategy(QFont.NoAntialias)
        self.databaseLocationAddress.setFont(font5)
        self.databaseLocationAddress.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.databaseLocationLayout.addWidget(self.databaseLocationAddress)

        self.databaseLocationLayout.setStretch(0, 1)
        self.databaseLocationLayout.setStretch(1, 8)

        self.verticalLayout.addWidget(self.databaseLocationWidget)

        self.wordlocationwidget = QWidget(self.widget_4)
        self.wordlocationwidget.setObjectName(u"wordlocationwidget")
        sizePolicy2.setHeightForWidth(self.wordlocationwidget.sizePolicy().hasHeightForWidth())
        self.wordlocationwidget.setSizePolicy(sizePolicy2)
        self.wordlocationwidget.setMaximumSize(QSize(16777215, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.wordlocationwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.wordlocationwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wordLocationPushButton = QPushButton(self.widget_6)
        self.wordLocationPushButton.setObjectName(u"wordLocationPushButton")
        sizePolicy1.setHeightForWidth(self.wordLocationPushButton.sizePolicy().hasHeightForWidth())
        self.wordLocationPushButton.setSizePolicy(sizePolicy1)
        self.wordLocationPushButton.setIconSize(QSize(100, 16))
        self.wordLocationPushButton.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.wordLocationPushButton)

        self.folderCheckBox = QCheckBox(self.widget_6)
        self.folderCheckBox.setObjectName(u"folderCheckBox")

        self.horizontalLayout_3.addWidget(self.folderCheckBox)


        self.horizontalLayout_6.addWidget(self.widget_6)

        self.wordLocationBoxEdit = QLineEdit(self.wordlocationwidget)
        self.wordLocationBoxEdit.setObjectName(u"wordLocationBoxEdit")
        sizePolicy2.setHeightForWidth(self.wordLocationBoxEdit.sizePolicy().hasHeightForWidth())
        self.wordLocationBoxEdit.setSizePolicy(sizePolicy2)
        self.wordLocationBoxEdit.setMaximumSize(QSize(16777215, 28))
        self.wordLocationBoxEdit.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.wordLocationBoxEdit)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 8)

        self.verticalLayout.addWidget(self.wordlocationwidget)

        self.searchWidget = QWidget(self.widget_4)
        self.searchWidget.setObjectName(u"searchWidget")
        sizePolicy2.setHeightForWidth(self.searchWidget.sizePolicy().hasHeightForWidth())
        self.searchWidget.setSizePolicy(sizePolicy2)
        self.searchWidget.setMaximumSize(QSize(16777215, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.searchWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.searchWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setIconSize(QSize(100, 16))
        self.pushButton.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.searchBoxWidget = QWidget(self.searchWidget)
        self.searchBoxWidget.setObjectName(u"searchBoxWidget")
        self.searchBoxWidgetLayout = QHBoxLayout(self.searchBoxWidget)
        self.searchBoxWidgetLayout.setObjectName(u"searchBoxWidgetLayout")
        self.searchBoxWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.searchBoxWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchBoxEdit = QPlainTextEdit(self.widget)
        self.searchBoxEdit.setObjectName(u"searchBoxEdit")
        self.searchBoxEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.searchBoxEdit)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.searchBoxWidgetLayout.addWidget(self.widget)

        self.navigationButtonWidget = QWidget(self.searchBoxWidget)
        self.navigationButtonWidget.setObjectName(u"navigationButtonWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.navigationButtonWidget.sizePolicy().hasHeightForWidth())
        self.navigationButtonWidget.setSizePolicy(sizePolicy5)
        self.navigationButtonWidget.setMaximumSize(QSize(120, 16777215))
        self.navigationButtonWidget.setBaseSize(QSize(120, 0))
        self.navigationButtonWidgetLayout = QHBoxLayout(self.navigationButtonWidget)
        self.navigationButtonWidgetLayout.setSpacing(0)
        self.navigationButtonWidgetLayout.setObjectName(u"navigationButtonWidgetLayout")
        self.navigationButtonWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.prevButton = QPushButton(self.navigationButtonWidget)
        self.prevButton.setObjectName(u"prevButton")
        sizePolicy1.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
        self.prevButton.setSizePolicy(sizePolicy1)

        self.navigationButtonWidgetLayout.addWidget(self.prevButton)

        self.nextButton = QPushButton(self.navigationButtonWidget)
        self.nextButton.setObjectName(u"nextButton")
        sizePolicy1.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy1)

        self.navigationButtonWidgetLayout.addWidget(self.nextButton)


        self.searchBoxWidgetLayout.addWidget(self.navigationButtonWidget)


        self.horizontalLayout_2.addWidget(self.searchBoxWidget)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.searchWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.centralLayout.addWidget(self.widget_4, 0, 0, 1, 1)

        kanjiIndex.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(kanjiIndex)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRandom = QMenu(self.menuFile)
        self.menuRandom.setObjectName(u"menuRandom")
        self.menuSave = QMenu(self.menubar)
        self.menuSave.setObjectName(u"menuSave")
        kanjiIndex.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.menuRandom.menuAction())
        self.menuFile.addAction(self.actionApply)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionDelete)
        self.menuRandom.addAction(self.actionIn_Selected_File)
        self.menuRandom.addAction(self.actionIn_Selected_Item_s_In_File)
        self.menuRandom.addAction(self.actionIn_Selected_Item_s)
        self.menuRandom.addAction(self.actionIn_Database)
        self.menuSave.addAction(self.actionCurrent_Words_List)
        self.menuSave.addAction(self.actionAll_Words_List)

        self.retranslateUi(kanjiIndex)

        QMetaObject.connectSlotsByName(kanjiIndex)
    # setupUi

    def retranslateUi(self, kanjiIndex):
        self.actionIn_Selected_File.setText(QCoreApplication.translate("kanjiIndex", u"In Selected File", None))
        self.actionIn_Selected_Item_s.setText(
            QCoreApplication.translate("kanjiIndex", u"Select Item(s) in Database", None))
        self.actionApply.setText(QCoreApplication.translate("kanjiIndex", u"Apply", None))
        self.actionResety.setText(QCoreApplication.translate("kanjiIndex", u"Reset", None))
        self.actionReset.setText(QCoreApplication.translate("kanjiIndex", u"Reset", None))
        self.actionDelete.setText(QCoreApplication.translate("kanjiIndex", u"Delete", None))
        self.actionIn_Selected_Item_s_In_File.setText(
            QCoreApplication.translate("kanjiIndex", u"Select Item(s) in File", None))
        self.actionIn_Database.setText(QCoreApplication.translate("kanjiIndex", u"In Database", None))
        self.actionCurrent_List.setText(QCoreApplication.translate("kanjiIndex", u"Current List", None))
        self.actionAll_Word.setText(QCoreApplication.translate("kanjiIndex", u"All Words", None))
        self.actionAll_Words.setText(QCoreApplication.translate("kanjiIndex", u"All Words", None))
        self.actionCurrent_Words_List.setText(QCoreApplication.translate("kanjiIndex", u"Current Words List", None))
        self.actionAll_Words_List.setText(QCoreApplication.translate("kanjiIndex", u"All Words List", None))
        self.englishPlainEdit.setPlainText("")
        self.phienEdit.setHtml(QCoreApplication.translate("kanjiIndex",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                    </p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                     </p>\n"
                                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00c1I                                                                 </p></body></html>",
                                                          None))
        self.levelLineEdit.setText("")
        self.kanjiEdit.setText("")
        self.vietnameseBrowser.setPlainText("")
        self.strokeEdit.setPlainText("")
        self.gradeEdit.setPlainText("")
        self.jishoUrlEdit.setHtml(QCoreApplication.translate("kanjiIndex",
                                                             u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                                </p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                                 </p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://jisho.org/search/%E6%84%9B%20%23kanji                                                                            "
                                                             "                                                                                </p></body></html>",
                                                             None))
        self.maziiUrlEdit.setHtml(QCoreApplication.translate("kanjiIndex",
                                                             u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                                </p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                                 </p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://mazii.net/search/kanji?dict=javi&amp;query=%E6%84%9B&amp;hl=en-US\"><span style=\" text-decoration: und"
                                                             "erline; color:#0000ff;\">https://mazii.net/search/kanji?dict=javi&amp;query=%E6%84%9B&amp;hl=en-US</span></a>                                                                                                                                                            </p></body></html>",
                                                             None))
        self.radicalPlainEdit.setPlainText("")
        self.partPlainEdit.setPlainText("")
        self.kunPlainEdit.setPlainText("")
        self.onPlainEdit.setPlainText("")
        self.databaseLocationButton.setText(QCoreApplication.translate("kanjiIndex", u"Database Location", None))
        self.wordLocationPushButton.setText(QCoreApplication.translate("kanjiIndex", u"Word Location", None))
        self.folderCheckBox.setText(QCoreApplication.translate("kanjiIndex", u"Folder", None))
        self.pushButton.setText(QCoreApplication.translate("kanjiIndex", u"Search", None))
        self.pushButton_2.setText(QCoreApplication.translate("kanjiIndex", u"...", None))
        self.prevButton.setText(QCoreApplication.translate("kanjiIndex", u"Prev", None))
        self.nextButton.setText(QCoreApplication.translate("kanjiIndex", u"Next", None))
        self.menuFile.setTitle(QCoreApplication.translate("kanjiIndex", u"File", None))
        self.menuRandom.setTitle(QCoreApplication.translate("kanjiIndex", u"Random", None))
        self.menuSave.setTitle(QCoreApplication.translate("kanjiIndex", u"Save", None))
        pass
    # retranslateUi

    def customConnect(self):
        self.fillterWord('')
        self.rawText = fileBrowserDialog.FileReader()

        self.wordListWidget.currentItemChanged.connect(self.item_click)
        self.fillterLineEdit.textChanged.connect(partial(self.fillterWord, absolute=False))
        self.wordLocationBoxEdit.textChanged.connect(self.resetWordLocation)

        self.nextButton.clicked.connect(self.nextPos)
        self.pushButton.clicked.connect(self.searchKanji)
        self.prevButton.clicked.connect(self.prevPos)

        self.searchBoxEdit.textChanged.connect(self.searchBoxEditWrapper)
        self.wordLocationPushButton.clicked.connect(self.getDirectoryOrFile)
        self.pushButton_2.clicked.connect(self.translateWindow)

        self.folderCheckBox.setChecked(settings.isFolder)
        self.folderCheckBox.toggled.connect(self.changeIsFolderSetting)

        self.databaseLocationButton.clicked.connect(self.setDatabaseLocation)
        self.databaseLocationAddress.setPlainText(settings.databaseLocation)

        self.actionApply.triggered.connect(self.applyTextChangedToDatabase)
        self.actionReset.triggered.connect(self.resetWord)
        self.actionDelete.triggered.connect(self.deleteIndex)

        self.actionCurrent_Words_List.triggered.connect(self.saveCurrentWordList)
        self.actionAll_Words_List.triggered.connect(self.saveAllWordsList)

        self.actionIn_Selected_File.triggered.connect(self.randomGetFile)
        self.actionIn_Selected_Item_s_In_File.triggered.connect(self.randomGetFileWithSelection)
        self.actionIn_Selected_Item_s.triggered.connect(
            partial(self.inSelectedItemDialog, SQLController.getAllObjects()))
        self.actionIn_Database.triggered.connect(partial(self.randomWordWindow, SQLController.getAllObjects()))


    def applyTextChangedToDatabase(self):
        index = self.wordListWidget.currentIndex().row()
        japanWordObject = JapanWords()
        japanWordObject.kanji = self.kanjiEdit.text()
        japanWordObject.vietnamese = self.vietnameseBrowser.toPlainText()
        japanWordObject.english = self.englishPlainEdit.toPlainText()
        japanWordObject.mean = self.phienEdit.toPlainText()
        japanWordObject.level = self.levelLineEdit.text()
        japanWordObject.strokes = self.strokeEdit.toPlainText()
        japanWordObject.taught = self.gradeEdit.toPlainText()
        japanWordObject.radicals = self.radicalPlainEdit.toPlainText()
        japanWordObject.kun = self.kunPlainEdit.toPlainText()
        japanWordObject.parts = self.partPlainEdit.toPlainText()
        japanWordObject.on = self.onPlainEdit.toPlainText()

        if japanWordObject.kanji != '':
            SQLController.updateDatabase(japanWordObject)
            self.searchBoxEditWrapper()
        self.wordListWidget.setCurrentRow(index)

    def deleteIndex(self):
        index = self.wordListWidget.currentIndex().row()
        SQLController.deleteIndex(self.kanjiEdit.text())
        self.searchBoxEditWrapper()
        self.wordListWidget.setCurrentRow(index)

    def inSelectedItemDialog(self, wordList):
        # reload(InSelectedItemsGUI)
        try:
            self.inSelectedWindow = QDialog()
            self.inSelectedWindow.setAttribute(Qt.WA_DeleteOnClose)
            self.inSelected = InSelectedItemsGUI.Ui_Selector()
            self.inSelected.setupUi(self.inSelectedWindow)
            self.inSelected.wordFromList = wordList
            self.inSelected.customConnect(self)
            self.inSelectedWindow.show()
        except:
            traceback.print_exc()

    def translateWindow(self):
        # reload(translateWindowGUI)
        try:
            del self.translateMainWindow
        except AttributeError:
            print('[INFO] TranslateWindow First Initialized')
        self.translateWindow = QMainWindow()
        self.translateWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.translateMainWindow = translateWindowGUI.Ui_TranslateWindow()
        self.translateMainWindow.setupUi(self.translateWindow)
        self.translateMainWindow.inputTextEdit.insertPlainText(self.searchBoxEdit.toPlainText())
        self.translateMainWindow.customConnect(self)
        self.translateWindow.show()

    def randomWordWindow(self, questionList):
        if len(questionList) == 0 or len(questionList) == 1:
            return
        # reload(randomWordWindow)
        try:
            del self.wordRandom
        except AttributeError:
            print('[INFO] Random Word Window First Initialized')

        try:
            self.wordRandomWindow = QMainWindow()
            self.wordRandomWindow.setAttribute(Qt.WA_DeleteOnClose)
            self.wordRandomWindow.setObjectName("Random Word")
            self.wordRandom = randomWordWindow.Ui_wordRandom()
            self.wordRandom.setupUi(self.wordRandomWindow)
            self.wordRandom.customConnect(questionList, self)
            self.wordRandomWindow.show()
        except Exception:
            traceback.print_exc()

    def resetWordLocation(self):
        if self.wordLocationBoxEdit.text() == '':
            self.rawText.resetText()
            self.fillterWord('')

    def fillterWord(self, words, **kwargs):
        self.wordListWidget.clear()
        wordList = []
        if words != '':
            words = words.split()
        for index in range(len(words)):
            words[index] = wordController.chineseToKanji(words[index])
        # print(f"[INFO] '{words}' is currently in Search")
        # if kwargs.get('notSearch'):
        #     words = words[0]  # Because text in searchKanji is an array of len 1
        #     orgWords = wordController.deleteDuplicate(words, wordController.filteredWords())
        #     words = wordController.splitString(orgWords, 1)
        # words = wordController.chineseToKanji(words)
        if words == '':
            wordList = SQLController.getAllObjects()
        if kwargs.get('searched'):
            words = words[0]  # Because text in searchKanji is an array of len 1
            orgWords = wordController.deleteDuplicate(words, wordController.filteredWords())
            words = wordController.splitString(orgWords, 1)
            # print(orgWords, filteredWords)
            # translateProcess.appendTraslated(filteredWords)
        if len(wordList) == 0:
            for word in words:
                wordList.extend(SQLController.findObjectInDatabase(f'{word}', absoluteSearch=kwargs.get('absolute')))
        wordList = SQLController.removeObjectDuplicate(wordList)
        self.setWordList(wordList)

    def translateKanjiToUI(self, word):
        word = SQLController.databaseToObjects(SQLController.getWord('kanji', f'{word}'))
        self.kanjiEdit.setText(word.kanji)
        self.vietnameseBrowser.setPlainText(word.vietnamese)
        self.englishPlainEdit.setPlainText(word.english)
        self.phienEdit.setText(f'{word.mean}')
        self.levelLineEdit.setText(f'{word.level}')
        self.strokeEdit.setPlainText(f'{word.strokes}')
        self.gradeEdit.setPlainText(f'{word.taught}')
        self.radicalPlainEdit.setPlainText(f'{word.radicals}')
        self.partPlainEdit.setPlainText(f'{word.parts}')
        self.onPlainEdit.setPlainText(f'{word.on}')
        self.kunPlainEdit.setPlainText(f'{word.kun}')
        self.jishoUrlEdit.setText(
            f"<a href=\"https://jisho.org/search/{word.kanji}%20%23kanji\">https://jisho.org/search/{word.kanji}%20%23kanji</a>")
        self.maziiUrlEdit.setText(
            f"<a href=\"https://mazii.net/search/kanji?dict=javi&query={word.kanji}&hl=vi-VN\">https://mazii.net/search/kanji?dict=javi&query={word.kanji}&hl=vi-VN</a>")

    def setWordList(self, wordslist: List, **kwargs):
        self.wordListWidget.addItems(
            [word.kanji for word in wordslist if self.wordListWidget.findItems(word.kanji, Qt.MatchExactly) == []])

    def searchBoxEditWrapper(self):
        if self.searchBoxEdit.toPlainText() != '':
            self.fillterWord(self.searchBoxEdit.toPlainText(), absolute=True)
        else:
            self.fillterWord(self.fillterLineEdit.text(), absolute=False)

    def searchKanji(self):
        # settings.inputPath = self.wordLocationBoxEdit.text()
        # settings.commitToFile()
        try:
            rawText, filteredText = self.deleteDuplicateWithAdd(str(self.rawText), self.searchBoxEdit.toPlainText())
            # print(rawText, filteredText)
        except Exception as ex:
            print(ex)

        if filteredText != '':
            self.appendTraslated(filteredText)

        if rawText != '':
            self.fillterWord(rawText, absolute=True, searched=True)

    def deleteDuplicateWithAdd(self, rawText, addtional=''):
        # rawText = ''.join(wordController.readFile(fileLocation, folder=isFolder))
        # rawText += addtional
        return wordController.deleteDuplicate(rawText + addtional, wordController.filteredWords(), database=True, org=2)

    def appendTraslated(self, text):
        if text != '':
            text = wordController.deleteDuplicate(text, wordController.filteredWords(), database=True)
            print(f'{text=} in AppendTraslated')
            if len(text) >= 3:
                self.initLoadingBar()
            translateProcess.appendTraslated(text)

    def toIndexText(self, text, **kwargs) -> None:
        if len(text) == 0:
            return
        text = wordController.deleteDuplicate(text, wordController.filteredWords())
        if kwargs.get('list') is not None:
            self.fillterWord(kwargs.get('list'), searched=True, absolute=True)
        for i in range(self.wordListWidget.count()):
            # print(self.wordListWidget.item(i))
            if self.wordListWidget.item(i).text() == text:
                self.wordListWidget.setCurrentRow(i)
                return
        else:
            self.setWordList(SQLController.getAllObjects())

    def initLoadingBar(self):
        processBar = Process(target=progressBarUI.runProgressBar)
        processBar.start()

    def resetWord(self):
        if self.kanjiEdit.text() != '':
            index = self.wordListWidget.currentIndex().row()
            self.initLoadingBar()
            translateProcess.appendTraslated(self.kanjiEdit.text(), 1, True)
            self.searchBoxEditWrapper()
            self.wordListWidget.setCurrentRow(index)

    def item_click(self, item):
        try:
            self.translateKanjiToUI(item.text())
            print(f'[INFO] Row currently selected is: {self.wordListWidget.currentIndex().row()}')
        except AttributeError:
            pass
        # print(item.)

    def nextPos(self):
        self.prevRow = self.wordListWidget.currentIndex().row() + 1
        if self.prevRow == self.wordListWidget.count():
            self.prevRow = 0
        self.wordListWidget.setCurrentRow(self.prevRow)

    def prevPos(self):
        self.prevRow = self.wordListWidget.currentIndex().row() - 1
        if self.prevRow == self.wordListWidget.count():
            self.prevRow = 0
        if self.prevRow < 0:
            self.prevRow = self.wordListWidget.count() - 1
        self.wordListWidget.setCurrentRow(self.prevRow)

    def getDirectoryOrFile(self):
        self.rawText.resetText()
        if settings.isFolder:
            self.rawText.getFolderTexts()
            # print(self.rawText)
            # settings.inputPath = QFileDialog.getExistingDirectory()
            # self.wordLocationBoxEdit.setText(f'{settings.inputPath}')
        else:
            self.rawText.getFileTexts()
        self.wordLocationBoxEdit.setText(self.rawText.getFileLocations())
        # print(self.rawText)
        # filePaths = QFileDialog.getOpenFileNames()
        # settings.inputPath = ", ".join(filePaths[0])
        # self.wordLocationBoxEdit.setText(f'{settings.inputPath}')
        # settings.commitToFile()

    def randomGetFile(self):
        inputPath = fileBrowserDialog.FileReader()
        inputPath.getFileTexts()

        rawText, filteredText = self.deleteDuplicateWithAdd(str(inputPath))
        print(f"[INFO] Input: '{rawText}'\n[INFO] Will be searched: {filteredText}")
        self.appendTraslated(filteredText)
        self.randomWordWindow(SQLController.removeObjectDuplicate(SQLController.getWordsObjects(rawText)))

    def randomGetFileWithSelection(self):
        inputPath = fileBrowserDialog.FileReader()
        inputPath.getFileTexts()
        rawText, filteredText = self.deleteDuplicateWithAdd(str(inputPath))
        print(f"[INFO] Input: '{rawText}'\n[INFO] Will be searched: {filteredText}")
        self.appendTraslated(filteredText)
        self.inSelectedItemDialog(SQLController.removeObjectDuplicate(SQLController.getWordsObjects(rawText)))

    def setDatabaseLocation(self):
        databaseLocation = fileBrowserDialog.DatabaseLocation(settings.databaseLocation)
        settings.databaseLocation = str(databaseLocation.databaseLocation)
        settings.commitToFile()
        self.databaseLocationAddress.setPlainText(settings.databaseLocation)

    def changeIsFolderSetting(self, state):
        settings.isFolder = state
        settings.commitToFile()

    def saveCurrentWordList(self) -> None:
        text = ''
        for index in range(self.wordListWidget.count()):
            text += self.wordListWidget.item(index).text()
        self.initSaveDialog(text, 'Current Kanji List')
        # fileBrowserDialog.FileReader()

    def saveAllWordsList(self) -> None:
        all_word_objs = SQLController.getAllObjects()
        text = ''
        for word_obj in all_word_objs:
            text += word_obj.kanji
        self.initSaveDialog(text, 'All Kanji List')

    def initSaveDialog(self, text, heading=None):
        fileBrowserDialog.SaveDialog(text, heading)

    def fileReaderText(self) -> None:
        fileBrowserDialog.FileReader()

if __name__ == "__main__":
    import sys

    freeze_support()
    app = QApplication(sys.argv)
    kanjiBrowserWindow = QMainWindow()
    kanjiBrowserUi = Ui_kanjiIndex()
    kanjiBrowserUi.setupUi(kanjiBrowserWindow)
    kanjiBrowserUi.customConnect()
    kanjiBrowserWindow.show()
    sys.exit(app.exec())