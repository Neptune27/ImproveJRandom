# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressBar.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import json
from functools import partial

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import multiprocessing


class Ui_ProcessBarDialog(object):
    def setupUi(self, ProcessBarDialog):
        if not ProcessBarDialog.objectName():
            ProcessBarDialog.setObjectName(u"ProcessBarDialog")
        ProcessBarDialog.resize(500, 118)
        ProcessBarDialog.show()
        self.objDialog = ProcessBarDialog
        self.objDialog.setWindowTitle("Finding Words, please wait")
        self.verticalLayout = QVBoxLayout(ProcessBarDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maziiProcessWidget = QWidget(ProcessBarDialog)
        self.maziiProcessWidget.setObjectName(u"maziiProcessWidget")
        self.horizontalLayout = QHBoxLayout(self.maziiProcessWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.maziiProgressBar = QProgressBar(self.maziiProcessWidget)
        self.maziiProgressBar.setObjectName(u"maziiProgressBar")
        self.maziiProgressBar.setValue(0)
        self.maziiProgressBar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.maziiProgressBar)

        self.maziiLabel = QLabel(self.maziiProcessWidget)
        self.maziiLabel.setObjectName(u"maziiLabel")
        self.maziiLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.maziiLabel)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.maziiProcessWidget)

        self.jishoProgressWidget = QWidget(ProcessBarDialog)
        self.jishoProgressWidget.setObjectName(u"jishoProgressWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.jishoProgressWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.jishoProgressBar = QProgressBar(self.jishoProgressWidget)
        self.jishoProgressBar.setObjectName(u"jishoProgressBar")
        self.jishoProgressBar.setValue(0)
        self.jishoProgressBar.setTextVisible(False)

        self.horizontalLayout_2.addWidget(self.jishoProgressBar)

        self.jishoLabel = QLabel(self.jishoProgressWidget)
        self.jishoLabel.setObjectName(u"jishoLabel")
        # self.setProgressFile()
        self.horizontalLayout_2.addWidget(self.jishoLabel)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.jishoProgressWidget)

        self.retranslateUi(ProcessBarDialog)
        self.timer = QTimer()
        self.timer.timeout.connect(partial(self.closeWhenFinished, ProcessBarDialog))
        self.timer.setInterval(100)
        self.timer.start()
        QMetaObject.connectSlotsByName(ProcessBarDialog)
        # self.closeWhenFinished(ProcessBarDialog)

    # setupUi


    def retranslateUi(self, ProcessBarDialog):
        ProcessBarDialog.setWindowTitle(QCoreApplication.translate("ProcessBarDialog", u"Dialog", None))
        self.maziiProgressBar.setFormat("")
        self.maziiLabel.setText(QCoreApplication.translate("ProcessBarDialog", u"Mazii %p of %t", None))
        self.jishoProgressBar.setFormat("")
        self.jishoLabel.setText(QCoreApplication.translate("ProcessBarDialog", u"Jisho %p of %t", None))

    def closeWhenFinished(self, ProcessBarDialog):
        with open('./Data/counter.json', 'r', encoding='UTF-8') as counter:
            var = json.loads(counter.read())
            # print('nvn')
            self.maziiProgressBar.setMaximum(int(var['maziiTotal']))
            self.jishoProgressBar.setMaximum(int(var['jishoTotal']))
            self.maziiProgressBar.setValue(var['maziiCounter'])
            self.jishoProgressBar.setValue(var['jishoCounter'])
            self.maziiLabel.setText(f"Mazii {var['maziiCounter']} of {var['maziiTotal']}")
            self.jishoLabel.setText(f"Jisho {var['jishoCounter']} of {var['jishoTotal']}")
            if var['maziiCounter'] == var['maziiTotal'] and var['jishoCounter'] == var['jishoTotal']:
                self.timer.stop()
                ProcessBarDialog.accept()

    # retranslateUi


def runProgressBar():
    import sys

    app = QApplication(sys.argv)
    processBar = QDialog()
    processBar.setAttribute(Qt.WA_QuitOnClose)
    processBarUI = Ui_ProcessBarDialog()
    processBarUI.setupUi(processBar)
    processBarUI.retranslateUi(processBar)
    sys.exit(app.exec())


if __name__ == '__main__':
    multiprocessing.freeze_support()
    runProgressBar()
