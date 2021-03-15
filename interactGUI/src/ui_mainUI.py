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
        guiDlg.resize(554, 481)
        self.respuesta = QPlainTextEdit(guiDlg)
        self.respuesta.setObjectName(u"respuesta")
        self.respuesta.setGeometry(QRect(20, 320, 331, 71))
        self.botonalegria = QPushButton(guiDlg)
        self.botonalegria.setObjectName(u"botonalegria")
        self.botonalegria.setGeometry(QRect(370, 320, 80, 31))
        self.botonmiedo = QPushButton(guiDlg)
        self.botonmiedo.setObjectName(u"botonmiedo")
        self.botonmiedo.setGeometry(QRect(370, 280, 80, 31))
        self.botontristeza = QPushButton(guiDlg)
        self.botontristeza.setObjectName(u"botontristeza")
        self.botontristeza.setGeometry(QRect(370, 240, 81, 31))
        self.botonsorpresa = QPushButton(guiDlg)
        self.botonsorpresa.setObjectName(u"botonsorpresa")
        self.botonsorpresa.setGeometry(QRect(370, 360, 80, 31))
        self.textoaenviar = QLineEdit(guiDlg)
        self.textoaenviar.setObjectName(u"textoaenviar")
        self.textoaenviar.setGeometry(QRect(20, 100, 331, 71))
        self.nombreaintroducir = QLineEdit(guiDlg)
        self.nombreaintroducir.setObjectName(u"nombreaintroducir")
        self.nombreaintroducir.setGeometry(QRect(371, 100, 171, 21))
        self.label = QLabel(guiDlg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 80, 131, 16))
        self.textoescuchado = QLineEdit(guiDlg)
        self.textoescuchado.setObjectName(u"textoescuchado")
        self.textoescuchado.setGeometry(QRect(20, 200, 331, 71))
        self.label_2 = QLabel(guiDlg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 80, 111, 16))
        self.label_2.setMaximumSize(QSize(121, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_3 = QLabel(guiDlg)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 170, 141, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(guiDlg)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 290, 121, 31))
        self.label_4.setFont(font)
        self.exportarpdf = QPushButton(guiDlg)
        self.exportarpdf.setObjectName(u"exportarpdf")
        self.exportarpdf.setGeometry(QRect(390, 180, 131, 21))
        self.asignarnombre = QPushButton(guiDlg)
        self.asignarnombre.setObjectName(u"asignarnombre")
        self.asignarnombre.setGeometry(QRect(370, 130, 171, 31))
        self.limpiarconversacion = QPushButton(guiDlg)
        self.limpiarconversacion.setObjectName(u"limpiarconversacion")
        self.limpiarconversacion.setGeometry(QRect(380, 210, 151, 21))
        self.muestramensajes = QPlainTextEdit(guiDlg)
        self.muestramensajes.setObjectName(u"muestramensajes")
        self.muestramensajes.setGeometry(QRect(20, 30, 511, 31))
        self.label_5 = QLabel(guiDlg)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 10, 81, 16))
        self.label_5.setFont(font)
        self.botonneutral = QPushButton(guiDlg)
        self.botonneutral.setObjectName(u"botonneutral")
        self.botonneutral.setGeometry(QRect(460, 260, 81, 31))
        self.botonenfadado = QPushButton(guiDlg)
        self.botonenfadado.setObjectName(u"botonenfadado")
        self.botonenfadado.setGeometry(QRect(460, 340, 80, 31))
        self.botondisgustado = QPushButton(guiDlg)
        self.botondisgustado.setObjectName(u"botondisgustado")
        self.botondisgustado.setGeometry(QRect(460, 300, 80, 31))
        self.grabar = QCheckBox(guiDlg)
        self.grabar.setObjectName(u"grabar")
        self.grabar.setGeometry(QRect(230, 290, 85, 21))
        self.si = QPushButton(guiDlg)
        self.si.setObjectName(u"si")
        self.si.setGeometry(QRect(370, 400, 80, 41))
        self.no = QPushButton(guiDlg)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(460, 400, 80, 41))

        self.retranslateUi(guiDlg)

        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"interactGUI", None))
        self.botonalegria.setText(QCoreApplication.translate("guiDlg", u"Alegr\u00eda", None))
        self.botonmiedo.setText(QCoreApplication.translate("guiDlg", u"Miedo", None))
        self.botontristeza.setText(QCoreApplication.translate("guiDlg", u"Tristeza", None))
        self.botonsorpresa.setText(QCoreApplication.translate("guiDlg", u"Sorpresa", None))
        self.label.setText(QCoreApplication.translate("guiDlg", u"Nombre del usuario", None))
        self.label_2.setText(QCoreApplication.translate("guiDlg", u"Texto a decir", None))
        self.label_3.setText(QCoreApplication.translate("guiDlg", u"Texto escuchado", None))
        self.label_4.setText(QCoreApplication.translate("guiDlg", u"Texto grabado", None))
        self.exportarpdf.setText(QCoreApplication.translate("guiDlg", u"Exportar a PDF", None))
        self.asignarnombre.setText(QCoreApplication.translate("guiDlg", u"Asignar nombre", None))
        self.limpiarconversacion.setText(QCoreApplication.translate("guiDlg", u"Limpiar conversaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("guiDlg", u"Mensajes", None))
        self.botonneutral.setText(QCoreApplication.translate("guiDlg", u"Neutral", None))
        self.botonenfadado.setText(QCoreApplication.translate("guiDlg", u"Enfadado", None))
        self.botondisgustado.setText(QCoreApplication.translate("guiDlg", u"Disgustado", None))
        self.grabar.setText(QCoreApplication.translate("guiDlg", u"Grabar", None))
        self.si.setText(QCoreApplication.translate("guiDlg", u"Si", None))
        self.no.setText(QCoreApplication.translate("guiDlg", u"No", None))
    # retranslateUi

