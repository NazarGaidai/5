# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setingsOW_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow_1(object):
    def setupUi(self, OtherWindow_1):
        OtherWindow_1.setObjectName("OtherWindow_1")
        OtherWindow_1.resize(431, 336)
        OtherWindow_1.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label = QtWidgets.QLabel(OtherWindow_1)
        self.label.setGeometry(QtCore.QRect(30, 20, 381, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(OtherWindow_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 381, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(OtherWindow_1)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 261, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(OtherWindow_1)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow_1)

    def retranslateUi(self, OtherWindow_1):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow_1.setWindowTitle(_translate("OtherWindow_1", "Довідник ринків"))
        self.label.setText(_translate("OtherWindow_1", "                                              Довідник ринків"))
        self.label_6.setText(_translate("OtherWindow_1", "200"))
        self.label_7.setText(_translate("OtherWindow_1", "300"))
        self.label_2.setText(_translate("OtherWindow_1", "Код ринку"))
        self.label_3.setText(_translate("OtherWindow_1", "Найменування товару"))
        self.label_12.setText(_translate("OtherWindow_1", "Житній"))
        self.label_11.setText(_translate("OtherWindow_1", "Бесарабський"))
        self.label_5.setText(_translate("OtherWindow_1", "100"))
        self.label_13.setText(_translate("OtherWindow_1", "Володимирський"))
        self.label_4.setText(_translate("OtherWindow_1", "Роботу виконав:Гайдай Назар (1-7 ФІТ)"))




