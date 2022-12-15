from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette,QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer
# import ui_main2 as main
from tkinter import *
from tkinter import simpledialog
import sys


GLOBAL_STATE = 0
                
import Sunmipol_logo_rc


class Ui_MainWindow(object):
        
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 611)
                MainWindow.setMinimumSize(QtCore.QSize(450, 611))
                MainWindow.setStyleSheet("")
                
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.GNG_Gauge_frame_Layer = QtWidgets.QVBoxLayout(self.centralwidget)
                self.GNG_Gauge_frame_Layer.setContentsMargins(0, 0, 0, 0)
                self.GNG_Gauge_frame_Layer.setSpacing(0)
                self.GNG_Gauge_frame_Layer.setObjectName(
                        "GNG_Gauge_frame_Layer")
                self.GNG_Gauge_frame = QtWidgets.QFrame(self.centralwidget)
                self.GNG_Gauge_frame.setStyleSheet("QFrame{\n"
                                                   "    background-color : rgb(56, 58, 89);\n"
                                                   "    color : rgb(220, 220, 220);\n"
                                                   "    border-radius :10px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "")
                self.GNG_Gauge_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.GNG_Gauge_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.GNG_Gauge_frame.setObjectName("GNG_Gauge_frame")
                self.verticalLayout = QtWidgets.QVBoxLayout(
                        self.GNG_Gauge_frame)
                self.verticalLayout.setObjectName("verticalLayout")
                self.title_bar = QtWidgets.QFrame(self.GNG_Gauge_frame)
                self.title_bar.setMaximumSize(QtCore.QSize(16777215, 30))
                self.title_bar.setStyleSheet("background-color: none;\n"
                                             "")
                self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.title_bar.setObjectName("title_bar")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.frame_title = QtWidgets.QFrame(self.title_bar)
                self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_title.setObjectName("frame_title")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
                self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.label_title = QtWidgets.QLabel(self.frame_title)
                self.label_title.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                               "color : rgb(235, 235, 235);")
                self.label_title.setObjectName("label_title")
                self.verticalLayout_2.addWidget(self.label_title)
                self.horizontalLayout.addWidget(self.frame_title)
                self.frame_btns = QtWidgets.QFrame(self.title_bar)
                self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_btns.setObjectName("frame_btns")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
                        self.frame_btns)
                self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 9)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
                self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
                self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
                self.btn_maximize.setStyleSheet("QPushButton{\n"
                                                "border : none;\n"
                                                "border-radius: 8px;\n"
                                                "background-color : rgb(85, 255, 127);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color : rgb(85, 255, 127,150);\n"
                                                "}")
                self.btn_maximize.setText("")
                self.btn_maximize.setObjectName("btn_maximize")
                self.horizontalLayout_4.addWidget(self.btn_maximize)
                self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
                self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
                self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
                self.btn_minimize.setStyleSheet("QPushButton{\n"
                                                "border : none;\n"
                                                "border-radius: 8px;\n"
                                                "background-color : rgb(255,170,0);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color : rgb(255,170,0,150);\n"
                                                "}")
                self.btn_minimize.setText("")
                self.btn_minimize.setObjectName("btn_minimize")
                self.horizontalLayout_4.addWidget(self.btn_minimize)
                self.btn_close = QtWidgets.QPushButton(self.frame_btns)
                self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
                self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
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
                self.horizontalLayout_4.addWidget(self.btn_close)
                self.horizontalLayout.addWidget(self.frame_btns)
                self.verticalLayout.addWidget(self.title_bar)
                self.content_bar = QtWidgets.QFrame(self.GNG_Gauge_frame)
                self.content_bar.setStyleSheet("")
                self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.content_bar.setObjectName("content_bar")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.content_bar)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.stackedWidget = QtWidgets.QStackedWidget(self.content_bar)
                self.stackedWidget.setObjectName("stackedWidget")
                self.page_home = QtWidgets.QWidget()
                self.page_home.setObjectName("page_home")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_home)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.frame_infos = QtWidgets.QFrame(self.page_home)
                self.frame_infos.setMinimumSize(QtCore.QSize(360, 460))
                self.frame_infos.setMaximumSize(QtCore.QSize(360, 460))
                self.frame_infos.setStyleSheet("background-color : none;")
                self.frame_infos.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_infos.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_infos.setObjectName("frame_infos")
                self.NotPass = QtWidgets.QLabel(self.frame_infos)
                self.NotPass.setGeometry(QtCore.QRect(185, 423, 91, 16))
                self.NotPass.setMinimumSize(QtCore.QSize(91, 16))
                self.NotPass.setMaximumSize(QtCore.QSize(91, 16))
                self.NotPass.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                           "color : rgb(78, 255, 220);\n"
                                           "background-color : none;")
                self.NotPass.setObjectName("NotPass")
                self.max = QtWidgets.QLineEdit(self.frame_infos)
                self.max.setGeometry(QtCore.QRect(185, 119, 161, 41))
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
                self.showText_3 = QtWidgets.QLabel(self.frame_infos)
                self.showText_3.setGeometry(QtCore.QRect(25, 377, 111, 28))
                self.showText_3.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                              "color : rgb(78, 255, 220);\n"
                                              "background-color : none;")
                self.showText_3.setObjectName("showText_3")
                self.Pass = QtWidgets.QLabel(self.frame_infos)
                self.Pass.setGeometry(QtCore.QRect(185, 383, 91, 16))
                self.Pass.setMinimumSize(QtCore.QSize(91, 16))
                self.Pass.setMaximumSize(QtCore.QSize(91, 16))
                self.Pass.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                        "color : rgb(78, 255, 220);\n"
                                        "background-color : none;\n"
                                        "")
                self.Pass.setObjectName("Pass")
                self.label_5 = QtWidgets.QLabel(self.frame_infos)
                self.label_5.setGeometry(QtCore.QRect(20, 125, 111, 28))
                self.label_5.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                           "color : rgb(78, 255, 220);\n"
                                           "background-color : none;")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.frame_infos)
                self.label_6.setGeometry(QtCore.QRect(25, 257, 111, 28))
                self.label_6.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                           "color : rgb(78, 255, 220);\n"
                                           "background-color : none;")
                self.label_6.setObjectName("label_6")
                self.cancel = QtWidgets.QPushButton(self.frame_infos)
                self.cancel.setGeometry(QtCore.QRect(195, 209, 75, 36))
                self.cancel.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                          "")
                self.cancel.setObjectName("cancel")
                self.showText_5 = QtWidgets.QLabel(self.frame_infos)
                self.showText_5.setGeometry(QtCore.QRect(25, 337, 111, 28))
                self.showText_5.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                              "color : rgb(78, 255, 220);\n"
                                              "background-color : none;")
                self.showText_5.setObjectName("showText_5")
                self.showText_4 = QtWidgets.QLabel(self.frame_infos)
                self.showText_4.setGeometry(QtCore.QRect(25, 417, 111, 28))
                self.showText_4.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                              "color : rgb(78, 255, 220);\n"
                                              "background-color : none;")
                self.showText_4.setObjectName("showText_4")
                self.PassORnotPass = QtWidgets.QLabel(self.frame_infos)
                self.PassORnotPass.setGeometry(QtCore.QRect(185, 303, 91, 16))
                self.PassORnotPass.setMinimumSize(QtCore.QSize(91, 16))
                self.PassORnotPass.setMaximumSize(QtCore.QSize(91, 16))
                self.PassORnotPass.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                                 "color : rgb(78, 255, 220);\n"
                                                 "background-color : none;")
                self.PassORnotPass.setObjectName("PassORnotPass")
                self.amount = QtWidgets.QLineEdit(self.frame_infos)
                self.amount.setGeometry(QtCore.QRect(185, 9, 161, 41))
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
                self.value = QtWidgets.QLabel(self.frame_infos)
                self.value.setGeometry(QtCore.QRect(185, 263, 91, 16))
                self.value.setMinimumSize(QtCore.QSize(91, 16))
                self.value.setMaximumSize(QtCore.QSize(91, 16))
                self.value.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                         "color : rgb(78, 255, 220);\n"
                                         "background-color : none;")
                self.value.setObjectName("value")
                self.process = QtWidgets.QPushButton(self.frame_infos)
                self.process.setGeometry(QtCore.QRect(195, 167, 75, 36))
                self.process.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                           "")
                self.process.setObjectName("process")
                self.min = QtWidgets.QLineEdit(self.frame_infos)
                self.min.setGeometry(QtCore.QRect(185, 64, 161, 41))
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
                self.showText_2 = QtWidgets.QLabel(self.frame_infos)
                self.showText_2.setGeometry(QtCore.QRect(25, 297, 111, 28))
                self.showText_2.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                              "color : rgb(78, 255, 220);\n"
                                              "background-color : none;")
                self.showText_2.setObjectName("showText_2")
                self.label = QtWidgets.QLabel(self.frame_infos)
                self.label.setGeometry(QtCore.QRect(20, 15, 111, 28))
                self.label.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                         "color : rgb(78, 255, 220);\n"
                                         "background-color : none;")
                self.label.setObjectName("label")
                self.total = QtWidgets.QLabel(self.frame_infos)
                self.total.setGeometry(QtCore.QRect(185, 343, 91, 16))
                self.total.setMinimumSize(QtCore.QSize(91, 16))
                self.total.setMaximumSize(QtCore.QSize(91, 16))
                self.total.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                         "color : rgb(78, 255, 220);\n"
                                         "background-color : none;")
                self.total.setObjectName("total")
                self.label_3 = QtWidgets.QLabel(self.frame_infos)
                self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 28))
                self.label_3.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
                                           "color : rgb(78, 255, 220);\n"
                                           "background-color : none;")
                self.label_3.setObjectName("label_3")
                self.Report = QtWidgets.QPushButton(self.frame_infos)
                self.Report.setGeometry(QtCore.QRect(270, 430, 75, 23))
                self.Report.setObjectName("Report")
                self.horizontalLayout_5.addWidget(self.frame_infos)
                self.stackedWidget.addWidget(self.page_home)
                self.page_dredits = QtWidgets.QWidget()
                self.page_dredits.setObjectName("page_dredits")
                self.stackedWidget.addWidget(self.page_dredits)
                self.verticalLayout_4.addWidget(self.stackedWidget)
                self.verticalLayout.addWidget(self.content_bar)
                self.credits_bar = QtWidgets.QFrame(self.GNG_Gauge_frame)
                self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
                self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.credits_bar.setObjectName("credits_bar")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
                        self.credits_bar)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
                self.frame_label_credits.setMaximumSize(
                        QtCore.QSize(16777215, 30))
                self.frame_label_credits.setFrameShape(
                        QtWidgets.QFrame.StyledPanel)
                self.frame_label_credits.setFrameShadow(
                        QtWidgets.QFrame.Raised)
                self.frame_label_credits.setObjectName("frame_label_credits")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
                        self.frame_label_credits)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_4 = QtWidgets.QLabel(self.frame_label_credits)
                self.label_4.setMinimumSize(QtCore.QSize(21, 21))
                self.label_4.setMaximumSize(QtCore.QSize(21, 21))
                self.label_4.setStyleSheet(
                        "image: url(:/image/Sunmipol_logo.png);")
                self.label_4.setText("")
                self.label_4.setObjectName("label_4")
                self.horizontalLayout_3.addWidget(self.label_4)
                self.label_7 = QtWidgets.QLabel(self.frame_label_credits)
                self.label_7.setMinimumSize(QtCore.QSize(0, 0))
                self.label_7.setMaximumSize(QtCore.QSize(16777215, 21))
                self.label_7.setStyleSheet("font: 87 14pt \"Segoe UI Black\";\n"
                                           "color: rgb(47, 195, 241)\n"
                                           "\n"
                                           "")
                self.label_7.setObjectName("label_7")
                self.horizontalLayout_3.addWidget(self.label_7)
                self.horizontalLayout_2.addWidget(self.frame_label_credits)
                self.frame_grip = QtWidgets.QFrame(self.credits_bar)
                self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
                self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
                self.frame_grip.setStyleSheet("padding : 5px;")
                self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_grip.setObjectName("frame_grip")
                self.horizontalLayout_2.addWidget(self.frame_grip)
                self.verticalLayout.addWidget(self.credits_bar)
                self.GNG_Gauge_frame_Layer.addWidget(self.GNG_Gauge_frame)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                MainWindow.setTabOrder(self.btn_close, self.btn_minimize)
                MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize)
                MainWindow.setTabOrder(self.btn_maximize, self.amount)
                MainWindow.setTabOrder(self.amount, self.min)
                MainWindow.setTabOrder(self.min, self.max)
                MainWindow.setTabOrder(self.max, self.process)
                MainWindow.setTabOrder(self.process, self.cancel)

                self.min.setValidator(QDoubleValidator(0.99, 99.99, 2))
                self.max.setValidator(QDoubleValidator(0.99, 99.99, 2))
                self.amount.setValidator(QDoubleValidator(0.99, 99.99, 2))

                self.btn_minimize.clicked.connect(lambda: self.showMinimized())
                self.btn_maximize.clicked.connect(
                        lambda: self.minizie_or_maximize_window())
                self.btn_close.clicked.connect(lambda: self.close())

        def minizie_or_maximize_window(self):
                global GLOBAL_STATE
                status = GLOBAL_STATE

                # IF NOT MAXIMIZED
                if status == 0:
                        GLOBAL_STATE = 0.5
                        self.showMaximized()
                # SET GLOBAL TO 1

                else:
                        GLOBAL_STATE = 0
                        self.showNormal()


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "GO-NOGO"))
                self.label_title.setText(_translate(
                        "MainWindow", "GO NOGO Test"))
                self.btn_maximize.setToolTip(
                        _translate("MainWindow", "Maximize"))
                self.btn_minimize.setToolTip(
                        _translate("MainWindow", "Minimize"))
                self.btn_close.setToolTip(_translate("MainWindow", "Close"))
                self.NotPass.setText(_translate("MainWindow", "0"))
                self.showText_3.setText(_translate("MainWindow", "ผ่าน"))
                self.Pass.setText(_translate("MainWindow", "0"))
                self.label_5.setText(_translate("MainWindow", "ค่า Max"))
                self.label_6.setText(_translate("MainWindow", "ค่าที่วัดได้"))
                self.cancel.setText(_translate("MainWindow", "ยกเลิก"))
                self.showText_5.setText(_translate(
                        "MainWindow", "จำนวนชิ้นงาน"))
                self.showText_4.setText(_translate("MainWindow", "ไม่ผ่าน"))
                self.PassORnotPass.setText(_translate(
                        "MainWindow", "ผ่าน/ไม่ผ่าน"))
                self.value.setText(_translate("MainWindow", "0"))
                self.process.setText(_translate("MainWindow", "เริ่มคำนวณ"))
                self.showText_2.setText(_translate("MainWindow", "คุณภาพ"))
                self.label.setText(_translate("MainWindow", "จำนวนชิ้นงาน"))
                self.total.setText(_translate("MainWindow", "0"))
                self.label_3.setText(_translate("MainWindow", "ค่า Min"))
                self.Report.setText(_translate("MainWindow", "Creat Report"))
                self.label_7.setText(_translate("MainWindow", " Sumipol"))


class Main(QMainWindow,  Ui_MainWindow):
    def __init__(self,):
        super().__init__()

        self.mwidget = QMainWindow(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setupUi(self)
        # self.minizie_or_maximize_window()
        
        

    

    # #center
    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())



if __name__ == "__main__":
    
   
    
    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
    MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)

    ex = Main()
    ex.show()
    sys.exit(app.exec_())
