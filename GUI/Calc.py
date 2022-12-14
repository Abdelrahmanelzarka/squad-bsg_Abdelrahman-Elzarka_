# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 550)
        self.OutputLabel = QtWidgets.QLabel(Dialog)
        self.OutputLabel.setGeometry(QtCore.QRect(20, 30, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLabel.setLineWidth(2)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        self.PercentButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("%"))
        self.PercentButton.setGeometry(QtCore.QRect(20, 140, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PercentButton.setFont(font)
        self.PercentButton.setObjectName("PercentButton")
        self.CButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("C"))
        self.CButton.setGeometry(QtCore.QRect(130, 140, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.CButton.setFont(font)
        self.CButton.setObjectName("CButton")
        self.ShiftButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.remove_it())
        self.ShiftButton.setGeometry(QtCore.QRect(240, 140, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ShiftButton.setFont(font)
        self.ShiftButton.setObjectName("ShiftButton")
        self.DivisionButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("/"))
        self.DivisionButton.setGeometry(QtCore.QRect(350, 140, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.DivisionButton.setFont(font)
        self.DivisionButton.setObjectName("DivisionButton")
        self.EightButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("8"))
        self.EightButton.setGeometry(QtCore.QRect(130, 220, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.EightButton.setFont(font)
        self.EightButton.setObjectName("EightButton")
        self.TimesButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("x"))
        self.TimesButton.setGeometry(QtCore.QRect(350, 220, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.TimesButton.setFont(font)
        self.TimesButton.setObjectName("TimesButton")
        self.SevenButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("7"))
        self.SevenButton.setGeometry(QtCore.QRect(20, 220, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.SevenButton.setFont(font)
        self.SevenButton.setObjectName("SevenButton")
        self.NineButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("9"))
        self.NineButton.setGeometry(QtCore.QRect(240, 220, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.NineButton.setFont(font)
        self.NineButton.setObjectName("NineButton")
        self.FiveButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("5"))
        self.FiveButton.setGeometry(QtCore.QRect(130, 300, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.FiveButton.setFont(font)
        self.FiveButton.setObjectName("FiveButton")
        self.MinusButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("-"))
        self.MinusButton.setGeometry(QtCore.QRect(350, 300, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.MinusButton.setFont(font)
        self.MinusButton.setObjectName("MinusButton")
        self.FourButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("4"))
        self.FourButton.setGeometry(QtCore.QRect(20, 300, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.FourButton.setFont(font)
        self.FourButton.setObjectName("FourButton")
        self.SixButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("6"))
        self.SixButton.setGeometry(QtCore.QRect(240, 300, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.SixButton.setFont(font)
        self.SixButton.setObjectName("SixButton")
        self.TwoButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("2"))
        self.TwoButton.setGeometry(QtCore.QRect(130, 380, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.TwoButton.setFont(font)
        self.TwoButton.setObjectName("TwoButton")
        self.PlusButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("+"))
        self.PlusButton.setGeometry(QtCore.QRect(350, 380, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PlusButton.setFont(font)
        self.PlusButton.setObjectName("PlusButton")
        self.OneButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("1"))
        self.OneButton.setGeometry(QtCore.QRect(20, 380, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.OneButton.setFont(font)
        self.OneButton.setObjectName("OneButton")
        self.ThreeButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("3"))
        self.ThreeButton.setGeometry(QtCore.QRect(240, 380, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ThreeButton.setFont(font)
        self.ThreeButton.setObjectName("ThreeButton")
        self.ZeroButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.press_it("0"))
        self.ZeroButton.setGeometry(QtCore.QRect(130, 460, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ZeroButton.setFont(font)
        self.ZeroButton.setObjectName("ZeroButton")
        self.EqualButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.math_it())
        self.EqualButton.setGeometry(QtCore.QRect(350, 460, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.EqualButton.setFont(font)
        self.EqualButton.setObjectName("EqualButton")
        self.SignButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.plus_minus_it())
        self.SignButton.setGeometry(QtCore.QRect(20, 460, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.SignButton.setFont(font)
        self.SignButton.setObjectName("SignButton")
        self.DotButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.dot_it())
        self.DotButton.setGeometry(QtCore.QRect(240, 460, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.DotButton.setFont(font)
        self.DotButton.setObjectName("DotButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def remove_it(self):
        screen = self.OutputLabel.text()
        screen = screen[:-1]
        self.OutputLabel.setText(screen)


    def math_it(self):
        screen = self.OutputLabel.text()
        try:
            answer = eval(screen)
            self.OutputLabel.setText(str(answer))
        except:
            self.OutputLabel.setText("ERROR")
    
    def plus_minus_it(self):
        screen = self.OutputLabel.text()
        if "-" in screen:
            self.OutputLabel.setText(screen.replace("-", ""))
        else:
            self.OutputLabel.setText(f'-{screen}')

    def dot_it(self):
        screen = self.OutputLabel.text()

        i=len(self.OutputLabel.text())-1
        f=0
        while(i>=0 and screen[i]!='+' and screen[i]!='-' and screen[i]!='x' and screen[i]!='/' and screen[i]!='%' ):
            if screen[i] == ".":
                f=1
            i=i-1

        if f==0:
           self.OutputLabel.setText(f'{screen}.')
        else:
            pass

    def press_it(self,pressed):
        if pressed=='C':
             self.OutputLabel.setText("0")
        else :
            if self.OutputLabel.text()=='0':
               self.OutputLabel.setText('') 
            self.OutputLabel.setText(f'{self.OutputLabel.text()}{pressed}')



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.OutputLabel.setText(_translate("Dialog", "0"))
        self.PercentButton.setText(_translate("Dialog", "%"))
        self.CButton.setText(_translate("Dialog", "C"))
        self.ShiftButton.setText(_translate("Dialog", "<<"))
        self.DivisionButton.setText(_translate("Dialog", "/"))
        self.EightButton.setText(_translate("Dialog", "8"))
        self.TimesButton.setText(_translate("Dialog", "x"))
        self.SevenButton.setText(_translate("Dialog", "7"))
        self.NineButton.setText(_translate("Dialog", "9"))
        self.FiveButton.setText(_translate("Dialog", "5"))
        self.MinusButton.setText(_translate("Dialog", "-"))
        self.FourButton.setText(_translate("Dialog", "4"))
        self.SixButton.setText(_translate("Dialog", "6"))
        self.TwoButton.setText(_translate("Dialog", "2"))
        self.PlusButton.setText(_translate("Dialog", "+"))
        self.OneButton.setText(_translate("Dialog", "1"))
        self.ThreeButton.setText(_translate("Dialog", "3"))
        self.ZeroButton.setText(_translate("Dialog", "0"))
        self.EqualButton.setText(_translate("Dialog", "="))
        self.SignButton.setText(_translate("Dialog", "+/-"))
        self.DotButton.setText(_translate("Dialog", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
