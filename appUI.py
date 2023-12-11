# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_amazonaccount(object):
    def setupUi(self, amazonaccount):
        amazonaccount.setObjectName("amazonaccount")
        amazonaccount.resize(855, 387)
        font = QtGui.QFont()
        font.setPointSize(10)
        amazonaccount.setFont(font)
        amazonaccount.setStyleSheet("QDialog{\n"
"    background-color:#333333\n"
"    }\n"
"    \n"
"QDialog QGroupBox{\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"    align-items: center;\n"
"    background-color: #2700AB;\n"
"    background-image: linear-gradient(#464d55, #25292e);\n"
"    border-radius: 8px;\n"
"    border-width: 0.6;\n"
"    box-shadow: 0 10px 20px rgba(0, 0, 0, .1),0 3px 6px rgba(0, 0, 0, .05);\n"
"    box-sizing: border-box;\n"
"    color: white;\n"
"    cursor: pointer;\n"
"    display: inline-flex;\n"
"    flex-direction: column;\n"
"    font-family: expo-brand-demi,system-ui,-apple-system,BlinkMacSystemFont,\"Segoe UI\",Roboto,\"Helvetica Neue\",Arial,\"Noto Sans\",sans-serif,\"Apple Color Emoji\",\"Segoe UI Emoji\",\"Segoe UI Symbol\",\"Noto Color Emoji\";\n"
"    font-size: 18px;\n"
"    height: 52px;\n"
"    justify-content: center;\n"
"    line-height: 1;\n"
"    margin: 0;\n"
"    outline: none;\n"
"    overflow: hidden;\n"
"    padding: 0 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    transform: translate3d(0, 0, 0);\n"
"    transition: all 150ms;\n"
"    vertical-align: baseline;\n"
"    white-space: nowrap;\n"
"    user-select: none;\n"
"    -webkit-user-select: none;\n"
"    touch-action: manipulation;\n"
"\n"
"    border-radius:20px;\n"
"    border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    box-shadow: rgba(0, 1, 0, .2) 0 2px 8px;\n"
"    opacity: 0.5;\n"
"    color:red\n"
"}\n"
"\n"
"QPushButton:active {\n"
"    outline: 0;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    box-shadow: rgba(0, 0, 0, .5) 0 0 0 3px;\n"
"}\n"
"\n"
"QPushButton#start_button{\n"
"font-weight: bold;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(amazonaccount)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 791, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.container = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.container.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.container.setContentsMargins(5, 5, 5, 5)
        self.container.setSpacing(5)
        self.container.setObjectName("container")
        self.inputbox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.inputbox.setObjectName("inputbox")
        self.browse_button = QtWidgets.QPushButton(self.inputbox)
        self.browse_button.setGeometry(QtCore.QRect(170, 60, 190, 51))
        self.browse_button.setObjectName("browse_button")
        self.start_button = QtWidgets.QPushButton(self.inputbox)
        self.start_button.setGeometry(QtCore.QRect(320, 200, 161, 61))
        font = QtGui.QFont()
        font.setFamily("expo-brand-demi,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("")
        self.start_button.setObjectName("start_button")
        self.profiles_button = QtWidgets.QPushButton(self.inputbox)
        self.profiles_button.setGeometry(QtCore.QRect(430, 60, 171, 51))
        self.profiles_button.setObjectName("profiles_button")
        self.openLogbut = QtWidgets.QPushButton(self.inputbox)
        self.openLogbut.setGeometry(QtCore.QRect(60, 210, 151, 41))
        self.openLogbut.setObjectName("openLogbut")
        self.close_button = QtWidgets.QPushButton(self.inputbox)
        self.close_button.setGeometry(QtCore.QRect(590, 210, 121, 41))
        self.close_button.setObjectName("close_button")
        self.container.addWidget(self.inputbox, 0, 0, 1, 1)

        self.retranslateUi(amazonaccount)
        QtCore.QMetaObject.connectSlotsByName(amazonaccount)

    def retranslateUi(self, amazonaccount):
        _translate = QtCore.QCoreApplication.translate
        amazonaccount.setWindowTitle(_translate("amazonaccount", "Amazoun Accounts"))
        self.inputbox.setTitle(_translate("amazonaccount", "Input Data"))
        self.browse_button.setText(_translate("amazonaccount", "Open Data File"))
        self.start_button.setText(_translate("amazonaccount", "Start"))
        self.profiles_button.setText(_translate("amazonaccount", "Profiles"))
        self.openLogbut.setText(_translate("amazonaccount", "Open Log"))
        self.close_button.setText(_translate("amazonaccount", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    amazonaccount = QtWidgets.QDialog()
    ui = Ui_amazonaccount()
    ui.setupUi(amazonaccount)
    amazonaccount.show()
    sys.exit(app.exec_())
