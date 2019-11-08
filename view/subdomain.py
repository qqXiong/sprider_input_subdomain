# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subdomain.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 624)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 170, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.host = QtWidgets.QLineEdit(Form)
        self.host.setGeometry(QtCore.QRect(80, 20, 201, 31))
        self.host.setObjectName("host")
        self.result = QtWidgets.QTextEdit(Form)
        self.result.setGeometry(QtCore.QRect(20, 210, 541, 391))
        self.result.setObjectName("result")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(80, 70, 201, 31))
        self.user.setObjectName("user")
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setGeometry(QtCore.QRect(360, 20, 201, 31))
        self.port.setObjectName("port")
        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(360, 70, 201, 31))
        self.passwd.setObjectName("passwd")
        self.db = QtWidgets.QLineEdit(Form)
        self.db.setGeometry(QtCore.QRect(80, 120, 201, 31))
        self.db.setObjectName("db")
        self.charset = QtWidgets.QLineEdit(Form)
        self.charset.setGeometry(QtCore.QRect(360, 120, 201, 31))
        self.charset.setObjectName("charset")
        self.domain = QtWidgets.QLineEdit(Form)
        self.domain.setGeometry(QtCore.QRect(80, 170, 201, 31))
        self.domain.setObjectName("domain")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 80, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(300, 130, 58, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 58, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "开始"))
        self.label.setText(_translate("Form", "host"))
        self.label_2.setText(_translate("Form", "port"))
        self.label_3.setText(_translate("Form", "user"))
        self.label_4.setText(_translate("Form", "passwd"))
        self.label_5.setText(_translate("Form", "db"))
        self.label_6.setText(_translate("Form", "charset"))
        self.label_7.setText(_translate("Form", "domain"))
