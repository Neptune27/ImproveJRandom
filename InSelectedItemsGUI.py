from functools import partial

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Selector(object):
    def setupUi(self, Selector):
        if not Selector.objectName():
            Selector.setObjectName(u"Selector")
        Selector.resize(496, 426)
        self.horizontalLayout = QHBoxLayout(Selector)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fromWidget = QWidget(Selector)
        self.fromWidget.setObjectName(u"fromWidget")
        self.verticalLayout = QVBoxLayout(self.fromWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fillterFromLineEdit = QLineEdit(self.fromWidget)
        self.fillterFromLineEdit.setObjectName(u"fillterFromLineEdit")

        self.verticalLayout.addWidget(self.fillterFromLineEdit)

        self.wordFromListWidget = QListWidget(self.fromWidget)
        self.wordFromListWidget.setObjectName(u"wordFromListWidget")
        font = QFont()
        font.setPointSize(14)
        self.wordFromListWidget.setFont(font)
        self.wordFromListWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.wordFromListWidget.setSelectionRectVisible(False)
        self.wordFromListWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.wordFromListWidget)

        self.horizontalLayout.addWidget(self.fromWidget)

        self.selectionWidget = QWidget(Selector)
        self.selectionWidget.setObjectName(u"selectionWidget")
        self.verticalLayout_3 = QVBoxLayout(self.selectionWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toFromWidget = QWidget(self.selectionWidget)
        self.toFromWidget.setObjectName(u"toFromWidget")
        self.verticalLayout_4 = QVBoxLayout(self.toFromWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.fromToToButton = QPushButton(self.toFromWidget)
        self.fromToToButton.setObjectName(u"fromToToButton")

        self.verticalLayout_4.addWidget(self.fromToToButton)

        self.toToFromButton = QPushButton(self.toFromWidget)
        self.toToFromButton.setObjectName(u"toToFromButton")
        self.toToFromButton.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.toToFromButton)

        self.verticalLayout_3.addWidget(self.toFromWidget)

        self.AcceptWidget = QWidget(self.selectionWidget)
        self.AcceptWidget.setObjectName(u"AcceptWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AcceptWidget.sizePolicy().hasHeightForWidth())
        self.AcceptWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.AcceptWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.acceptButton = QPushButton(self.AcceptWidget)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.acceptButton)

        self.quitButton = QPushButton(self.AcceptWidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.quitButton)

        self.verticalLayout_3.addWidget(self.AcceptWidget)

        self.horizontalLayout.addWidget(self.selectionWidget)

        self.toWidget = QWidget(Selector)
        self.toWidget.setObjectName(u"toWidget")
        self.verticalLayout_2 = QVBoxLayout(self.toWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fillterToLineEdit = QLineEdit(self.toWidget)
        self.fillterToLineEdit.setObjectName(u"fillterToLineEdit")

        self.verticalLayout_2.addWidget(self.fillterToLineEdit)

        self.wordToListWidget = QListWidget(self.toWidget)
        self.wordToListWidget.setObjectName(u"wordToListWidget")
        self.wordToListWidget.setFont(font)
        self.wordToListWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.wordToListWidget.setSelectionRectVisible(False)
        self.wordToListWidget.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.wordToListWidget)

        self.horizontalLayout.addWidget(self.toWidget)

        self.retranslateUi(Selector)

        QMetaObject.connectSlotsByName(Selector)

        self.wordFromListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.wordToListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.windowObject = Selector

        self.wordFromList = []

    # setupUi

    def retranslateUi(self, Selector):
        Selector.setWindowTitle(QCoreApplication.translate("Selector", u"Selector", None))
        self.fromToToButton.setText(QCoreApplication.translate("Selector", u">>", None))
        self.toToFromButton.setText(QCoreApplication.translate("Selector", u"<<", None))
        self.acceptButton.setText(QCoreApplication.translate("Selector", u"Accept", None))
        self.quitButton.setText(QCoreApplication.translate("Selector", u"Quit", None))

    # retranslateUi

    def customConnect(self, mainWindow):
        self.mainWindow = mainWindow
        self.wordFromList = self.sortedListByKanji(self.wordFromList)
        self.wordToList = []

        self.setListWidget(self.wordFromListWidget, self.wordFromList)
        self.setListWidget(self.wordToListWidget, self.wordToList)
        self.fromToToButton.clicked.connect(
            partial(self.moveObject, self.wordFromListWidget, 0))
        self.toToFromButton.clicked.connect(
            partial(self.moveObject, self.wordToListWidget, 1))

        self.wordFromListWidget.doubleClicked.connect(
            partial(self.doubleClickedWrapper, self.wordFromListWidget, 0))
        self.wordToListWidget.doubleClicked.connect(
            partial(self.doubleClickedWrapper, self.wordToListWidget, 1))

        self.acceptButton.clicked.connect(self.acceptClicked)
        self.quitButton.clicked.connect(self.windowObject.close)

        self.fillterFromLineEdit.textChanged.connect(partial(self.searchFilter, self.wordFromListWidget))
        self.fillterToLineEdit.textChanged.connect(partial(self.searchFilter, self.wordToListWidget))

    def setListWidget(self, whichListWidget: QListWidget, whichList):
        whichListWidget.clear()
        whichList = self.sortedListByKanji(whichList)
        whichListWidget.addItems([item.kanji for item in whichList])

    def doubleClickedWrapper(self, which: QListWidget, type, *args) -> None:
        """*args is a throwaway argument for double clicked signals"""
        print(f'[INFO] DoubleClicked {which}')
        self.moveObject(which, type)

    def moveObject(self, fromWhereWidget: QListWidget, *args) -> None:
        if len(fromWhereWidget.selectedIndexes()) == 0:
            return
        offset = 0
        for index in fromWhereWidget.selectedIndexes():
            if args[0] == 0:
                self.wordToList.append(self.wordFromList[index.row() - offset])
                self.wordFromList.pop(index.row() - offset)
            elif args[0] == 1:
                self.wordFromList.append(self.wordToList[index.row() - offset])
                self.wordToList.pop(index.row() - offset)
            offset += 1
        self.wordFromList = self.sortedListByKanji(self.wordFromList)
        self.wordToList = self.sortedListByKanji(self.wordToList)

        self.setListWidget(self.wordFromListWidget, self.wordFromList)
        self.setListWidget(self.wordToListWidget, self.wordToList)

    def acceptClicked(self):
        self.windowObject.accept()
        self.mainWindow.randomWordWindow(self.wordToList)

    def sortedListByKanji(self, wordList):
        return sorted(wordList, key=lambda x: x.kanji)

    def searchFilter(self, whichListWidget: QListWidget, whichLineEditText: QLineEdit):
        if whichLineEditText != '':
            for i in range(whichListWidget.count()):
                if whichLineEditText in whichListWidget.item(i).text():
                    whichListWidget.item(i).setHidden(False)
                else:
                    whichListWidget.item(i).setHidden(True)
        else:
            for i in range(whichListWidget.count()):
                whichListWidget.item(i).setHidden(False)
