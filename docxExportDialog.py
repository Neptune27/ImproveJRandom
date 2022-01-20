from functools import partial

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DocxSelector(object):
    def setupUi(self, DocxSelector):
        if not DocxSelector.objectName():
            DocxSelector.setObjectName(u"DocxSelector")
        DocxSelector.resize(401, 176)
        self.verticalLayout = QVBoxLayout(DocxSelector)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(DocxSelector)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.kanjiBox = QCheckBox(self.widget_2)
        self.kanjiBox.setObjectName(u"kanjiBox")
        self.kanjiBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.kanjiBox)

        self.vietnameseBox = QCheckBox(self.widget_2)
        self.vietnameseBox.setObjectName(u"vietnameseBox")

        self.verticalLayout_2.addWidget(self.vietnameseBox)

        self.strokesBox = QCheckBox(self.widget_2)
        self.strokesBox.setObjectName(u"strokesBox")

        self.verticalLayout_2.addWidget(self.strokesBox)

        self.levelBox = QCheckBox(self.widget_2)
        self.levelBox.setObjectName(u"levelBox")

        self.verticalLayout_2.addWidget(self.levelBox)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, 0, 0)
        self.meansBox = QCheckBox(self.widget_4)
        self.meansBox.setObjectName(u"meansBox")
        self.meansBox.setChecked(True)

        self.verticalLayout_3.addWidget(self.meansBox)

        self.OnBox = QCheckBox(self.widget_4)
        self.OnBox.setObjectName(u"OnBox")

        self.verticalLayout_3.addWidget(self.OnBox)

        self.radicalsBox = QCheckBox(self.widget_4)
        self.radicalsBox.setObjectName(u"radicalsBox")

        self.verticalLayout_3.addWidget(self.radicalsBox)

        self.taughtBox = QCheckBox(self.widget_4)
        self.taughtBox.setObjectName(u"taughtBox")

        self.verticalLayout_3.addWidget(self.taughtBox)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 0, 0, 0)
        self.englishBox = QCheckBox(self.widget_3)
        self.englishBox.setObjectName(u"englishBox")
        self.englishBox.setChecked(True)

        self.verticalLayout_4.addWidget(self.englishBox)

        self.kunBox = QCheckBox(self.widget_3)
        self.kunBox.setObjectName(u"kunBox")

        self.verticalLayout_4.addWidget(self.kunBox)

        self.partsBox = QCheckBox(self.widget_3)
        self.partsBox.setObjectName(u"partsBox")

        self.verticalLayout_4.addWidget(self.partsBox)

        self.colorizeBox = QCheckBox(self.widget_3)
        self.colorizeBox.setObjectName(u"colorizeBox")

        self.verticalLayout_4.addWidget(self.colorizeBox)

        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(DocxSelector)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DocxSelector)
        self.buttonBox.accepted.connect(DocxSelector.accept)
        self.buttonBox.rejected.connect(DocxSelector.reject)

        QMetaObject.connectSlotsByName(DocxSelector)

        self.isAccepted = True
        self.DocxSelectorWindow = DocxSelector
        self.DocxSelectorWindow.reject = partial(self.cancel, self.DocxSelectorWindow.reject)
    # setupUi

    def retranslateUi(self, DocxSelector):
        DocxSelector.setWindowTitle(QCoreApplication.translate("DocxSelector", u"Docx Export Options", None))
        self.kanjiBox.setText(QCoreApplication.translate("DocxSelector", u"Kanji", None))
        self.vietnameseBox.setText(QCoreApplication.translate("DocxSelector", u"Vietnamese Meaning", None))
        self.strokesBox.setText(QCoreApplication.translate("DocxSelector", u"Strokes", None))
        self.levelBox.setText(QCoreApplication.translate("DocxSelector", u"Level", None))
        self.meansBox.setText(QCoreApplication.translate("DocxSelector", u"Means", None))
        self.OnBox.setText(QCoreApplication.translate("DocxSelector", u"On Reading", None))
        self.radicalsBox.setText(QCoreApplication.translate("DocxSelector", u"Radicals", None))
        self.taughtBox.setText(QCoreApplication.translate("DocxSelector", u"Taught In", None))
        self.englishBox.setText(QCoreApplication.translate("DocxSelector", u"English Meanings", None))
        self.kunBox.setText(QCoreApplication.translate("DocxSelector", u"Kun Reading", None))
        self.partsBox.setText(QCoreApplication.translate("DocxSelector", u"Parts", None))
        self.colorizeBox.setText(QCoreApplication.translate("DocxSelector", u"Colorize", None))
    # retranslateUi

    def cancel(self, func):
        self.isAccepted = False
        func()
