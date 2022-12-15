# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '160264_GO-NOGO_V2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 451)
        MainWindow.setStyleSheet("QMainWindow\n"
"{qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 29, 73, 255), stop:0.5 rgba(42, 44, 111, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 271, 431))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color : rgb(56, 58, 89);\n"
"    color : rgb(220, 220, 220);\n"
"    border-radius :10px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_bar = QtWidgets.QFrame(self.frame)
        self.title_bar.setGeometry(QtCore.QRect(0, 0, 266, 35))
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.btn_minimiize = QtWidgets.QPushButton(self.title_bar)
        self.btn_minimiize.setGeometry(QtCore.QRect(204, 14, 16, 16))
        self.btn_minimiize.setStyleSheet("QPushButton{\n"
"border : none;\n"
"border-radius: 8px;\n"
"background-color : rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color : rgb(85, 255, 127,150);\n"
"}")
        self.btn_minimiize.setText("")
        self.btn_minimiize.setObjectName("btn_minimiize")
        self.btn_close = QtWidgets.QPushButton(self.title_bar)
        self.btn_close.setGeometry(QtCore.QRect(244, 14, 16, 16))
        self.btn_close.setStyleSheet("QPushButton{\n"
"border : none;\n"
"border-radius: 8px;\n"
"background-color : rgb(255,0,0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color : rgb(255,0,0,150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.btn_maxnimize = QtWidgets.QPushButton(self.title_bar)
        self.btn_maxnimize.setGeometry(QtCore.QRect(224, 14, 16, 16))
        self.btn_maxnimize.setStyleSheet("QPushButton{\n"
"border : none;\n"
"border-radius: 8px;\n"
"background-color : rgb(255,170,0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color : rgb(255,170,0,150);\n"
"}")
        self.btn_maxnimize.setText("")
        self.btn_maxnimize.setObjectName("btn_maxnimize")
        self.label_2 = QtWidgets.QLabel(self.title_bar)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 28))
        self.label_2.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(235, 235, 235);")
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 390, 111, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 21, 41))
        self.label_4.setStyleSheet("image: url(:/image/Sunmipol_logo.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(24, 9, 81, 21))
        self.label_7.setStyleSheet("font: 87 14pt \"Segoe UI Black\";\n"
"color: rgb(47, 195, 241)\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(17, 32, 237, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.max = QtWidgets.QLineEdit(self.frame_2)
        self.max.setGeometry(QtCore.QRect(100, 110, 131, 41))
        self.max.setStyleSheet("QLineEdit {\n"
"background-color :rgb(170, 170, 255);\n"
"color : rgb(28, 29, 73);\n"
"padding:10px;\n"
"border-style : none;\n"
"border-radius: 10px\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid rgb(85, 255, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid  rgb(85, 255, 255);\n"
"}")
        self.max.setText("")
        self.max.setObjectName("max")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(5, 107, 47, 28))
        self.label_5.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(5, 9, 74, 28))
        self.label.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(5, 61, 44, 28))
        self.label_3.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.label_3.setObjectName("label_3")
        self.PassORnotPass = QtWidgets.QLabel(self.frame_2)
        self.PassORnotPass.setGeometry(QtCore.QRect(100, 272, 91, 16))
        self.PassORnotPass.setMinimumSize(QtCore.QSize(91, 16))
        self.PassORnotPass.setMaximumSize(QtCore.QSize(91, 16))
        self.PassORnotPass.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.PassORnotPass.setObjectName("PassORnotPass")
        self.showText_2 = QtWidgets.QLabel(self.frame_2)
        self.showText_2.setGeometry(QtCore.QRect(10, 266, 43, 28))
        self.showText_2.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.showText_2.setObjectName("showText_2")
        self.showText_4 = QtWidgets.QLabel(self.frame_2)
        self.showText_4.setGeometry(QtCore.QRect(10, 334, 36, 28))
        self.showText_4.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.showText_4.setObjectName("showText_4")
        self.process = QtWidgets.QPushButton(self.frame_2)
        self.process.setGeometry(QtCore.QRect(100, 158, 75, 36))
        self.process.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"")
        self.process.setObjectName("process")
        self.cancel = QtWidgets.QPushButton(self.frame_2)
        self.cancel.setGeometry(QtCore.QRect(100, 200, 75, 36))
        self.cancel.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"")
        self.cancel.setObjectName("cancel")
        self.NotPass = QtWidgets.QLabel(self.frame_2)
        self.NotPass.setGeometry(QtCore.QRect(100, 340, 91, 16))
        self.NotPass.setMinimumSize(QtCore.QSize(91, 16))
        self.NotPass.setMaximumSize(QtCore.QSize(91, 16))
        self.NotPass.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.NotPass.setObjectName("NotPass")
        self.Pass = QtWidgets.QLabel(self.frame_2)
        self.Pass.setGeometry(QtCore.QRect(100, 306, 91, 16))
        self.Pass.setMinimumSize(QtCore.QSize(91, 16))
        self.Pass.setMaximumSize(QtCore.QSize(91, 16))
        self.Pass.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.Pass.setObjectName("Pass")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 236, 51, 28))
        self.label_6.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.label_6.setObjectName("label_6")
        self.amount = QtWidgets.QLineEdit(self.frame_2)
        self.amount.setGeometry(QtCore.QRect(100, 12, 131, 41))
        self.amount.setStyleSheet("QLineEdit {\n"
"background-color :rgb(170, 170, 255);\n"
"color : rgb(28, 29, 73);\n"
"padding:10px;\n"
"border-style : none;\n"
"border-radius: 10px\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid rgb(85, 255, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid  rgb(85, 255, 255);\n"
"}")
        self.amount.setObjectName("amount")
        self.showText = QtWidgets.QLabel(self.frame_2)
        self.showText.setGeometry(QtCore.QRect(100, 242, 91, 16))
        self.showText.setMinimumSize(QtCore.QSize(91, 16))
        self.showText.setMaximumSize(QtCore.QSize(91, 16))
        self.showText.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.showText.setObjectName("showText")
        self.showText_3 = QtWidgets.QLabel(self.frame_2)
        self.showText_3.setGeometry(QtCore.QRect(10, 300, 23, 28))
        self.showText_3.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(78, 255, 220);")
        self.showText_3.setObjectName("showText_3")
        self.min = QtWidgets.QLineEdit(self.frame_2)
        self.min.setGeometry(QtCore.QRect(100, 61, 131, 41))
        self.min.setStyleSheet("QLineEdit {\n"
"background-color :rgb(170, 170, 255);\n"
"color : rgb(28, 29, 73);\n"
"padding:10px;\n"
"border-style : none;\n"
"border-radius: 10px\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid rgb(85, 255, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid  rgb(85, 255, 255);\n"
"}")
        self.min.setObjectName("min")
        self.frame_2.raise_()
        self.title_bar.raise_()
        self.frame_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GO-NOGO"))
        self.label_2.setText(_translate("MainWindow", "GO NOGO Test"))
        self.label_7.setText(_translate("MainWindow", "Sumipol"))
        self.label_5.setText(_translate("MainWindow", "ค่า Max"))
        self.label.setText(_translate("MainWindow", "จำนวนชิ้นงาน"))
        self.label_3.setText(_translate("MainWindow", "ค่า Min"))
        self.PassORnotPass.setText(_translate("MainWindow", "ผ่าน/ไม่ผ่าน"))
        self.showText_2.setText(_translate("MainWindow", "คุณภาพ"))
        self.showText_4.setText(_translate("MainWindow", "ไม่ผ่าน"))
        self.process.setText(_translate("MainWindow", "เริ่มคำนวณ"))
        self.cancel.setText(_translate("MainWindow", "ยกเลิก"))
        self.NotPass.setText(_translate("MainWindow", "0"))
        self.Pass.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "ค่าที่วัดได้"))
        self.showText.setText(_translate("MainWindow", "0"))
        self.showText_3.setText(_translate("MainWindow", "ผ่าน"))

    def getmax(self):
        limit_max = float(self.max.text())
        return limit_max
    def getmin(self):
        limit_min = float(self.min.text())
        return limit_min

import Sunmipol_logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())