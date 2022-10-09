# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewQt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1118, 770)
        self.cargarPushButton = QPushButton(Form)
        self.cargarPushButton.setObjectName(u"cargarPushButton")
        self.cargarPushButton.setGeometry(QRect(480, 20, 111, 41))
        self.UrlLineEdit = QLineEdit(Form)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")
        self.UrlLineEdit.setGeometry(QRect(150, 30, 311, 20))
        self.TxtPlainTextEdit = QPlainTextEdit(Form)
        self.TxtPlainTextEdit.setObjectName(u"TxtPlainTextEdit")
        self.TxtPlainTextEdit.setGeometry(QRect(150, 100, 821, 401))
        font = QFont()
        font.setPointSize(16)
        self.TxtPlainTextEdit.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 510, 211, 31))
        self.LexplainTextEdit = QPlainTextEdit(Form)
        self.LexplainTextEdit.setObjectName(u"LexplainTextEdit")
        self.LexplainTextEdit.setGeometry(QRect(70, 550, 281, 211))
        font1 = QFont()
        font1.setPointSize(12)
        self.LexplainTextEdit.setFont(font1)
        self.semanticoTextEdit = QTextEdit(Form)
        self.semanticoTextEdit.setObjectName(u"semanticoTextEdit")
        self.semanticoTextEdit.setGeometry(QRect(520, 560, 281, 201))
        self.semanticoTextEdit.setFont(font1)
        self.pushButtonSemantico = QPushButton(Form)
        self.pushButtonSemantico.setObjectName(u"pushButtonSemantico")
        self.pushButtonSemantico.setGeometry(QRect(550, 520, 211, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cargarPushButton.setText(QCoreApplication.translate("Form", u"CARGAR ARCHIVO", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Lexico", None))
        self.pushButtonSemantico.setText(QCoreApplication.translate("Form", u"Semantico", None))
    # retranslateUi

