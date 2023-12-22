# Decimal button is malfunctioning, doesnt allow the user to use it for the number after the arithmatic.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 10, 350, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.output.setFont(font)
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.percentage_it())
        self.percentButton.setGeometry(QtCore.QRect(10, 150, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 150, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 150, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(280, 150, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(280, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 330, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 330, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(280, 330, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 330, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 420, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 420, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(280, 420, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 420, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.equals())
        self.equalButton.setGeometry(QtCore.QRect(280, 510, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 510, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("+/-"))
        self.plusminusButton.setGeometry(QtCore.QRect(10, 510, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.pointButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.dot_it())
        self.pointButton.setGeometry(QtCore.QRect(190, 510, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pointButton.setFont(font)
        self.pointButton.setObjectName("pointButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def remove_it(self):
        screen = self.output.text()
        screen = screen[:-1]
        self.output.setText(screen)
    
    def percentage_it(self):
        screen = self.output.text()
        screen = self.output.setText(f"{screen}*0.01")

    def dot_it(self):
        # Decimal button is malfunctioning, doesnt allow the user to use it for the number after the arithmatic
        screen = self.output.text()
        if "+" in screen:
            plus = screen.split("+")
            for num in plus:
                if num[-1] in "0123456789" and "." not in num[:-1]: 
                    self.output.setText(f"{self.output.text()}.")
                if screen[-1] in ".+-x/%": 
                    return
        if "-" in screen:
            minus = screen.split("-")
            for num in minus:
                if num[-1] in "0123456789" and "." not in num[:-1]: 
                    self.output.setText(f"{self.output.text()}.")
                if screen[-1] in ".+-x/%": 
                    return
        if "*" in screen:
            times = screen.split("*")
            for num in times:
                if num[-1] in "0123456789" and "." not in num[:-1]: 
                    self.output.setText(f"{self.output.text()}.")
                if screen[-1] in ".+-x/%": 
                    return
        if "/" in screen:
            divide = screen.split("/")
            for num in divide:
                if num[-1] in "0123456789" and "." not in num[:-1]: 
                    self.output.setText(f"{self.output.text()}.")
                if screen[-1] in ".+-x/%": 
                    return
        elif screen[-1] in "0123456789" and "." not in screen[:-1]: 
            self.output.setText(f"{self.output.text()}.")
        elif screen[-1] in ".+-x/%": 
            return
        

    def equals(self):
        try:
            screen =  self.output.text()
            answer = eval(screen)
            self.output.setText(str(answer))
        except:
            self.output.setText("ERROR")


    def press_it(self, pressed):
        if pressed == "+/-":
            if self.output.text()[0] in "1234567890":
                self.output.setText(f"-{self.output.text()}")
                return
            if self.output.text()[0] == "-":
                self.output.setText(f"{self.output.text()[1:]}")
                return
        if pressed == "+":
            if self.output.text()[-1] == "+":
                return
        if pressed == "-":
            if self.output.text()[-1] == "-":
                return
        if pressed == "*":
            if self.output.text()[-1] == "*":
                return
        if pressed == "/":
            if self.output.text()[-1] == "/":
                return
        if pressed == "%":
            if self.output.text()[-1] == "%":
                return
        if pressed == "C":
            self.output.setText("0")
            return
        else:
            if self.output.text() == "0":
                self.output.setText("")
            self.output.setText(f"{self.output.text()}{pressed}")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.pointButton.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())