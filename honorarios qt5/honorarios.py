# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'honorarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(832, 674)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 130, 531, 391))
        self.label.setStyleSheet("background-color: rgba(0,0,0,195);\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.SalarioMin = QtWidgets.QLineEdit(Form)
        self.SalarioMin.setGeometry(QtCore.QRect(150, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.SalarioMin.setFont(font)
        self.SalarioMin.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgba(255,255,255,200);\n"
"color: rgba(255,255,255, 200);\n"
"paddling-bottom: 7px;\n"
"")
        self.SalarioMin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SalarioMin.setObjectName("SalarioMin")
        self.Condenacao = QtWidgets.QLineEdit(Form)
        self.Condenacao.setGeometry(QtCore.QRect(150, 360, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Condenacao.setFont(font)
        self.Condenacao.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgba(255,255,255,200);\n"
"color: rgba(255,255,255, 200);\n"
"paddling-bottom: 7px;\n"
"")
        self.Condenacao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Condenacao.setObjectName("Condenacao")
        self.MinResult = QtWidgets.QLineEdit(Form)
        self.MinResult.setGeometry(QtCore.QRect(440, 290, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.MinResult.setFont(font)
        self.MinResult.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgba(255,255,255,200);\n"
"color: rgba(255,255,255, 200);\n"
"paddling-bottom: 7px;\n"
"")
        self.MinResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MinResult.setReadOnly(True)
        self.MinResult.setObjectName("MinResult")
        self.MaxResult = QtWidgets.QLineEdit(Form)
        self.MaxResult.setGeometry(QtCore.QRect(440, 360, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.MaxResult.setFont(font)
        self.MaxResult.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgba(255,255,255,200);\n"
"color: rgba(255,255,255, 200);\n"
"paddling-bottom: 7px;\n"
"")
        self.MaxResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MaxResult.setReadOnly(True)
        self.MaxResult.setObjectName("MaxResult")
        self.CalcButton = QtWidgets.QPushButton(Form)
        self.CalcButton.setGeometry(QtCore.QRect(170, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CalcButton.setFont(font)
        self.CalcButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalcButton.setStyleSheet("QPushButton#CalcButton{\n"
"border-style:outset;\n"
"border-radius: 15px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"color: rgba(255,255,255,200);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  #232526, stop:1#414345);\n"
"}\n"
"QPushButton#CalcButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 #414345, stop:1 #232526);\n"
"}\n"
"QPushButton#CalcButton:pressed{\n"
"paddling-left: 5px;\n"
"paddling-top: 5px;\n"
"background-color: rgba(248, 248, 255, 100);\n"
"}\n"
"")
        self.CalcButton.setObjectName("CalcButton")
        self.CleanButton = QtWidgets.QPushButton(Form)
        self.CleanButton.setGeometry(QtCore.QRect(470, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CleanButton.setFont(font)
        self.CleanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CleanButton.setStyleSheet("QPushButton#CleanButton{\n"
"border-style:outset;\n"
"border-radius: 15px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"color: rgba(255,255,255,200);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  #232526, stop:1#414345);\n"
"}\n"
"QPushButton#CleanButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 #414345, stop:1 #232526);\n"
"}\n"
"QPushButton#CleanButton:pressed{\n"
"paddling-left: 5px;\n"
"paddling-top: 5px;\n"
"background-color: rgba(248, 248, 255, 100);\n"
"}\n"
"")
        self.CleanButton.setObjectName("CleanButton")
        self.Titulo = QtWidgets.QLabel(Form)
        self.Titulo.setGeometry(QtCore.QRect(170, 140, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("color: rgba(255,255,255, 220)")
        self.Titulo.setObjectName("Titulo")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(400, 280, 2, 231))
        self.line.setStyleSheet("background-color: rgba(255,255,255,100);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setGeometry(QtCore.QRect(610, 130, 41, 28))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(10)
        self.CloseButton.setFont(font)
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("QPushButton#CloseButton{\n"
"color: rgba(255, 255, 255, 180);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"background-style: outset;\n"
"}\n"
"QPushButton#CloseButton:hover{\n"
"color: rgba(255,255,255,255);\n"
"}\n"
"QPushButton#CloseButton:pressed{\n"
"paddling-left: 5px;\n"
"paddling-top: 5px;\n"
"color: rgba(220, 20, 60, 230);\n"
"}")
        self.CloseButton.setObjectName("CloseButton")
        self.Obs = QtWidgets.QLabel(Form)
        self.Obs.setGeometry(QtCore.QRect(290, 240, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Obs.setFont(font)
        self.Obs.setStyleSheet("color: rgba(255,255,255,180);")
        self.Obs.setObjectName("Obs")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SalarioMin.setPlaceholderText(_translate("Form", "Salário Mínimo:"))
        self.Condenacao.setPlaceholderText(_translate("Form", "Valor da Condenação:"))
        self.MinResult.setPlaceholderText(_translate("Form", "Mín:"))
        self.MaxResult.setPlaceholderText(_translate("Form", "Máx:"))
        self.CalcButton.setText(_translate("Form", "Calcular"))
        self.CleanButton.setText(_translate("Form", "Limpar"))
        self.Titulo.setText(_translate("Form", "Fixação de Honorários"))
        self.CloseButton.setText(_translate("Form", "X"))
        self.Obs.setText(_translate("Form", "- Formato do salário: ####.##"))
