# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if not guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(400, 70)
        self.textoaenviar = QTextEdit(guiDlg)
        self.textoaenviar.setObjectName(u"textoaenviar")
        self.textoaenviar.setGeometry(QRect(10, 20, 251, 31))
        self.enviotexto = QPushButton(guiDlg)
        self.enviotexto.setObjectName(u"enviotexto")
        self.enviotexto.setGeometry(QRect(270, 20, 121, 31))

        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"speech", None))
        self.enviotexto.setText(QCoreApplication.translate("guiDlg", u"Enviar texto", None))
    # retranslateUi

