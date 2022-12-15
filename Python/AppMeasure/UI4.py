
from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette,QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer



import sys


GLOBAL_STATE = 0


class cssden(object):
#     def __init__(self):
#         super().__init__()


#         self.mwidget = QMainWindow(self)
#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#         self.setupUi(self)
#         def moveWindow(event):
#             # RESTORE BEFORE MOVE
#             if self.returnStatus() == 1:
#                 self.minizie_or_maximize_window(self)

#             # IF LEFT CLICK MOVE WINDOW
#             if event.buttons() == Qt.LeftButton:
#                 self.move(self.pos() + event.globalPos() - self.dragPos)
#                 self.dragPos = event.globalPos()
#                 event.accept()

    

#         self.title_bar.mouseMoveEvent = moveWindow
#         self.show()


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE



    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 700)
        MainWindow.setMinimumSize(QtCore.QSize(450, 611))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GNG_Gauge_frame_Layer = QtWidgets.QVBoxLayout(self.centralwidget)
        self.GNG_Gauge_frame_Layer.setContentsMargins(0, 0, 0, 0)
        self.GNG_Gauge_frame_Layer.setSpacing(0)
        self.GNG_Gauge_frame_Layer.setObjectName("GNG_Gauge_frame_Layer")
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GNG_Gauge_frame)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns)
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
        self.content_bar.setStyleSheet("background :  rgb(56, 58, 89);")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.content_bar)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.page_1)
        self.frame_2.setMinimumSize(QtCore.QSize(380, 400))
        self.frame_2.setMaximumSize(QtCore.QSize(380, 400))
        self.frame_2.setStyleSheet("background-color :rgb(230, 230, 230)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 144))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(90, 80, 190, 58))
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(190, 58))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("image:url(:/image/Sumipol.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(141, 9, 80, 80))
        self.label_8.setMaximumSize(QtCore.QSize(80, 80))
        self.label_8.setStyleSheet("image: url(:/image/Sunmipol_logo.png);\n"
"background:none;\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.label_10.raise_()
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(41, 20, 280, 50))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    boder: 2px solid rgb(45,45,45);\n"
"    boder-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color:rgb(30,30,30);\n"
"    border-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 1.5px solid rgb(0, 255, 255, 250);\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid rgb(0, 255, 255, 250);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(41, 80, 280, 50))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    boder: 2px solid rgb(45,45,45);\n"
"    boder-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color:rgb(30,30,30);\n"
"    border-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 1.5px solid rgb(0, 255, 255, 250);\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid rgb(0, 255, 255, 250);\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setGeometry(QtCore.QRect(41, 140, 271, 21))
        self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 3px solid rgb(100,100,100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135,135,135);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(0, 205, 255);\n"
"    background-color: rgb(0, 255, 255);\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 281, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50,50,50);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 2px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.frame_4)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setMinimumSize(QtCore.QSize(630, 218))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Tool1 = QtWidgets.QPushButton(self.frame_6)
        self.Tool1.setMinimumSize(QtCore.QSize(200, 200))
        self.Tool1.setMaximumSize(QtCore.QSize(200, 200))
        self.Tool1.setStyleSheet("QPushButton{\n"
"    image: url(:/image/Tool 1);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 4px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 4px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"\n"
"")
        self.Tool1.setText("")
        self.Tool1.setObjectName("Tool1")
        self.horizontalLayout_7.addWidget(self.Tool1)
        self.Tool2 = QtWidgets.QPushButton(self.frame_6)
        self.Tool2.setMinimumSize(QtCore.QSize(200, 200))
        self.Tool2.setMaximumSize(QtCore.QSize(200, 200))
        self.Tool2.setStyleSheet("QPushButton{\n"
"    image: url(:/image/Tool 2);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 4px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 4px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"")
        self.Tool2.setText("")
        self.Tool2.setObjectName("Tool2")
        self.horizontalLayout_7.addWidget(self.Tool2)
        self.Tool3 = QtWidgets.QPushButton(self.frame_6)
        self.Tool3.setMinimumSize(QtCore.QSize(200, 200))
        self.Tool3.setMaximumSize(QtCore.QSize(200, 200))
        self.Tool3.setStyleSheet("QPushButton{\n"
"    image: url(:/image/Tool 6.png);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 4px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 4px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"")
        self.Tool3.setText("")
        self.Tool3.setObjectName("Tool3")
        self.horizontalLayout_7.addWidget(self.Tool3)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setMinimumSize(QtCore.QSize(630, 218))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Tool4 = QtWidgets.QPushButton(self.frame_7)
        self.Tool4.setMinimumSize(QtCore.QSize(200, 200))
        self.Tool4.setMaximumSize(QtCore.QSize(200, 200))
        self.Tool4.setStyleSheet("QPushButton{\n"
"    image: url(:/image/Tool 4);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 4px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 4px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"")
        self.Tool4.setText("")
        self.Tool4.setObjectName("Tool4")
        self.horizontalLayout_8.addWidget(self.Tool4)
        self.Tool5 = QtWidgets.QPushButton(self.frame_7)
        self.Tool5.setMinimumSize(QtCore.QSize(200, 200))
        self.Tool5.setMaximumSize(QtCore.QSize(200, 200))
        self.Tool5.setStyleSheet("QPushButton{\n"
"    image: url(:/image/Tool 5);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 4px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 4px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"")
        self.Tool5.setText("")
        self.Tool5.setObjectName("Tool5")
        self.horizontalLayout_8.addWidget(self.Tool5)
        self.Tool6 = QtWidgets.QPushButton(self.frame_7)
        self.Tool6.setMinimumSize(QtCore.QSize(200, 200))
        self.Tool6.setMaximumSize(QtCore.QSize(200, 200))
        self.Tool6.setStyleSheet("QPushButton{\n"
"    image: url(:/image/Tool 6);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 4px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 4px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"")
        self.Tool6.setText("")
        self.Tool6.setObjectName("Tool6")
        self.horizontalLayout_8.addWidget(self.Tool6)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_infos = QtWidgets.QFrame(self.page_3)
        self.frame_infos.setGeometry(QtCore.QRect(493, 53, 380, 490))
        self.frame_infos.setMaximumSize(QtCore.QSize(380, 490))
        self.frame_infos.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_infos.setStyleSheet("background-color :  rgb(56, 58, 89);")
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
        self.cancel.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50,50,50);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"    font: 20pt \"FC Galaxy\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 2px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
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
        self.process.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50,50,50);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"    font: 20pt \"FC Galaxy\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 2px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
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
        self.Report.setGeometry(QtCore.QRect(260, 450, 111, 31))
        self.Report.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50,50,50);\n"
"    boder: 2px solid rgb(60,60,60);\n"
"    boder-radius: 5px;\n"
"    color: rgb(220, 220, 220);\n"
"    font: 20pt \"FC Galaxy\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 255, 255, 250);\n"
"    boder: 2px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}\n"
"")
        self.Report.setObjectName("Report")
        self.Home = QtWidgets.QPushButton(self.page_3)
        self.Home.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.Home.setStyleSheet("QPushButton {\n"
"image: url(:/image/Home.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"    image: url(:/image/Home - 250.png);\n"
"    background-color: rgb(120, 120, 120);\n"
"    boder: 2px rgb(255,164,24);\n"
"    color: rgb(35,35,35);\n"
"}")
        self.Home.setText("")
        self.Home.setObjectName("Home")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.page_4)
        self.frame.setStyleSheet("background-color : rgb(170, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 110, 30))
        self.label_9.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 40, 110, 30))
        self.label_11.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(30, 70, 110, 30))
        self.label_12.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(30, 100, 110, 30))
        self.label_13.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(30, 130, 110, 30))
        self.label_14.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(340, 10, 131, 30))
        self.label_15.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(340, 40, 131, 30))
        self.label_16.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(340, 100, 131, 30))
        self.label_17.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(340, 70, 131, 30))
        self.label_18.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(340, 130, 131, 30))
        self.label_19.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_19.setObjectName("label_19")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(660, 10, 141, 30))
        self.label_30.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(660, 40, 141, 30))
        self.label_31.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_31.setObjectName("label_31")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(660, 70, 141, 30))
        self.label_33.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(660, 100, 141, 30))
        self.label_34.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(980, 130, 141, 30))
        self.label_35.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(980, 40, 141, 30))
        self.label_36.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(980, 10, 141, 30))
        self.label_37.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(980, 100, 141, 30))
        self.label_38.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(980, 70, 141, 30))
        self.label_39.setStyleSheet("font: 20pt \"FC Galaxy\";\n"
"color : rgb(255, 255, 255);\n"
"background-color : none;")
        self.label_39.setObjectName("label_39")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 15, 113, 20))
        self.lineEdit_3.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 45, 113, 20))
        self.lineEdit_4.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 135, 113, 20))
        self.lineEdit_5.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 75, 113, 20))
        self.lineEdit_6.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 105, 113, 20))
        self.lineEdit_8.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(500, 15, 113, 20))
        self.lineEdit_7.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(500, 105, 113, 20))
        self.lineEdit_9.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(500, 45, 113, 20))
        self.lineEdit_10.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(500, 75, 113, 20))
        self.lineEdit_11.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(500, 135, 113, 20))
        self.lineEdit_12.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(1110, 15, 113, 20))
        self.lineEdit_13.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(1110, 105, 113, 20))
        self.lineEdit_14.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(1110, 45, 113, 20))
        self.lineEdit_15.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(1110, 75, 113, 20))
        self.lineEdit_16.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(1110, 135, 113, 20))
        self.lineEdit_17.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(830, 15, 113, 20))
        self.lineEdit_18.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(830, 45, 113, 20))
        self.lineEdit_20.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setGeometry(QtCore.QRect(830, 75, 113, 20))
        self.lineEdit_21.setStyleSheet("border: none;\n"
"background: rgb(255, 255, 255);\n"
"")
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 40, 1193, 1))
        self.line.setTabletTracking(False)
        self.line.setAcceptDrops(False)
        self.line.setStyleSheet("background: rgb(255, 255, 255)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(30, 70, 1193, 1))
        self.line_2.setTabletTracking(False)
        self.line_2.setAcceptDrops(False)
        self.line_2.setStyleSheet("background: rgb(255, 255, 255)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(30, 100, 1193, 1))
        self.line_3.setTabletTracking(False)
        self.line_3.setAcceptDrops(False)
        self.line_3.setStyleSheet("background: rgb(255, 255, 255)")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(30, 130, 1193, 1))
        self.line_4.setTabletTracking(False)
        self.line_4.setAcceptDrops(False)
        self.line_4.setStyleSheet("background: rgb(255, 255, 255)")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(20, 160, 1282, 396))
        self.frame_5.setStyleSheet("background-color:none;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_466 = QtWidgets.QLabel(self.frame_5)
        self.label_466.setGeometry(QtCore.QRect(1150, 278, 45, 25))
        self.label_466.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_466.setText("")
        self.label_466.setAlignment(QtCore.Qt.AlignCenter)
        self.label_466.setObjectName("label_466")
        self.label_404 = QtWidgets.QLabel(self.frame_5)
        self.label_404.setGeometry(QtCore.QRect(849, 163, 45, 25))
        self.label_404.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_404.setText("")
        self.label_404.setAlignment(QtCore.Qt.AlignCenter)
        self.label_404.setObjectName("label_404")
        self.label_367 = QtWidgets.QLabel(self.frame_5)
        self.label_367.setGeometry(QtCore.QRect(849, 140, 45, 25))
        self.label_367.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_367.setText("")
        self.label_367.setAlignment(QtCore.Qt.AlignCenter)
        self.label_367.setObjectName("label_367")
        self.label_561 = QtWidgets.QLabel(self.frame_5)
        self.label_561.setGeometry(QtCore.QRect(462, 347, 45, 25))
        self.label_561.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_561.setText("")
        self.label_561.setAlignment(QtCore.Qt.AlignCenter)
        self.label_561.setObjectName("label_561")
        self.label_618 = QtWidgets.QLabel(self.frame_5)
        self.label_618.setGeometry(QtCore.QRect(236, 370, 61, 25))
        self.label_618.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_618.setText("")
        self.label_618.setAlignment(QtCore.Qt.AlignCenter)
        self.label_618.setObjectName("label_618")
        self.label_510 = QtWidgets.QLabel(self.frame_5)
        self.label_510.setGeometry(QtCore.QRect(28, 232, 141, 25))
        self.label_510.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_510.setText("")
        self.label_510.setAlignment(QtCore.Qt.AlignCenter)
        self.label_510.setObjectName("label_510")
        self.label_462 = QtWidgets.QLabel(self.frame_5)
        self.label_462.setGeometry(QtCore.QRect(364, 255, 51, 25))
        self.label_462.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_462.setText("")
        self.label_462.setAlignment(QtCore.Qt.AlignCenter)
        self.label_462.setObjectName("label_462")
        self.label_283 = QtWidgets.QLabel(self.frame_5)
        self.label_283.setGeometry(QtCore.QRect(892, 71, 45, 25))
        self.label_283.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_283.setText("")
        self.label_283.setAlignment(QtCore.Qt.AlignCenter)
        self.label_283.setObjectName("label_283")
        self.label_498 = QtWidgets.QLabel(self.frame_5)
        self.label_498.setGeometry(QtCore.QRect(505, 278, 45, 25))
        self.label_498.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_498.setText("")
        self.label_498.setAlignment(QtCore.Qt.AlignCenter)
        self.label_498.setObjectName("label_498")
        self.label_534 = QtWidgets.QLabel(self.frame_5)
        self.label_534.setGeometry(QtCore.QRect(548, 347, 45, 25))
        self.label_534.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_534.setText("")
        self.label_534.setAlignment(QtCore.Qt.AlignCenter)
        self.label_534.setObjectName("label_534")
        self.label_363 = QtWidgets.QLabel(self.frame_5)
        self.label_363.setGeometry(QtCore.QRect(892, 94, 45, 25))
        self.label_363.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_363.setText("")
        self.label_363.setAlignment(QtCore.Qt.AlignCenter)
        self.label_363.setObjectName("label_363")
        self.label_459 = QtWidgets.QLabel(self.frame_5)
        self.label_459.setGeometry(QtCore.QRect(295, 278, 71, 25))
        self.label_459.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_459.setText("")
        self.label_459.setAlignment(QtCore.Qt.AlignCenter)
        self.label_459.setObjectName("label_459")
        self.label_452 = QtWidgets.QLabel(self.frame_5)
        self.label_452.setGeometry(QtCore.QRect(167, 232, 71, 25))
        self.label_452.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_452.setText("")
        self.label_452.setAlignment(QtCore.Qt.AlignCenter)
        self.label_452.setObjectName("label_452")
        self.label_420 = QtWidgets.QLabel(self.frame_5)
        self.label_420.setGeometry(QtCore.QRect(505, 209, 45, 25))
        self.label_420.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_420.setText("")
        self.label_420.setAlignment(QtCore.Qt.AlignCenter)
        self.label_420.setObjectName("label_420")
        self.label_366 = QtWidgets.QLabel(self.frame_5)
        self.label_366.setGeometry(QtCore.QRect(591, 94, 45, 25))
        self.label_366.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_366.setText("")
        self.label_366.setAlignment(QtCore.Qt.AlignCenter)
        self.label_366.setObjectName("label_366")
        self.label_546 = QtWidgets.QLabel(self.frame_5)
        self.label_546.setGeometry(QtCore.QRect(1107, 301, 45, 25))
        self.label_546.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_546.setText("")
        self.label_546.setAlignment(QtCore.Qt.AlignCenter)
        self.label_546.setObjectName("label_546")
        self.label_518 = QtWidgets.QLabel(self.frame_5)
        self.label_518.setGeometry(QtCore.QRect(1236, 232, 45, 25))
        self.label_518.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_518.setText("")
        self.label_518.setAlignment(QtCore.Qt.AlignCenter)
        self.label_518.setObjectName("label_518")
        self.label_507 = QtWidgets.QLabel(self.frame_5)
        self.label_507.setGeometry(QtCore.QRect(236, 255, 61, 25))
        self.label_507.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_507.setText("")
        self.label_507.setAlignment(QtCore.Qt.AlignCenter)
        self.label_507.setObjectName("label_507")
        self.label_573 = QtWidgets.QLabel(self.frame_5)
        self.label_573.setGeometry(QtCore.QRect(0, 301, 30, 25))
        self.label_573.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_573.setAlignment(QtCore.Qt.AlignCenter)
        self.label_573.setObjectName("label_573")
        self.label_372 = QtWidgets.QLabel(self.frame_5)
        self.label_372.setGeometry(QtCore.QRect(1107, 186, 45, 25))
        self.label_372.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_372.setText("")
        self.label_372.setAlignment(QtCore.Qt.AlignCenter)
        self.label_372.setObjectName("label_372")
        self.label_403 = QtWidgets.QLabel(self.frame_5)
        self.label_403.setGeometry(QtCore.QRect(677, 186, 45, 25))
        self.label_403.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_403.setText("")
        self.label_403.setAlignment(QtCore.Qt.AlignCenter)
        self.label_403.setObjectName("label_403")
        self.label_250 = QtWidgets.QLabel(self.frame_5)
        self.label_250.setGeometry(QtCore.QRect(1021, 48, 45, 25))
        self.label_250.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_250.setText("")
        self.label_250.setAlignment(QtCore.Qt.AlignCenter)
        self.label_250.setObjectName("label_250")
        self.label_243 = QtWidgets.QLabel(self.frame_5)
        self.label_243.setGeometry(QtCore.QRect(505, 48, 45, 25))
        self.label_243.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_243.setText("")
        self.label_243.setAlignment(QtCore.Qt.AlignCenter)
        self.label_243.setObjectName("label_243")
        self.label_554 = QtWidgets.QLabel(self.frame_5)
        self.label_554.setGeometry(QtCore.QRect(1021, 301, 45, 25))
        self.label_554.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_554.setText("")
        self.label_554.setAlignment(QtCore.Qt.AlignCenter)
        self.label_554.setObjectName("label_554")
        self.label_328 = QtWidgets.QLabel(self.frame_5)
        self.label_328.setGeometry(QtCore.QRect(978, 117, 45, 25))
        self.label_328.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_328.setText("")
        self.label_328.setAlignment(QtCore.Qt.AlignCenter)
        self.label_328.setObjectName("label_328")
        self.label_192 = QtWidgets.QLabel(self.frame_5)
        self.label_192.setGeometry(QtCore.QRect(236, 2, 61, 25))
        self.label_192.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_192.setText("")
        self.label_192.setAlignment(QtCore.Qt.AlignCenter)
        self.label_192.setObjectName("label_192")
        self.label_572 = QtWidgets.QLabel(self.frame_5)
        self.label_572.setGeometry(QtCore.QRect(978, 347, 45, 25))
        self.label_572.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_572.setText("")
        self.label_572.setAlignment(QtCore.Qt.AlignCenter)
        self.label_572.setObjectName("label_572")
        self.label_337 = QtWidgets.QLabel(self.frame_5)
        self.label_337.setGeometry(QtCore.QRect(236, 94, 61, 25))
        self.label_337.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_337.setText("")
        self.label_337.setAlignment(QtCore.Qt.AlignCenter)
        self.label_337.setObjectName("label_337")
        self.label_188 = QtWidgets.QLabel(self.frame_5)
        self.label_188.setGeometry(QtCore.QRect(28, 2, 141, 25))
        self.label_188.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_188.setAlignment(QtCore.Qt.AlignCenter)
        self.label_188.setObjectName("label_188")
        self.label_233 = QtWidgets.QLabel(self.frame_5)
        self.label_233.setGeometry(QtCore.QRect(1193, 25, 45, 25))
        self.label_233.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_233.setText("")
        self.label_233.setAlignment(QtCore.Qt.AlignCenter)
        self.label_233.setObjectName("label_233")
        self.label_302 = QtWidgets.QLabel(self.frame_5)
        self.label_302.setGeometry(QtCore.QRect(591, 117, 45, 25))
        self.label_302.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_302.setText("")
        self.label_302.setAlignment(QtCore.Qt.AlignCenter)
        self.label_302.setObjectName("label_302")
        self.label_219 = QtWidgets.QLabel(self.frame_5)
        self.label_219.setGeometry(QtCore.QRect(806, 2, 45, 25))
        self.label_219.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_219.setAlignment(QtCore.Qt.AlignCenter)
        self.label_219.setObjectName("label_219")
        self.label_397 = QtWidgets.QLabel(self.frame_5)
        self.label_397.setGeometry(QtCore.QRect(1236, 209, 45, 25))
        self.label_397.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_397.setText("")
        self.label_397.setAlignment(QtCore.Qt.AlignCenter)
        self.label_397.setObjectName("label_397")
        self.label_288 = QtWidgets.QLabel(self.frame_5)
        self.label_288.setGeometry(QtCore.QRect(413, 71, 51, 25))
        self.label_288.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_288.setText("")
        self.label_288.setAlignment(QtCore.Qt.AlignCenter)
        self.label_288.setObjectName("label_288")
        self.label_308 = QtWidgets.QLabel(self.frame_5)
        self.label_308.setGeometry(QtCore.QRect(167, 140, 71, 25))
        self.label_308.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_308.setText("")
        self.label_308.setAlignment(QtCore.Qt.AlignCenter)
        self.label_308.setObjectName("label_308")
        self.label_261 = QtWidgets.QLabel(self.frame_5)
        self.label_261.setGeometry(QtCore.QRect(892, 48, 45, 25))
        self.label_261.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_261.setText("")
        self.label_261.setAlignment(QtCore.Qt.AlignCenter)
        self.label_261.setObjectName("label_261")
        self.label_418 = QtWidgets.QLabel(self.frame_5)
        self.label_418.setGeometry(QtCore.QRect(167, 186, 71, 25))
        self.label_418.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_418.setText("")
        self.label_418.setAlignment(QtCore.Qt.AlignCenter)
        self.label_418.setObjectName("label_418")
        self.label_575 = QtWidgets.QLabel(self.frame_5)
        self.label_575.setGeometry(QtCore.QRect(935, 347, 45, 25))
        self.label_575.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_575.setText("")
        self.label_575.setAlignment(QtCore.Qt.AlignCenter)
        self.label_575.setObjectName("label_575")
        self.label_221 = QtWidgets.QLabel(self.frame_5)
        self.label_221.setGeometry(QtCore.QRect(978, 2, 45, 25))
        self.label_221.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_221.setAlignment(QtCore.Qt.AlignCenter)
        self.label_221.setObjectName("label_221")
        self.label_583 = QtWidgets.QLabel(self.frame_5)
        self.label_583.setGeometry(QtCore.QRect(1193, 301, 45, 25))
        self.label_583.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_583.setText("")
        self.label_583.setAlignment(QtCore.Qt.AlignCenter)
        self.label_583.setObjectName("label_583")
        self.label_231 = QtWidgets.QLabel(self.frame_5)
        self.label_231.setGeometry(QtCore.QRect(806, 25, 45, 25))
        self.label_231.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_231.setText("")
        self.label_231.setAlignment(QtCore.Qt.AlignCenter)
        self.label_231.setObjectName("label_231")
        self.label_254 = QtWidgets.QLabel(self.frame_5)
        self.label_254.setGeometry(QtCore.QRect(1150, 48, 45, 25))
        self.label_254.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_254.setText("")
        self.label_254.setAlignment(QtCore.Qt.AlignCenter)
        self.label_254.setObjectName("label_254")
        self.label_195 = QtWidgets.QLabel(self.frame_5)
        self.label_195.setGeometry(QtCore.QRect(1150, 25, 45, 25))
        self.label_195.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_195.setText("")
        self.label_195.setAlignment(QtCore.Qt.AlignCenter)
        self.label_195.setObjectName("label_195")
        self.label_296 = QtWidgets.QLabel(self.frame_5)
        self.label_296.setGeometry(QtCore.QRect(167, 94, 71, 25))
        self.label_296.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_296.setText("")
        self.label_296.setAlignment(QtCore.Qt.AlignCenter)
        self.label_296.setObjectName("label_296")
        self.label_521 = QtWidgets.QLabel(self.frame_5)
        self.label_521.setGeometry(QtCore.QRect(413, 232, 51, 25))
        self.label_521.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_521.setText("")
        self.label_521.setAlignment(QtCore.Qt.AlignCenter)
        self.label_521.setObjectName("label_521")
        self.label_375 = QtWidgets.QLabel(self.frame_5)
        self.label_375.setGeometry(QtCore.QRect(364, 209, 51, 25))
        self.label_375.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_375.setText("")
        self.label_375.setAlignment(QtCore.Qt.AlignCenter)
        self.label_375.setObjectName("label_375")
        self.label_305 = QtWidgets.QLabel(self.frame_5)
        self.label_305.setGeometry(QtCore.QRect(295, 117, 71, 25))
        self.label_305.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_305.setText("")
        self.label_305.setAlignment(QtCore.Qt.AlignCenter)
        self.label_305.setObjectName("label_305")
        self.label_208 = QtWidgets.QLabel(self.frame_5)
        self.label_208.setGeometry(QtCore.QRect(763, 2, 45, 25))
        self.label_208.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_208.setAlignment(QtCore.Qt.AlignCenter)
        self.label_208.setObjectName("label_208")
        self.label_464 = QtWidgets.QLabel(self.frame_5)
        self.label_464.setGeometry(QtCore.QRect(167, 278, 71, 25))
        self.label_464.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_464.setText("")
        self.label_464.setAlignment(QtCore.Qt.AlignCenter)
        self.label_464.setObjectName("label_464")
        self.label_484 = QtWidgets.QLabel(self.frame_5)
        self.label_484.setGeometry(QtCore.QRect(978, 255, 45, 25))
        self.label_484.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_484.setText("")
        self.label_484.setAlignment(QtCore.Qt.AlignCenter)
        self.label_484.setObjectName("label_484")
        self.label_258 = QtWidgets.QLabel(self.frame_5)
        self.label_258.setGeometry(QtCore.QRect(720, 48, 45, 25))
        self.label_258.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_258.setText("")
        self.label_258.setAlignment(QtCore.Qt.AlignCenter)
        self.label_258.setObjectName("label_258")
        self.label_435 = QtWidgets.QLabel(self.frame_5)
        self.label_435.setGeometry(QtCore.QRect(413, 186, 51, 25))
        self.label_435.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_435.setText("")
        self.label_435.setAlignment(QtCore.Qt.AlignCenter)
        self.label_435.setObjectName("label_435")
        self.label_448 = QtWidgets.QLabel(self.frame_5)
        self.label_448.setGeometry(QtCore.QRect(806, 278, 45, 25))
        self.label_448.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_448.setText("")
        self.label_448.setAlignment(QtCore.Qt.AlignCenter)
        self.label_448.setObjectName("label_448")
        self.label_265 = QtWidgets.QLabel(self.frame_5)
        self.label_265.setGeometry(QtCore.QRect(295, 71, 71, 25))
        self.label_265.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_265.setText("")
        self.label_265.setAlignment(QtCore.Qt.AlignCenter)
        self.label_265.setObjectName("label_265")
        self.label_543 = QtWidgets.QLabel(self.frame_5)
        self.label_543.setGeometry(QtCore.QRect(634, 301, 45, 25))
        self.label_543.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_543.setText("")
        self.label_543.setAlignment(QtCore.Qt.AlignCenter)
        self.label_543.setObjectName("label_543")
        self.label_447 = QtWidgets.QLabel(self.frame_5)
        self.label_447.setGeometry(QtCore.QRect(1193, 278, 45, 25))
        self.label_447.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_447.setText("")
        self.label_447.setAlignment(QtCore.Qt.AlignCenter)
        self.label_447.setObjectName("label_447")
        self.label_271 = QtWidgets.QLabel(self.frame_5)
        self.label_271.setGeometry(QtCore.QRect(167, 71, 71, 25))
        self.label_271.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_271.setText("")
        self.label_271.setAlignment(QtCore.Qt.AlignCenter)
        self.label_271.setObjectName("label_271")
        self.label_565 = QtWidgets.QLabel(self.frame_5)
        self.label_565.setGeometry(QtCore.QRect(236, 347, 61, 25))
        self.label_565.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_565.setText("")
        self.label_565.setAlignment(QtCore.Qt.AlignCenter)
        self.label_565.setObjectName("label_565")
        self.label_342 = QtWidgets.QLabel(self.frame_5)
        self.label_342.setGeometry(QtCore.QRect(505, 140, 45, 25))
        self.label_342.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_342.setText("")
        self.label_342.setAlignment(QtCore.Qt.AlignCenter)
        self.label_342.setObjectName("label_342")
        self.label_424 = QtWidgets.QLabel(self.frame_5)
        self.label_424.setGeometry(QtCore.QRect(935, 163, 45, 25))
        self.label_424.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_424.setText("")
        self.label_424.setAlignment(QtCore.Qt.AlignCenter)
        self.label_424.setObjectName("label_424")
        self.label_552 = QtWidgets.QLabel(self.frame_5)
        self.label_552.setGeometry(QtCore.QRect(1064, 347, 45, 25))
        self.label_552.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_552.setText("")
        self.label_552.setAlignment(QtCore.Qt.AlignCenter)
        self.label_552.setObjectName("label_552")
        self.label_496 = QtWidgets.QLabel(self.frame_5)
        self.label_496.setGeometry(QtCore.QRect(167, 255, 71, 25))
        self.label_496.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_496.setText("")
        self.label_496.setAlignment(QtCore.Qt.AlignCenter)
        self.label_496.setObjectName("label_496")
        self.label_564 = QtWidgets.QLabel(self.frame_5)
        self.label_564.setGeometry(QtCore.QRect(806, 324, 45, 25))
        self.label_564.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_564.setText("")
        self.label_564.setAlignment(QtCore.Qt.AlignCenter)
        self.label_564.setObjectName("label_564")
        self.label_392 = QtWidgets.QLabel(self.frame_5)
        self.label_392.setGeometry(QtCore.QRect(295, 163, 71, 25))
        self.label_392.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_392.setText("")
        self.label_392.setAlignment(QtCore.Qt.AlignCenter)
        self.label_392.setObjectName("label_392")
        self.label_325 = QtWidgets.QLabel(self.frame_5)
        self.label_325.setGeometry(QtCore.QRect(677, 117, 45, 25))
        self.label_325.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_325.setText("")
        self.label_325.setAlignment(QtCore.Qt.AlignCenter)
        self.label_325.setObjectName("label_325")
        self.label_544 = QtWidgets.QLabel(self.frame_5)
        self.label_544.setGeometry(QtCore.QRect(1150, 347, 45, 25))
        self.label_544.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_544.setText("")
        self.label_544.setAlignment(QtCore.Qt.AlignCenter)
        self.label_544.setObjectName("label_544")
        self.label_412 = QtWidgets.QLabel(self.frame_5)
        self.label_412.setGeometry(QtCore.QRect(720, 163, 45, 25))
        self.label_412.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_412.setText("")
        self.label_412.setAlignment(QtCore.Qt.AlignCenter)
        self.label_412.setObjectName("label_412")
        self.label_213 = QtWidgets.QLabel(self.frame_5)
        self.label_213.setGeometry(QtCore.QRect(364, 2, 51, 25))
        self.label_213.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_213.setAlignment(QtCore.Qt.AlignCenter)
        self.label_213.setObjectName("label_213")
        self.label_336 = QtWidgets.QLabel(self.frame_5)
        self.label_336.setGeometry(QtCore.QRect(677, 140, 45, 25))
        self.label_336.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_336.setText("")
        self.label_336.setAlignment(QtCore.Qt.AlignCenter)
        self.label_336.setObjectName("label_336")
        self.label_264 = QtWidgets.QLabel(self.frame_5)
        self.label_264.setGeometry(QtCore.QRect(1064, 48, 45, 25))
        self.label_264.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_264.setText("")
        self.label_264.setAlignment(QtCore.Qt.AlignCenter)
        self.label_264.setObjectName("label_264")
        self.label_378 = QtWidgets.QLabel(self.frame_5)
        self.label_378.setGeometry(QtCore.QRect(548, 209, 45, 25))
        self.label_378.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_378.setText("")
        self.label_378.setAlignment(QtCore.Qt.AlignCenter)
        self.label_378.setObjectName("label_378")
        self.label_590 = QtWidgets.QLabel(self.frame_5)
        self.label_590.setGeometry(QtCore.QRect(591, 347, 45, 25))
        self.label_590.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_590.setText("")
        self.label_590.setAlignment(QtCore.Qt.AlignCenter)
        self.label_590.setObjectName("label_590")
        self.label_555 = QtWidgets.QLabel(self.frame_5)
        self.label_555.setGeometry(QtCore.QRect(413, 347, 51, 25))
        self.label_555.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_555.setText("")
        self.label_555.setAlignment(QtCore.Qt.AlignCenter)
        self.label_555.setObjectName("label_555")
        self.label_332 = QtWidgets.QLabel(self.frame_5)
        self.label_332.setGeometry(QtCore.QRect(1236, 117, 45, 25))
        self.label_332.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_332.setText("")
        self.label_332.setAlignment(QtCore.Qt.AlignCenter)
        self.label_332.setObjectName("label_332")
        self.label_204 = QtWidgets.QLabel(self.frame_5)
        self.label_204.setGeometry(QtCore.QRect(413, 25, 51, 25))
        self.label_204.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_204.setText("")
        self.label_204.setAlignment(QtCore.Qt.AlignCenter)
        self.label_204.setObjectName("label_204")
        self.label_354 = QtWidgets.QLabel(self.frame_5)
        self.label_354.setGeometry(QtCore.QRect(28, 94, 141, 25))
        self.label_354.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_354.setText("")
        self.label_354.setAlignment(QtCore.Qt.AlignCenter)
        self.label_354.setObjectName("label_354")
        self.label_550 = QtWidgets.QLabel(self.frame_5)
        self.label_550.setGeometry(QtCore.QRect(28, 324, 141, 25))
        self.label_550.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_550.setText("")
        self.label_550.setAlignment(QtCore.Qt.AlignCenter)
        self.label_550.setObjectName("label_550")
        self.label_352 = QtWidgets.QLabel(self.frame_5)
        self.label_352.setGeometry(QtCore.QRect(1064, 117, 45, 25))
        self.label_352.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_352.setText("")
        self.label_352.setAlignment(QtCore.Qt.AlignCenter)
        self.label_352.setObjectName("label_352")
        self.label_310 = QtWidgets.QLabel(self.frame_5)
        self.label_310.setGeometry(QtCore.QRect(1150, 140, 45, 25))
        self.label_310.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_310.setText("")
        self.label_310.setAlignment(QtCore.Qt.AlignCenter)
        self.label_310.setObjectName("label_310")
        self.label_612 = QtWidgets.QLabel(self.frame_5)
        self.label_612.setGeometry(QtCore.QRect(505, 370, 45, 25))
        self.label_612.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_612.setText("")
        self.label_612.setAlignment(QtCore.Qt.AlignCenter)
        self.label_612.setObjectName("label_612")
        self.label_300 = QtWidgets.QLabel(self.frame_5)
        self.label_300.setGeometry(QtCore.QRect(548, 140, 45, 25))
        self.label_300.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_300.setText("")
        self.label_300.setAlignment(QtCore.Qt.AlignCenter)
        self.label_300.setObjectName("label_300")
        self.label_566 = QtWidgets.QLabel(self.frame_5)
        self.label_566.setGeometry(QtCore.QRect(1236, 324, 45, 25))
        self.label_566.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_566.setText("")
        self.label_566.setAlignment(QtCore.Qt.AlignCenter)
        self.label_566.setObjectName("label_566")
        self.label_269 = QtWidgets.QLabel(self.frame_5)
        self.label_269.setGeometry(QtCore.QRect(806, 71, 45, 25))
        self.label_269.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_269.setText("")
        self.label_269.setAlignment(QtCore.Qt.AlignCenter)
        self.label_269.setObjectName("label_269")
        self.label_362 = QtWidgets.QLabel(self.frame_5)
        self.label_362.setGeometry(QtCore.QRect(1236, 94, 45, 25))
        self.label_362.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_362.setText("")
        self.label_362.setAlignment(QtCore.Qt.AlignCenter)
        self.label_362.setObjectName("label_362")
        self.label_251 = QtWidgets.QLabel(self.frame_5)
        self.label_251.setGeometry(QtCore.QRect(462, 48, 45, 25))
        self.label_251.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_251.setText("")
        self.label_251.setAlignment(QtCore.Qt.AlignCenter)
        self.label_251.setObjectName("label_251")
        self.label_530 = QtWidgets.QLabel(self.frame_5)
        self.label_530.setGeometry(QtCore.QRect(167, 301, 71, 25))
        self.label_530.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_530.setText("")
        self.label_530.setAlignment(QtCore.Qt.AlignCenter)
        self.label_530.setObjectName("label_530")
        self.label_414 = QtWidgets.QLabel(self.frame_5)
        self.label_414.setGeometry(QtCore.QRect(677, 209, 45, 25))
        self.label_414.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_414.setText("")
        self.label_414.setAlignment(QtCore.Qt.AlignCenter)
        self.label_414.setObjectName("label_414")
        self.label_222 = QtWidgets.QLabel(self.frame_5)
        self.label_222.setGeometry(QtCore.QRect(677, 25, 45, 25))
        self.label_222.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_222.setText("")
        self.label_222.setAlignment(QtCore.Qt.AlignCenter)
        self.label_222.setObjectName("label_222")
        self.label_525 = QtWidgets.QLabel(self.frame_5)
        self.label_525.setGeometry(QtCore.QRect(1193, 347, 45, 25))
        self.label_525.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_525.setText("")
        self.label_525.setAlignment(QtCore.Qt.AlignCenter)
        self.label_525.setObjectName("label_525")
        self.label_549 = QtWidgets.QLabel(self.frame_5)
        self.label_549.setGeometry(QtCore.QRect(1021, 347, 45, 25))
        self.label_549.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_549.setText("")
        self.label_549.setAlignment(QtCore.Qt.AlignCenter)
        self.label_549.setObjectName("label_549")
        self.label_303 = QtWidgets.QLabel(self.frame_5)
        self.label_303.setGeometry(QtCore.QRect(295, 140, 71, 25))
        self.label_303.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_303.setText("")
        self.label_303.setAlignment(QtCore.Qt.AlignCenter)
        self.label_303.setObjectName("label_303")
        self.label_383 = QtWidgets.QLabel(self.frame_5)
        self.label_383.setGeometry(QtCore.QRect(295, 186, 71, 25))
        self.label_383.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_383.setText("")
        self.label_383.setAlignment(QtCore.Qt.AlignCenter)
        self.label_383.setObjectName("label_383")
        self.label_346 = QtWidgets.QLabel(self.frame_5)
        self.label_346.setGeometry(QtCore.QRect(935, 94, 45, 25))
        self.label_346.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_346.setText("")
        self.label_346.setAlignment(QtCore.Qt.AlignCenter)
        self.label_346.setObjectName("label_346")
        self.label_442 = QtWidgets.QLabel(self.frame_5)
        self.label_442.setGeometry(QtCore.QRect(505, 186, 45, 25))
        self.label_442.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_442.setText("")
        self.label_442.setAlignment(QtCore.Qt.AlignCenter)
        self.label_442.setObjectName("label_442")
        self.label_495 = QtWidgets.QLabel(self.frame_5)
        self.label_495.setGeometry(QtCore.QRect(0, 232, 30, 25))
        self.label_495.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_495.setAlignment(QtCore.Qt.AlignCenter)
        self.label_495.setObjectName("label_495")
        self.label_456 = QtWidgets.QLabel(self.frame_5)
        self.label_456.setGeometry(QtCore.QRect(548, 278, 45, 25))
        self.label_456.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_456.setText("")
        self.label_456.setAlignment(QtCore.Qt.AlignCenter)
        self.label_456.setObjectName("label_456")
        self.label_478 = QtWidgets.QLabel(self.frame_5)
        self.label_478.setGeometry(QtCore.QRect(935, 255, 45, 25))
        self.label_478.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_478.setText("")
        self.label_478.setAlignment(QtCore.Qt.AlignCenter)
        self.label_478.setObjectName("label_478")
        self.label_605 = QtWidgets.QLabel(self.frame_5)
        self.label_605.setGeometry(QtCore.QRect(462, 370, 45, 25))
        self.label_605.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_605.setText("")
        self.label_605.setAlignment(QtCore.Qt.AlignCenter)
        self.label_605.setObjectName("label_605")
        self.label_520 = QtWidgets.QLabel(self.frame_5)
        self.label_520.setGeometry(QtCore.QRect(505, 255, 45, 25))
        self.label_520.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_520.setText("")
        self.label_520.setAlignment(QtCore.Qt.AlignCenter)
        self.label_520.setObjectName("label_520")
        self.label_234 = QtWidgets.QLabel(self.frame_5)
        self.label_234.setGeometry(QtCore.QRect(236, 25, 61, 25))
        self.label_234.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_234.setText("")
        self.label_234.setAlignment(QtCore.Qt.AlignCenter)
        self.label_234.setObjectName("label_234")
        self.label_311 = QtWidgets.QLabel(self.frame_5)
        self.label_311.setGeometry(QtCore.QRect(28, 140, 141, 25))
        self.label_311.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_311.setText("")
        self.label_311.setAlignment(QtCore.Qt.AlignCenter)
        self.label_311.setObjectName("label_311")
        self.label_627 = QtWidgets.QLabel(self.frame_5)
        self.label_627.setGeometry(QtCore.QRect(1150, 370, 45, 25))
        self.label_627.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_627.setText("")
        self.label_627.setAlignment(QtCore.Qt.AlignCenter)
        self.label_627.setObjectName("label_627")
        self.label_297 = QtWidgets.QLabel(self.frame_5)
        self.label_297.setGeometry(QtCore.QRect(364, 140, 51, 25))
        self.label_297.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_297.setText("")
        self.label_297.setAlignment(QtCore.Qt.AlignCenter)
        self.label_297.setObjectName("label_297")
        self.label_207 = QtWidgets.QLabel(self.frame_5)
        self.label_207.setGeometry(QtCore.QRect(935, 2, 45, 25))
        self.label_207.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_207.setAlignment(QtCore.Qt.AlignCenter)
        self.label_207.setObjectName("label_207")
        self.label_225 = QtWidgets.QLabel(self.frame_5)
        self.label_225.setGeometry(QtCore.QRect(462, 25, 45, 25))
        self.label_225.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_225.setText("")
        self.label_225.setAlignment(QtCore.Qt.AlignCenter)
        self.label_225.setObjectName("label_225")
        self.label_489 = QtWidgets.QLabel(self.frame_5)
        self.label_489.setGeometry(QtCore.QRect(1193, 255, 45, 25))
        self.label_489.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_489.setText("")
        self.label_489.setAlignment(QtCore.Qt.AlignCenter)
        self.label_489.setObjectName("label_489")
        self.label_240 = QtWidgets.QLabel(self.frame_5)
        self.label_240.setGeometry(QtCore.QRect(591, 48, 45, 25))
        self.label_240.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_240.setText("")
        self.label_240.setAlignment(QtCore.Qt.AlignCenter)
        self.label_240.setObjectName("label_240")
        self.label_190 = QtWidgets.QLabel(self.frame_5)
        self.label_190.setGeometry(QtCore.QRect(505, 25, 45, 25))
        self.label_190.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_190.setText("")
        self.label_190.setAlignment(QtCore.Qt.AlignCenter)
        self.label_190.setObjectName("label_190")
        self.label_476 = QtWidgets.QLabel(self.frame_5)
        self.label_476.setGeometry(QtCore.QRect(1021, 232, 45, 25))
        self.label_476.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_476.setText("")
        self.label_476.setAlignment(QtCore.Qt.AlignCenter)
        self.label_476.setObjectName("label_476")
        self.label_592 = QtWidgets.QLabel(self.frame_5)
        self.label_592.setGeometry(QtCore.QRect(806, 301, 45, 25))
        self.label_592.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_592.setText("")
        self.label_592.setAlignment(QtCore.Qt.AlignCenter)
        self.label_592.setObjectName("label_592")
        self.label_523 = QtWidgets.QLabel(self.frame_5)
        self.label_523.setGeometry(QtCore.QRect(849, 278, 45, 25))
        self.label_523.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_523.setText("")
        self.label_523.setAlignment(QtCore.Qt.AlignCenter)
        self.label_523.setObjectName("label_523")
        self.label_603 = QtWidgets.QLabel(self.frame_5)
        self.label_603.setGeometry(QtCore.QRect(806, 370, 45, 25))
        self.label_603.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_603.setText("")
        self.label_603.setAlignment(QtCore.Qt.AlignCenter)
        self.label_603.setObjectName("label_603")
        self.label_248 = QtWidgets.QLabel(self.frame_5)
        self.label_248.setGeometry(QtCore.QRect(413, 48, 51, 25))
        self.label_248.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_248.setText("")
        self.label_248.setAlignment(QtCore.Qt.AlignCenter)
        self.label_248.setObjectName("label_248")
        self.label_211 = QtWidgets.QLabel(self.frame_5)
        self.label_211.setGeometry(QtCore.QRect(1193, 2, 45, 25))
        self.label_211.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_211.setAlignment(QtCore.Qt.AlignCenter)
        self.label_211.setObjectName("label_211")
        self.label_488 = QtWidgets.QLabel(self.frame_5)
        self.label_488.setGeometry(QtCore.QRect(1236, 255, 45, 25))
        self.label_488.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_488.setText("")
        self.label_488.setAlignment(QtCore.Qt.AlignCenter)
        self.label_488.setObjectName("label_488")
        self.label_616 = QtWidgets.QLabel(self.frame_5)
        self.label_616.setGeometry(QtCore.QRect(763, 370, 45, 25))
        self.label_616.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_616.setText("")
        self.label_616.setAlignment(QtCore.Qt.AlignCenter)
        self.label_616.setObjectName("label_616")
        self.label_453 = QtWidgets.QLabel(self.frame_5)
        self.label_453.setGeometry(QtCore.QRect(364, 278, 51, 25))
        self.label_453.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_453.setText("")
        self.label_453.setAlignment(QtCore.Qt.AlignCenter)
        self.label_453.setObjectName("label_453")
        self.label_429 = QtWidgets.QLabel(self.frame_5)
        self.label_429.setGeometry(QtCore.QRect(236, 186, 61, 25))
        self.label_429.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_429.setText("")
        self.label_429.setAlignment(QtCore.Qt.AlignCenter)
        self.label_429.setObjectName("label_429")
        self.label_610 = QtWidgets.QLabel(self.frame_5)
        self.label_610.setGeometry(QtCore.QRect(677, 370, 45, 25))
        self.label_610.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_610.setText("")
        self.label_610.setAlignment(QtCore.Qt.AlignCenter)
        self.label_610.setObjectName("label_610")
        self.label_220 = QtWidgets.QLabel(self.frame_5)
        self.label_220.setGeometry(QtCore.QRect(935, 25, 45, 25))
        self.label_220.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_220.setText("")
        self.label_220.setAlignment(QtCore.Qt.AlignCenter)
        self.label_220.setObjectName("label_220")
        self.label_338 = QtWidgets.QLabel(self.frame_5)
        self.label_338.setGeometry(QtCore.QRect(978, 140, 45, 25))
        self.label_338.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_338.setText("")
        self.label_338.setAlignment(QtCore.Qt.AlignCenter)
        self.label_338.setObjectName("label_338")
        self.label_469 = QtWidgets.QLabel(self.frame_5)
        self.label_469.setGeometry(QtCore.QRect(462, 232, 45, 25))
        self.label_469.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_469.setText("")
        self.label_469.setAlignment(QtCore.Qt.AlignCenter)
        self.label_469.setObjectName("label_469")
        self.label_349 = QtWidgets.QLabel(self.frame_5)
        self.label_349.setGeometry(QtCore.QRect(1193, 94, 45, 25))
        self.label_349.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_349.setText("")
        self.label_349.setAlignment(QtCore.Qt.AlignCenter)
        self.label_349.setObjectName("label_349")
        self.label_623 = QtWidgets.QLabel(self.frame_5)
        self.label_623.setGeometry(QtCore.QRect(935, 370, 45, 25))
        self.label_623.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_623.setText("")
        self.label_623.setAlignment(QtCore.Qt.AlignCenter)
        self.label_623.setObjectName("label_623")
        self.label_567 = QtWidgets.QLabel(self.frame_5)
        self.label_567.setGeometry(QtCore.QRect(1193, 324, 45, 25))
        self.label_567.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_567.setText("")
        self.label_567.setAlignment(QtCore.Qt.AlignCenter)
        self.label_567.setObjectName("label_567")
        self.label_437 = QtWidgets.QLabel(self.frame_5)
        self.label_437.setGeometry(QtCore.QRect(0, 209, 30, 25))
        self.label_437.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_437.setAlignment(QtCore.Qt.AlignCenter)
        self.label_437.setObjectName("label_437")
        self.label_600 = QtWidgets.QLabel(self.frame_5)
        self.label_600.setGeometry(QtCore.QRect(591, 301, 45, 25))
        self.label_600.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_600.setText("")
        self.label_600.setAlignment(QtCore.Qt.AlignCenter)
        self.label_600.setObjectName("label_600")
        self.label_619 = QtWidgets.QLabel(self.frame_5)
        self.label_619.setGeometry(QtCore.QRect(0, 370, 30, 25))
        self.label_619.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_619.setAlignment(QtCore.Qt.AlignCenter)
        self.label_619.setObjectName("label_619")
        self.label_606 = QtWidgets.QLabel(self.frame_5)
        self.label_606.setGeometry(QtCore.QRect(591, 370, 45, 25))
        self.label_606.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_606.setText("")
        self.label_606.setAlignment(QtCore.Qt.AlignCenter)
        self.label_606.setObjectName("label_606")
        self.label_482 = QtWidgets.QLabel(self.frame_5)
        self.label_482.setGeometry(QtCore.QRect(849, 232, 45, 25))
        self.label_482.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_482.setText("")
        self.label_482.setAlignment(QtCore.Qt.AlignCenter)
        self.label_482.setObjectName("label_482")
        self.label_319 = QtWidgets.QLabel(self.frame_5)
        self.label_319.setGeometry(QtCore.QRect(1236, 140, 45, 25))
        self.label_319.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_319.setText("")
        self.label_319.setAlignment(QtCore.Qt.AlignCenter)
        self.label_319.setObjectName("label_319")
        self.label_501 = QtWidgets.QLabel(self.frame_5)
        self.label_501.setGeometry(QtCore.QRect(892, 278, 45, 25))
        self.label_501.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_501.setText("")
        self.label_501.setAlignment(QtCore.Qt.AlignCenter)
        self.label_501.setObjectName("label_501")
        self.label_444 = QtWidgets.QLabel(self.frame_5)
        self.label_444.setGeometry(QtCore.QRect(591, 163, 45, 25))
        self.label_444.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_444.setText("")
        self.label_444.setAlignment(QtCore.Qt.AlignCenter)
        self.label_444.setObjectName("label_444")
        self.label_216 = QtWidgets.QLabel(self.frame_5)
        self.label_216.setGeometry(QtCore.QRect(763, 25, 45, 25))
        self.label_216.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_216.setText("")
        self.label_216.setAlignment(QtCore.Qt.AlignCenter)
        self.label_216.setObjectName("label_216")
        self.label_385 = QtWidgets.QLabel(self.frame_5)
        self.label_385.setGeometry(QtCore.QRect(364, 163, 51, 25))
        self.label_385.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_385.setText("")
        self.label_385.setAlignment(QtCore.Qt.AlignCenter)
        self.label_385.setObjectName("label_385")
        self.label_380 = QtWidgets.QLabel(self.frame_5)
        self.label_380.setGeometry(QtCore.QRect(591, 186, 45, 25))
        self.label_380.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_380.setText("")
        self.label_380.setAlignment(QtCore.Qt.AlignCenter)
        self.label_380.setObjectName("label_380")
        self.label_513 = QtWidgets.QLabel(self.frame_5)
        self.label_513.setGeometry(QtCore.QRect(413, 255, 51, 25))
        self.label_513.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_513.setText("")
        self.label_513.setAlignment(QtCore.Qt.AlignCenter)
        self.label_513.setObjectName("label_513")
        self.label_351 = QtWidgets.QLabel(self.frame_5)
        self.label_351.setGeometry(QtCore.QRect(236, 117, 61, 25))
        self.label_351.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_351.setText("")
        self.label_351.setAlignment(QtCore.Qt.AlignCenter)
        self.label_351.setObjectName("label_351")
        self.label_344 = QtWidgets.QLabel(self.frame_5)
        self.label_344.setGeometry(QtCore.QRect(892, 117, 45, 25))
        self.label_344.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_344.setText("")
        self.label_344.setAlignment(QtCore.Qt.AlignCenter)
        self.label_344.setObjectName("label_344")
        self.label_272 = QtWidgets.QLabel(self.frame_5)
        self.label_272.setGeometry(QtCore.QRect(1021, 71, 45, 25))
        self.label_272.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_272.setText("")
        self.label_272.setAlignment(QtCore.Qt.AlignCenter)
        self.label_272.setObjectName("label_272")
        self.label_421 = QtWidgets.QLabel(self.frame_5)
        self.label_421.setGeometry(QtCore.QRect(634, 186, 45, 25))
        self.label_421.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_421.setText("")
        self.label_421.setAlignment(QtCore.Qt.AlignCenter)
        self.label_421.setObjectName("label_421")
        self.label_281 = QtWidgets.QLabel(self.frame_5)
        self.label_281.setGeometry(QtCore.QRect(1236, 71, 45, 25))
        self.label_281.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_281.setText("")
        self.label_281.setAlignment(QtCore.Qt.AlignCenter)
        self.label_281.setObjectName("label_281")
        self.label_232 = QtWidgets.QLabel(self.frame_5)
        self.label_232.setGeometry(QtCore.QRect(892, 25, 45, 25))
        self.label_232.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_232.setText("")
        self.label_232.setAlignment(QtCore.Qt.AlignCenter)
        self.label_232.setObjectName("label_232")
        self.label_450 = QtWidgets.QLabel(self.frame_5)
        self.label_450.setGeometry(QtCore.QRect(1107, 255, 45, 25))
        self.label_450.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_450.setText("")
        self.label_450.setAlignment(QtCore.Qt.AlignCenter)
        self.label_450.setObjectName("label_450")
        self.label_541 = QtWidgets.QLabel(self.frame_5)
        self.label_541.setGeometry(QtCore.QRect(364, 301, 51, 25))
        self.label_541.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_541.setText("")
        self.label_541.setAlignment(QtCore.Qt.AlignCenter)
        self.label_541.setObjectName("label_541")
        self.label_218 = QtWidgets.QLabel(self.frame_5)
        self.label_218.setGeometry(QtCore.QRect(978, 25, 45, 25))
        self.label_218.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_218.setText("")
        self.label_218.setAlignment(QtCore.Qt.AlignCenter)
        self.label_218.setObjectName("label_218")
        self.label_212 = QtWidgets.QLabel(self.frame_5)
        self.label_212.setGeometry(QtCore.QRect(1064, 2, 45, 25))
        self.label_212.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_212.setAlignment(QtCore.Qt.AlignCenter)
        self.label_212.setObjectName("label_212")
        self.label_335 = QtWidgets.QLabel(self.frame_5)
        self.label_335.setGeometry(QtCore.QRect(677, 94, 45, 25))
        self.label_335.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_335.setText("")
        self.label_335.setAlignment(QtCore.Qt.AlignCenter)
        self.label_335.setObjectName("label_335")
        self.label_529 = QtWidgets.QLabel(self.frame_5)
        self.label_529.setGeometry(QtCore.QRect(1107, 347, 45, 25))
        self.label_529.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_529.setText("")
        self.label_529.setAlignment(QtCore.Qt.AlignCenter)
        self.label_529.setObjectName("label_529")
        self.label_607 = QtWidgets.QLabel(self.frame_5)
        self.label_607.setGeometry(QtCore.QRect(28, 370, 141, 25))
        self.label_607.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_607.setText("")
        self.label_607.setAlignment(QtCore.Qt.AlignCenter)
        self.label_607.setObjectName("label_607")
        self.label_470 = QtWidgets.QLabel(self.frame_5)
        self.label_470.setGeometry(QtCore.QRect(295, 232, 71, 25))
        self.label_470.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_470.setText("")
        self.label_470.setAlignment(QtCore.Qt.AlignCenter)
        self.label_470.setObjectName("label_470")
        self.label_465 = QtWidgets.QLabel(self.frame_5)
        self.label_465.setGeometry(QtCore.QRect(634, 232, 45, 25))
        self.label_465.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_465.setText("")
        self.label_465.setAlignment(QtCore.Qt.AlignCenter)
        self.label_465.setObjectName("label_465")
        self.label_528 = QtWidgets.QLabel(self.frame_5)
        self.label_528.setGeometry(QtCore.QRect(1107, 324, 45, 25))
        self.label_528.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_528.setText("")
        self.label_528.setAlignment(QtCore.Qt.AlignCenter)
        self.label_528.setObjectName("label_528")
        self.label_491 = QtWidgets.QLabel(self.frame_5)
        self.label_491.setGeometry(QtCore.QRect(677, 232, 45, 25))
        self.label_491.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_491.setText("")
        self.label_491.setAlignment(QtCore.Qt.AlignCenter)
        self.label_491.setObjectName("label_491")
        self.label_327 = QtWidgets.QLabel(self.frame_5)
        self.label_327.setGeometry(QtCore.QRect(462, 140, 45, 25))
        self.label_327.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_327.setText("")
        self.label_327.setAlignment(QtCore.Qt.AlignCenter)
        self.label_327.setObjectName("label_327")
        self.label_540 = QtWidgets.QLabel(self.frame_5)
        self.label_540.setGeometry(QtCore.QRect(364, 324, 51, 25))
        self.label_540.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_540.setText("")
        self.label_540.setAlignment(QtCore.Qt.AlignCenter)
        self.label_540.setObjectName("label_540")
        self.label_589 = QtWidgets.QLabel(self.frame_5)
        self.label_589.setGeometry(QtCore.QRect(548, 324, 45, 25))
        self.label_589.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_589.setText("")
        self.label_589.setAlignment(QtCore.Qt.AlignCenter)
        self.label_589.setObjectName("label_589")
        self.label_400 = QtWidgets.QLabel(self.frame_5)
        self.label_400.setGeometry(QtCore.QRect(935, 186, 45, 25))
        self.label_400.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_400.setText("")
        self.label_400.setAlignment(QtCore.Qt.AlignCenter)
        self.label_400.setObjectName("label_400")
        self.label_358 = QtWidgets.QLabel(self.frame_5)
        self.label_358.setGeometry(QtCore.QRect(806, 94, 45, 25))
        self.label_358.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_358.setText("")
        self.label_358.setAlignment(QtCore.Qt.AlignCenter)
        self.label_358.setObjectName("label_358")
        self.label_440 = QtWidgets.QLabel(self.frame_5)
        self.label_440.setGeometry(QtCore.QRect(1236, 163, 45, 25))
        self.label_440.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_440.setText("")
        self.label_440.setAlignment(QtCore.Qt.AlignCenter)
        self.label_440.setObjectName("label_440")
        self.label_597 = QtWidgets.QLabel(self.frame_5)
        self.label_597.setGeometry(QtCore.QRect(892, 301, 45, 25))
        self.label_597.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_597.setText("")
        self.label_597.setAlignment(QtCore.Qt.AlignCenter)
        self.label_597.setObjectName("label_597")
        self.label_202 = QtWidgets.QLabel(self.frame_5)
        self.label_202.setGeometry(QtCore.QRect(167, 2, 71, 25))
        self.label_202.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)\n"
"")
        self.label_202.setText("")
        self.label_202.setAlignment(QtCore.Qt.AlignCenter)
        self.label_202.setObjectName("label_202")
        self.label_509 = QtWidgets.QLabel(self.frame_5)
        self.label_509.setGeometry(QtCore.QRect(0, 255, 30, 25))
        self.label_509.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_509.setAlignment(QtCore.Qt.AlignCenter)
        self.label_509.setObjectName("label_509")
        self.label_241 = QtWidgets.QLabel(self.frame_5)
        self.label_241.setGeometry(QtCore.QRect(935, 48, 45, 25))
        self.label_241.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_241.setText("")
        self.label_241.setAlignment(QtCore.Qt.AlignCenter)
        self.label_241.setObjectName("label_241")
        self.label_242 = QtWidgets.QLabel(self.frame_5)
        self.label_242.setGeometry(QtCore.QRect(978, 48, 45, 25))
        self.label_242.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_242.setText("")
        self.label_242.setAlignment(QtCore.Qt.AlignCenter)
        self.label_242.setObjectName("label_242")
        self.label_191 = QtWidgets.QLabel(self.frame_5)
        self.label_191.setGeometry(QtCore.QRect(295, 25, 71, 25))
        self.label_191.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_191.setText("")
        self.label_191.setAlignment(QtCore.Qt.AlignCenter)
        self.label_191.setObjectName("label_191")
        self.label_318 = QtWidgets.QLabel(self.frame_5)
        self.label_318.setGeometry(QtCore.QRect(1064, 140, 45, 25))
        self.label_318.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_318.setText("")
        self.label_318.setAlignment(QtCore.Qt.AlignCenter)
        self.label_318.setObjectName("label_318")
        self.label_223 = QtWidgets.QLabel(self.frame_5)
        self.label_223.setGeometry(QtCore.QRect(720, 25, 45, 25))
        self.label_223.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_223.setText("")
        self.label_223.setAlignment(QtCore.Qt.AlignCenter)
        self.label_223.setObjectName("label_223")
        self.label_373 = QtWidgets.QLabel(self.frame_5)
        self.label_373.setGeometry(QtCore.QRect(1107, 209, 45, 25))
        self.label_373.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_373.setText("")
        self.label_373.setAlignment(QtCore.Qt.AlignCenter)
        self.label_373.setObjectName("label_373")
        self.label_425 = QtWidgets.QLabel(self.frame_5)
        self.label_425.setGeometry(QtCore.QRect(720, 186, 45, 25))
        self.label_425.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_425.setText("")
        self.label_425.setAlignment(QtCore.Qt.AlignCenter)
        self.label_425.setObjectName("label_425")
        self.label_417 = QtWidgets.QLabel(self.frame_5)
        self.label_417.setGeometry(QtCore.QRect(0, 163, 30, 25))
        self.label_417.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_417.setAlignment(QtCore.Qt.AlignCenter)
        self.label_417.setObjectName("label_417")
        self.label_313 = QtWidgets.QLabel(self.frame_5)
        self.label_313.setGeometry(QtCore.QRect(462, 94, 45, 25))
        self.label_313.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_313.setText("")
        self.label_313.setAlignment(QtCore.Qt.AlignCenter)
        self.label_313.setObjectName("label_313")
        self.label_599 = QtWidgets.QLabel(self.frame_5)
        self.label_599.setGeometry(QtCore.QRect(413, 301, 51, 25))
        self.label_599.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_599.setText("")
        self.label_599.setAlignment(QtCore.Qt.AlignCenter)
        self.label_599.setObjectName("label_599")
        self.label_614 = QtWidgets.QLabel(self.frame_5)
        self.label_614.setGeometry(QtCore.QRect(849, 370, 45, 25))
        self.label_614.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_614.setText("")
        self.label_614.setAlignment(QtCore.Qt.AlignCenter)
        self.label_614.setObjectName("label_614")
        self.label_386 = QtWidgets.QLabel(self.frame_5)
        self.label_386.setGeometry(QtCore.QRect(167, 209, 71, 25))
        self.label_386.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_386.setText("")
        self.label_386.setAlignment(QtCore.Qt.AlignCenter)
        self.label_386.setObjectName("label_386")
        self.label_187 = QtWidgets.QLabel(self.frame_5)
        self.label_187.setGeometry(QtCore.QRect(892, 2, 45, 25))
        self.label_187.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_187.setAlignment(QtCore.Qt.AlignCenter)
        self.label_187.setObjectName("label_187")
        self.label_259 = QtWidgets.QLabel(self.frame_5)
        self.label_259.setGeometry(QtCore.QRect(167, 48, 71, 25))
        self.label_259.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_259.setText("")
        self.label_259.setAlignment(QtCore.Qt.AlignCenter)
        self.label_259.setObjectName("label_259")
        self.label_608 = QtWidgets.QLabel(self.frame_5)
        self.label_608.setGeometry(QtCore.QRect(720, 370, 45, 25))
        self.label_608.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_608.setText("")
        self.label_608.setAlignment(QtCore.Qt.AlignCenter)
        self.label_608.setObjectName("label_608")
        self.label_497 = QtWidgets.QLabel(self.frame_5)
        self.label_497.setGeometry(QtCore.QRect(935, 278, 45, 25))
        self.label_497.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_497.setText("")
        self.label_497.setAlignment(QtCore.Qt.AlignCenter)
        self.label_497.setObjectName("label_497")
        self.label_284 = QtWidgets.QLabel(self.frame_5)
        self.label_284.setGeometry(QtCore.QRect(1150, 71, 45, 25))
        self.label_284.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_284.setText("")
        self.label_284.setAlignment(QtCore.Qt.AlignCenter)
        self.label_284.setObjectName("label_284")
        self.label_391 = QtWidgets.QLabel(self.frame_5)
        self.label_391.setGeometry(QtCore.QRect(462, 163, 45, 25))
        self.label_391.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_391.setText("")
        self.label_391.setAlignment(QtCore.Qt.AlignCenter)
        self.label_391.setObjectName("label_391")
        self.label_411 = QtWidgets.QLabel(self.frame_5)
        self.label_411.setGeometry(QtCore.QRect(1193, 186, 45, 25))
        self.label_411.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_411.setText("")
        self.label_411.setAlignment(QtCore.Qt.AlignCenter)
        self.label_411.setObjectName("label_411")
        self.label_591 = QtWidgets.QLabel(self.frame_5)
        self.label_591.setGeometry(QtCore.QRect(413, 324, 51, 25))
        self.label_591.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_591.setText("")
        self.label_591.setAlignment(QtCore.Qt.AlignCenter)
        self.label_591.setObjectName("label_591")
        self.label_330 = QtWidgets.QLabel(self.frame_5)
        self.label_330.setGeometry(QtCore.QRect(806, 117, 45, 25))
        self.label_330.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_330.setText("")
        self.label_330.setAlignment(QtCore.Qt.AlignCenter)
        self.label_330.setObjectName("label_330")
        self.label_621 = QtWidgets.QLabel(self.frame_5)
        self.label_621.setGeometry(QtCore.QRect(1107, 370, 45, 25))
        self.label_621.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_621.setText("")
        self.label_621.setAlignment(QtCore.Qt.AlignCenter)
        self.label_621.setObjectName("label_621")
        self.label_361 = QtWidgets.QLabel(self.frame_5)
        self.label_361.setGeometry(QtCore.QRect(763, 117, 45, 25))
        self.label_361.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_361.setText("")
        self.label_361.setAlignment(QtCore.Qt.AlignCenter)
        self.label_361.setObjectName("label_361")
        self.label_333 = QtWidgets.QLabel(self.frame_5)
        self.label_333.setGeometry(QtCore.QRect(1193, 117, 45, 25))
        self.label_333.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_333.setText("")
        self.label_333.setAlignment(QtCore.Qt.AlignCenter)
        self.label_333.setObjectName("label_333")
        self.label_357 = QtWidgets.QLabel(self.frame_5)
        self.label_357.setGeometry(QtCore.QRect(413, 117, 51, 25))
        self.label_357.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_357.setText("")
        self.label_357.setAlignment(QtCore.Qt.AlignCenter)
        self.label_357.setObjectName("label_357")
        self.label_494 = QtWidgets.QLabel(self.frame_5)
        self.label_494.setGeometry(QtCore.QRect(978, 278, 45, 25))
        self.label_494.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_494.setText("")
        self.label_494.setAlignment(QtCore.Qt.AlignCenter)
        self.label_494.setObjectName("label_494")
        self.label_306 = QtWidgets.QLabel(self.frame_5)
        self.label_306.setGeometry(QtCore.QRect(364, 117, 51, 25))
        self.label_306.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_306.setText("")
        self.label_306.setAlignment(QtCore.Qt.AlignCenter)
        self.label_306.setObjectName("label_306")
        self.label_276 = QtWidgets.QLabel(self.frame_5)
        self.label_276.setGeometry(QtCore.QRect(1107, 71, 45, 25))
        self.label_276.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_276.setText("")
        self.label_276.setAlignment(QtCore.Qt.AlignCenter)
        self.label_276.setObjectName("label_276")
        self.label_531 = QtWidgets.QLabel(self.frame_5)
        self.label_531.setGeometry(QtCore.QRect(364, 347, 51, 25))
        self.label_531.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_531.setText("")
        self.label_531.setAlignment(QtCore.Qt.AlignCenter)
        self.label_531.setObjectName("label_531")
        self.label_577 = QtWidgets.QLabel(self.frame_5)
        self.label_577.setGeometry(QtCore.QRect(634, 324, 45, 25))
        self.label_577.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_577.setText("")
        self.label_577.setAlignment(QtCore.Qt.AlignCenter)
        self.label_577.setObjectName("label_577")
        self.label_416 = QtWidgets.QLabel(self.frame_5)
        self.label_416.setGeometry(QtCore.QRect(978, 209, 45, 25))
        self.label_416.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_416.setText("")
        self.label_416.setAlignment(QtCore.Qt.AlignCenter)
        self.label_416.setObjectName("label_416")
        self.label_253 = QtWidgets.QLabel(self.frame_5)
        self.label_253.setGeometry(QtCore.QRect(295, 48, 71, 25))
        self.label_253.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_253.setText("")
        self.label_253.setAlignment(QtCore.Qt.AlignCenter)
        self.label_253.setObjectName("label_253")
        self.label_293 = QtWidgets.QLabel(self.frame_5)
        self.label_293.setGeometry(QtCore.QRect(505, 94, 45, 25))
        self.label_293.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_293.setText("")
        self.label_293.setAlignment(QtCore.Qt.AlignCenter)
        self.label_293.setObjectName("label_293")
        self.label_492 = QtWidgets.QLabel(self.frame_5)
        self.label_492.setGeometry(QtCore.QRect(677, 278, 45, 25))
        self.label_492.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_492.setText("")
        self.label_492.setAlignment(QtCore.Qt.AlignCenter)
        self.label_492.setObjectName("label_492")
        self.label_585 = QtWidgets.QLabel(self.frame_5)
        self.label_585.setGeometry(QtCore.QRect(236, 324, 61, 25))
        self.label_585.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_585.setText("")
        self.label_585.setAlignment(QtCore.Qt.AlignCenter)
        self.label_585.setObjectName("label_585")
        self.label_571 = QtWidgets.QLabel(self.frame_5)
        self.label_571.setGeometry(QtCore.QRect(236, 301, 61, 25))
        self.label_571.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_571.setText("")
        self.label_571.setAlignment(QtCore.Qt.AlignCenter)
        self.label_571.setObjectName("label_571")
        self.label_315 = QtWidgets.QLabel(self.frame_5)
        self.label_315.setGeometry(QtCore.QRect(1021, 140, 45, 25))
        self.label_315.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_315.setText("")
        self.label_315.setAlignment(QtCore.Qt.AlignCenter)
        self.label_315.setObjectName("label_315")
        self.label_574 = QtWidgets.QLabel(self.frame_5)
        self.label_574.setGeometry(QtCore.QRect(167, 324, 71, 25))
        self.label_574.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_574.setText("")
        self.label_574.setAlignment(QtCore.Qt.AlignCenter)
        self.label_574.setObjectName("label_574")
        self.label_535 = QtWidgets.QLabel(self.frame_5)
        self.label_535.setGeometry(QtCore.QRect(720, 347, 45, 25))
        self.label_535.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_535.setText("")
        self.label_535.setAlignment(QtCore.Qt.AlignCenter)
        self.label_535.setObjectName("label_535")
        self.label_547 = QtWidgets.QLabel(self.frame_5)
        self.label_547.setGeometry(QtCore.QRect(462, 301, 45, 25))
        self.label_547.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_547.setText("")
        self.label_547.setAlignment(QtCore.Qt.AlignCenter)
        self.label_547.setObjectName("label_547")
        self.label_390 = QtWidgets.QLabel(self.frame_5)
        self.label_390.setGeometry(QtCore.QRect(1107, 163, 45, 25))
        self.label_390.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_390.setText("")
        self.label_390.setAlignment(QtCore.Qt.AlignCenter)
        self.label_390.setObjectName("label_390")
        self.label_471 = QtWidgets.QLabel(self.frame_5)
        self.label_471.setGeometry(QtCore.QRect(1021, 278, 45, 25))
        self.label_471.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_471.setText("")
        self.label_471.setAlignment(QtCore.Qt.AlignCenter)
        self.label_471.setObjectName("label_471")
        self.label_292 = QtWidgets.QLabel(self.frame_5)
        self.label_292.setGeometry(QtCore.QRect(806, 140, 45, 25))
        self.label_292.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_292.setText("")
        self.label_292.setAlignment(QtCore.Qt.AlignCenter)
        self.label_292.setObjectName("label_292")
        self.label_340 = QtWidgets.QLabel(self.frame_5)
        self.label_340.setGeometry(QtCore.QRect(167, 117, 71, 25))
        self.label_340.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_340.setText("")
        self.label_340.setAlignment(QtCore.Qt.AlignCenter)
        self.label_340.setObjectName("label_340")
        self.label_467 = QtWidgets.QLabel(self.frame_5)
        self.label_467.setGeometry(QtCore.QRect(28, 278, 141, 25))
        self.label_467.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_467.setText("")
        self.label_467.setAlignment(QtCore.Qt.AlignCenter)
        self.label_467.setObjectName("label_467")
        self.label_490 = QtWidgets.QLabel(self.frame_5)
        self.label_490.setGeometry(QtCore.QRect(720, 232, 45, 25))
        self.label_490.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_490.setText("")
        self.label_490.setAlignment(QtCore.Qt.AlignCenter)
        self.label_490.setObjectName("label_490")
        self.label_560 = QtWidgets.QLabel(self.frame_5)
        self.label_560.setGeometry(QtCore.QRect(849, 301, 45, 25))
        self.label_560.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_560.setText("")
        self.label_560.setAlignment(QtCore.Qt.AlignCenter)
        self.label_560.setObjectName("label_560")
        self.label_626 = QtWidgets.QLabel(self.frame_5)
        self.label_626.setGeometry(QtCore.QRect(634, 370, 45, 25))
        self.label_626.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_626.setText("")
        self.label_626.setAlignment(QtCore.Qt.AlignCenter)
        self.label_626.setObjectName("label_626")
        self.label_322 = QtWidgets.QLabel(self.frame_5)
        self.label_322.setGeometry(QtCore.QRect(935, 117, 45, 25))
        self.label_322.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_322.setText("")
        self.label_322.setAlignment(QtCore.Qt.AlignCenter)
        self.label_322.setObjectName("label_322")
        self.label_194 = QtWidgets.QLabel(self.frame_5)
        self.label_194.setGeometry(QtCore.QRect(591, 25, 45, 25))
        self.label_194.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_194.setText("")
        self.label_194.setAlignment(QtCore.Qt.AlignCenter)
        self.label_194.setObjectName("label_194")
        self.label_542 = QtWidgets.QLabel(self.frame_5)
        self.label_542.setGeometry(QtCore.QRect(167, 347, 71, 25))
        self.label_542.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_542.setText("")
        self.label_542.setAlignment(QtCore.Qt.AlignCenter)
        self.label_542.setObjectName("label_542")
        self.label_371 = QtWidgets.QLabel(self.frame_5)
        self.label_371.setGeometry(QtCore.QRect(505, 163, 45, 25))
        self.label_371.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_371.setText("")
        self.label_371.setAlignment(QtCore.Qt.AlignCenter)
        self.label_371.setObjectName("label_371")
        self.label_485 = QtWidgets.QLabel(self.frame_5)
        self.label_485.setGeometry(QtCore.QRect(462, 255, 45, 25))
        self.label_485.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_485.setText("")
        self.label_485.setAlignment(QtCore.Qt.AlignCenter)
        self.label_485.setObjectName("label_485")
        self.label_236 = QtWidgets.QLabel(self.frame_5)
        self.label_236.setGeometry(QtCore.QRect(634, 2, 45, 25))
        self.label_236.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_236.setAlignment(QtCore.Qt.AlignCenter)
        self.label_236.setObjectName("label_236")
        self.label_524 = QtWidgets.QLabel(self.frame_5)
        self.label_524.setGeometry(QtCore.QRect(1064, 232, 45, 25))
        self.label_524.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_524.setText("")
        self.label_524.setAlignment(QtCore.Qt.AlignCenter)
        self.label_524.setObjectName("label_524")
        self.label_481 = QtWidgets.QLabel(self.frame_5)
        self.label_481.setGeometry(QtCore.QRect(677, 255, 45, 25))
        self.label_481.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_481.setText("")
        self.label_481.setAlignment(QtCore.Qt.AlignCenter)
        self.label_481.setObjectName("label_481")
        self.label_301 = QtWidgets.QLabel(self.frame_5)
        self.label_301.setGeometry(QtCore.QRect(720, 140, 45, 25))
        self.label_301.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_301.setText("")
        self.label_301.setAlignment(QtCore.Qt.AlignCenter)
        self.label_301.setObjectName("label_301")
        self.label_370 = QtWidgets.QLabel(self.frame_5)
        self.label_370.setGeometry(QtCore.QRect(806, 209, 45, 25))
        self.label_370.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_370.setText("")
        self.label_370.setAlignment(QtCore.Qt.AlignCenter)
        self.label_370.setObjectName("label_370")
        self.label_568 = QtWidgets.QLabel(self.frame_5)
        self.label_568.setGeometry(QtCore.QRect(720, 301, 45, 25))
        self.label_568.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_568.setText("")
        self.label_568.setAlignment(QtCore.Qt.AlignCenter)
        self.label_568.setObjectName("label_568")
        self.label_519 = QtWidgets.QLabel(self.frame_5)
        self.label_519.setGeometry(QtCore.QRect(892, 232, 45, 25))
        self.label_519.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_519.setText("")
        self.label_519.setAlignment(QtCore.Qt.AlignCenter)
        self.label_519.setObjectName("label_519")
        self.label_246 = QtWidgets.QLabel(self.frame_5)
        self.label_246.setGeometry(QtCore.QRect(763, 48, 45, 25))
        self.label_246.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_246.setText("")
        self.label_246.setAlignment(QtCore.Qt.AlignCenter)
        self.label_246.setObjectName("label_246")
        self.label_586 = QtWidgets.QLabel(self.frame_5)
        self.label_586.setGeometry(QtCore.QRect(1064, 324, 45, 25))
        self.label_586.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_586.setText("")
        self.label_586.setAlignment(QtCore.Qt.AlignCenter)
        self.label_586.setObjectName("label_586")
        self.label_581 = QtWidgets.QLabel(self.frame_5)
        self.label_581.setGeometry(QtCore.QRect(720, 324, 45, 25))
        self.label_581.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_581.setText("")
        self.label_581.setAlignment(QtCore.Qt.AlignCenter)
        self.label_581.setObjectName("label_581")
        self.label_323 = QtWidgets.QLabel(self.frame_5)
        self.label_323.setGeometry(QtCore.QRect(1150, 94, 45, 25))
        self.label_323.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_323.setText("")
        self.label_323.setAlignment(QtCore.Qt.AlignCenter)
        self.label_323.setObjectName("label_323")
        self.label_517 = QtWidgets.QLabel(self.frame_5)
        self.label_517.setGeometry(QtCore.QRect(763, 255, 45, 25))
        self.label_517.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_517.setText("")
        self.label_517.setAlignment(QtCore.Qt.AlignCenter)
        self.label_517.setObjectName("label_517")
        self.label_350 = QtWidgets.QLabel(self.frame_5)
        self.label_350.setGeometry(QtCore.QRect(634, 140, 45, 25))
        self.label_350.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_350.setText("")
        self.label_350.setAlignment(QtCore.Qt.AlignCenter)
        self.label_350.setObjectName("label_350")
        self.label_205 = QtWidgets.QLabel(self.frame_5)
        self.label_205.setGeometry(QtCore.QRect(849, 25, 45, 25))
        self.label_205.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_205.setText("")
        self.label_205.setAlignment(QtCore.Qt.AlignCenter)
        self.label_205.setObjectName("label_205")
        self.label_455 = QtWidgets.QLabel(self.frame_5)
        self.label_455.setGeometry(QtCore.QRect(763, 278, 45, 25))
        self.label_455.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_455.setText("")
        self.label_455.setAlignment(QtCore.Qt.AlignCenter)
        self.label_455.setObjectName("label_455")
        self.label_562 = QtWidgets.QLabel(self.frame_5)
        self.label_562.setGeometry(QtCore.QRect(978, 324, 45, 25))
        self.label_562.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_562.setText("")
        self.label_562.setAlignment(QtCore.Qt.AlignCenter)
        self.label_562.setObjectName("label_562")
        self.label_451 = QtWidgets.QLabel(self.frame_5)
        self.label_451.setGeometry(QtCore.QRect(1107, 278, 45, 25))
        self.label_451.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_451.setText("")
        self.label_451.setAlignment(QtCore.Qt.AlignCenter)
        self.label_451.setObjectName("label_451")
        self.label_483 = QtWidgets.QLabel(self.frame_5)
        self.label_483.setGeometry(QtCore.QRect(462, 278, 45, 25))
        self.label_483.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_483.setText("")
        self.label_483.setAlignment(QtCore.Qt.AlignCenter)
        self.label_483.setObjectName("label_483")
        self.label_505 = QtWidgets.QLabel(self.frame_5)
        self.label_505.setGeometry(QtCore.QRect(1193, 232, 45, 25))
        self.label_505.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_505.setText("")
        self.label_505.setAlignment(QtCore.Qt.AlignCenter)
        self.label_505.setObjectName("label_505")
        self.label_389 = QtWidgets.QLabel(self.frame_5)
        self.label_389.setGeometry(QtCore.QRect(28, 209, 141, 25))
        self.label_389.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_389.setText("")
        self.label_389.setAlignment(QtCore.Qt.AlignCenter)
        self.label_389.setObjectName("label_389")
        self.label_545 = QtWidgets.QLabel(self.frame_5)
        self.label_545.setGeometry(QtCore.QRect(28, 347, 141, 25))
        self.label_545.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_545.setText("")
        self.label_545.setAlignment(QtCore.Qt.AlignCenter)
        self.label_545.setObjectName("label_545")
        self.label_514 = QtWidgets.QLabel(self.frame_5)
        self.label_514.setGeometry(QtCore.QRect(806, 232, 45, 25))
        self.label_514.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_514.setText("")
        self.label_514.setAlignment(QtCore.Qt.AlignCenter)
        self.label_514.setObjectName("label_514")
        self.label_399 = QtWidgets.QLabel(self.frame_5)
        self.label_399.setGeometry(QtCore.QRect(413, 209, 51, 25))
        self.label_399.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_399.setText("")
        self.label_399.setAlignment(QtCore.Qt.AlignCenter)
        self.label_399.setObjectName("label_399")
        self.label_314 = QtWidgets.QLabel(self.frame_5)
        self.label_314.setGeometry(QtCore.QRect(295, 94, 71, 25))
        self.label_314.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_314.setText("")
        self.label_314.setAlignment(QtCore.Qt.AlignCenter)
        self.label_314.setObjectName("label_314")
        self.label_426 = QtWidgets.QLabel(self.frame_5)
        self.label_426.setGeometry(QtCore.QRect(978, 163, 45, 25))
        self.label_426.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_426.setText("")
        self.label_426.setAlignment(QtCore.Qt.AlignCenter)
        self.label_426.setObjectName("label_426")
        self.label_201 = QtWidgets.QLabel(self.frame_5)
        self.label_201.setGeometry(QtCore.QRect(1107, 2, 45, 25))
        self.label_201.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)\n"
"")
        self.label_201.setAlignment(QtCore.Qt.AlignCenter)
        self.label_201.setObjectName("label_201")
        self.label_226 = QtWidgets.QLabel(self.frame_5)
        self.label_226.setGeometry(QtCore.QRect(677, 2, 45, 25))
        self.label_226.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_226.setAlignment(QtCore.Qt.AlignCenter)
        self.label_226.setObjectName("label_226")
        self.label_533 = QtWidgets.QLabel(self.frame_5)
        self.label_533.setGeometry(QtCore.QRect(763, 347, 45, 25))
        self.label_533.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_533.setText("")
        self.label_533.setAlignment(QtCore.Qt.AlignCenter)
        self.label_533.setObjectName("label_533")
        self.label_532 = QtWidgets.QLabel(self.frame_5)
        self.label_532.setGeometry(QtCore.QRect(763, 301, 45, 25))
        self.label_532.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_532.setText("")
        self.label_532.setAlignment(QtCore.Qt.AlignCenter)
        self.label_532.setObjectName("label_532")
        self.label_609 = QtWidgets.QLabel(self.frame_5)
        self.label_609.setGeometry(QtCore.QRect(1064, 370, 45, 25))
        self.label_609.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_609.setText("")
        self.label_609.setAlignment(QtCore.Qt.AlignCenter)
        self.label_609.setObjectName("label_609")
        self.label_551 = QtWidgets.QLabel(self.frame_5)
        self.label_551.setGeometry(QtCore.QRect(849, 324, 45, 25))
        self.label_551.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_551.setText("")
        self.label_551.setAlignment(QtCore.Qt.AlignCenter)
        self.label_551.setObjectName("label_551")
        self.label_374 = QtWidgets.QLabel(self.frame_5)
        self.label_374.setGeometry(QtCore.QRect(167, 163, 71, 25))
        self.label_374.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_374.setText("")
        self.label_374.setAlignment(QtCore.Qt.AlignCenter)
        self.label_374.setObjectName("label_374")
        self.label_341 = QtWidgets.QLabel(self.frame_5)
        self.label_341.setGeometry(QtCore.QRect(935, 140, 45, 25))
        self.label_341.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_341.setText("")
        self.label_341.setAlignment(QtCore.Qt.AlignCenter)
        self.label_341.setObjectName("label_341")
        self.label_594 = QtWidgets.QLabel(self.frame_5)
        self.label_594.setGeometry(QtCore.QRect(1021, 324, 45, 25))
        self.label_594.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_594.setText("")
        self.label_594.setAlignment(QtCore.Qt.AlignCenter)
        self.label_594.setObjectName("label_594")
        self.label_422 = QtWidgets.QLabel(self.frame_5)
        self.label_422.setGeometry(QtCore.QRect(892, 186, 45, 25))
        self.label_422.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_422.setText("")
        self.label_422.setAlignment(QtCore.Qt.AlignCenter)
        self.label_422.setObjectName("label_422")
        self.label_369 = QtWidgets.QLabel(self.frame_5)
        self.label_369.setGeometry(QtCore.QRect(1193, 209, 45, 25))
        self.label_369.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_369.setText("")
        self.label_369.setAlignment(QtCore.Qt.AlignCenter)
        self.label_369.setObjectName("label_369")
        self.label_445 = QtWidgets.QLabel(self.frame_5)
        self.label_445.setGeometry(QtCore.QRect(849, 209, 45, 25))
        self.label_445.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_445.setText("")
        self.label_445.setAlignment(QtCore.Qt.AlignCenter)
        self.label_445.setObjectName("label_445")
        self.label_436 = QtWidgets.QLabel(self.frame_5)
        self.label_436.setGeometry(QtCore.QRect(806, 163, 45, 25))
        self.label_436.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_436.setText("")
        self.label_436.setAlignment(QtCore.Qt.AlignCenter)
        self.label_436.setObjectName("label_436")
        self.label_262 = QtWidgets.QLabel(self.frame_5)
        self.label_262.setGeometry(QtCore.QRect(677, 48, 45, 25))
        self.label_262.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_262.setText("")
        self.label_262.setAlignment(QtCore.Qt.AlignCenter)
        self.label_262.setObjectName("label_262")
        self.label_287 = QtWidgets.QLabel(self.frame_5)
        self.label_287.setGeometry(QtCore.QRect(0, 71, 30, 25))
        self.label_287.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)\n"
"")
        self.label_287.setAlignment(QtCore.Qt.AlignCenter)
        self.label_287.setObjectName("label_287")
        self.label_408 = QtWidgets.QLabel(self.frame_5)
        self.label_408.setGeometry(QtCore.QRect(806, 186, 45, 25))
        self.label_408.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_408.setText("")
        self.label_408.setAlignment(QtCore.Qt.AlignCenter)
        self.label_408.setObjectName("label_408")
        self.label_486 = QtWidgets.QLabel(self.frame_5)
        self.label_486.setGeometry(QtCore.QRect(806, 255, 45, 25))
        self.label_486.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_486.setText("")
        self.label_486.setAlignment(QtCore.Qt.AlignCenter)
        self.label_486.setObjectName("label_486")
        self.label_228 = QtWidgets.QLabel(self.frame_5)
        self.label_228.setGeometry(QtCore.QRect(1236, 2, 45, 25))
        self.label_228.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_228.setAlignment(QtCore.Qt.AlignCenter)
        self.label_228.setObjectName("label_228")
        self.label_260 = QtWidgets.QLabel(self.frame_5)
        self.label_260.setGeometry(QtCore.QRect(0, 48, 30, 25))
        self.label_260.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_260.setAlignment(QtCore.Qt.AlignCenter)
        self.label_260.setObjectName("label_260")
        self.label_339 = QtWidgets.QLabel(self.frame_5)
        self.label_339.setGeometry(QtCore.QRect(0, 94, 30, 25))
        self.label_339.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_339.setAlignment(QtCore.Qt.AlignCenter)
        self.label_339.setObjectName("label_339")
        self.label_317 = QtWidgets.QLabel(self.frame_5)
        self.label_317.setGeometry(QtCore.QRect(849, 117, 45, 25))
        self.label_317.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_317.setText("")
        self.label_317.setAlignment(QtCore.Qt.AlignCenter)
        self.label_317.setObjectName("label_317")
        self.label_438 = QtWidgets.QLabel(self.frame_5)
        self.label_438.setGeometry(QtCore.QRect(1021, 186, 45, 25))
        self.label_438.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_438.setText("")
        self.label_438.setAlignment(QtCore.Qt.AlignCenter)
        self.label_438.setObjectName("label_438")
        self.label_458 = QtWidgets.QLabel(self.frame_5)
        self.label_458.setGeometry(QtCore.QRect(591, 255, 45, 25))
        self.label_458.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_458.setText("")
        self.label_458.setAlignment(QtCore.Qt.AlignCenter)
        self.label_458.setObjectName("label_458")
        self.label_559 = QtWidgets.QLabel(self.frame_5)
        self.label_559.setGeometry(QtCore.QRect(677, 324, 45, 25))
        self.label_559.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_559.setText("")
        self.label_559.setAlignment(QtCore.Qt.AlignCenter)
        self.label_559.setObjectName("label_559")
        self.label_237 = QtWidgets.QLabel(self.frame_5)
        self.label_237.setGeometry(QtCore.QRect(413, 2, 51, 25))
        self.label_237.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_237.setAlignment(QtCore.Qt.AlignCenter)
        self.label_237.setObjectName("label_237")
        self.label_388 = QtWidgets.QLabel(self.frame_5)
        self.label_388.setGeometry(QtCore.QRect(1150, 209, 45, 25))
        self.label_388.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_388.setText("")
        self.label_388.setAlignment(QtCore.Qt.AlignCenter)
        self.label_388.setObjectName("label_388")
        self.label_601 = QtWidgets.QLabel(self.frame_5)
        self.label_601.setGeometry(QtCore.QRect(849, 347, 45, 25))
        self.label_601.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_601.setText("")
        self.label_601.setAlignment(QtCore.Qt.AlignCenter)
        self.label_601.setObjectName("label_601")
        self.label_347 = QtWidgets.QLabel(self.frame_5)
        self.label_347.setGeometry(QtCore.QRect(720, 117, 45, 25))
        self.label_347.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_347.setText("")
        self.label_347.setAlignment(QtCore.Qt.AlignCenter)
        self.label_347.setObjectName("label_347")
        self.label_379 = QtWidgets.QLabel(self.frame_5)
        self.label_379.setGeometry(QtCore.QRect(720, 209, 45, 25))
        self.label_379.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_379.setText("")
        self.label_379.setAlignment(QtCore.Qt.AlignCenter)
        self.label_379.setObjectName("label_379")
        self.label_394 = QtWidgets.QLabel(self.frame_5)
        self.label_394.setGeometry(QtCore.QRect(28, 186, 141, 25))
        self.label_394.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_394.setText("")
        self.label_394.setAlignment(QtCore.Qt.AlignCenter)
        self.label_394.setObjectName("label_394")
        self.label_396 = QtWidgets.QLabel(self.frame_5)
        self.label_396.setGeometry(QtCore.QRect(1064, 209, 45, 25))
        self.label_396.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_396.setText("")
        self.label_396.setAlignment(QtCore.Qt.AlignCenter)
        self.label_396.setObjectName("label_396")
        self.label_290 = QtWidgets.QLabel(self.frame_5)
        self.label_290.setGeometry(QtCore.QRect(364, 71, 51, 25))
        self.label_290.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_290.setText("")
        self.label_290.setAlignment(QtCore.Qt.AlignCenter)
        self.label_290.setObjectName("label_290")
        self.label_553 = QtWidgets.QLabel(self.frame_5)
        self.label_553.setGeometry(QtCore.QRect(1236, 347, 45, 25))
        self.label_553.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_553.setText("")
        self.label_553.setAlignment(QtCore.Qt.AlignCenter)
        self.label_553.setObjectName("label_553")
        self.label_224 = QtWidgets.QLabel(self.frame_5)
        self.label_224.setGeometry(QtCore.QRect(720, 2, 45, 25))
        self.label_224.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_224.setAlignment(QtCore.Qt.AlignCenter)
        self.label_224.setObjectName("label_224")
        self.label_393 = QtWidgets.QLabel(self.frame_5)
        self.label_393.setGeometry(QtCore.QRect(1021, 209, 45, 25))
        self.label_393.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_393.setText("")
        self.label_393.setAlignment(QtCore.Qt.AlignCenter)
        self.label_393.setObjectName("label_393")
        self.label_286 = QtWidgets.QLabel(self.frame_5)
        self.label_286.setGeometry(QtCore.QRect(720, 71, 45, 25))
        self.label_286.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_286.setText("")
        self.label_286.setAlignment(QtCore.Qt.AlignCenter)
        self.label_286.setObjectName("label_286")
        self.label_410 = QtWidgets.QLabel(self.frame_5)
        self.label_410.setGeometry(QtCore.QRect(1236, 186, 45, 25))
        self.label_410.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_410.setText("")
        self.label_410.setAlignment(QtCore.Qt.AlignCenter)
        self.label_410.setObjectName("label_410")
        self.label_294 = QtWidgets.QLabel(self.frame_5)
        self.label_294.setGeometry(QtCore.QRect(1107, 117, 45, 25))
        self.label_294.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_294.setText("")
        self.label_294.setAlignment(QtCore.Qt.AlignCenter)
        self.label_294.setObjectName("label_294")
        self.label_475 = QtWidgets.QLabel(self.frame_5)
        self.label_475.setGeometry(QtCore.QRect(1236, 278, 45, 25))
        self.label_475.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_475.setText("")
        self.label_475.setAlignment(QtCore.Qt.AlignCenter)
        self.label_475.setObjectName("label_475")
        self.label_432 = QtWidgets.QLabel(self.frame_5)
        self.label_432.setGeometry(QtCore.QRect(28, 163, 141, 25))
        self.label_432.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_432.setText("")
        self.label_432.setAlignment(QtCore.Qt.AlignCenter)
        self.label_432.setObjectName("label_432")
        self.label_266 = QtWidgets.QLabel(self.frame_5)
        self.label_266.setGeometry(QtCore.QRect(548, 71, 45, 25))
        self.label_266.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_266.setText("")
        self.label_266.setAlignment(QtCore.Qt.AlignCenter)
        self.label_266.setObjectName("label_266")
        self.label_199 = QtWidgets.QLabel(self.frame_5)
        self.label_199.setGeometry(QtCore.QRect(462, 2, 45, 25))
        self.label_199.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_199.setAlignment(QtCore.Qt.AlignCenter)
        self.label_199.setObjectName("label_199")
        self.label_345 = QtWidgets.QLabel(self.frame_5)
        self.label_345.setGeometry(QtCore.QRect(892, 140, 45, 25))
        self.label_345.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_345.setText("")
        self.label_345.setAlignment(QtCore.Qt.AlignCenter)
        self.label_345.setObjectName("label_345")
        self.label_584 = QtWidgets.QLabel(self.frame_5)
        self.label_584.setGeometry(QtCore.QRect(634, 347, 45, 25))
        self.label_584.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_584.setText("")
        self.label_584.setAlignment(QtCore.Qt.AlignCenter)
        self.label_584.setObjectName("label_584")
        self.label_280 = QtWidgets.QLabel(self.frame_5)
        self.label_280.setGeometry(QtCore.QRect(677, 71, 45, 25))
        self.label_280.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_280.setText("")
        self.label_280.setAlignment(QtCore.Qt.AlignCenter)
        self.label_280.setObjectName("label_280")
        self.label_235 = QtWidgets.QLabel(self.frame_5)
        self.label_235.setGeometry(QtCore.QRect(548, 25, 45, 25))
        self.label_235.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_235.setText("")
        self.label_235.setAlignment(QtCore.Qt.AlignCenter)
        self.label_235.setObjectName("label_235")
        self.label_413 = QtWidgets.QLabel(self.frame_5)
        self.label_413.setGeometry(QtCore.QRect(677, 163, 45, 25))
        self.label_413.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_413.setText("")
        self.label_413.setAlignment(QtCore.Qt.AlignCenter)
        self.label_413.setObjectName("label_413")
        self.label_598 = QtWidgets.QLabel(self.frame_5)
        self.label_598.setGeometry(QtCore.QRect(505, 324, 45, 25))
        self.label_598.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_598.setText("")
        self.label_598.setAlignment(QtCore.Qt.AlignCenter)
        self.label_598.setObjectName("label_598")
        self.label_252 = QtWidgets.QLabel(self.frame_5)
        self.label_252.setGeometry(QtCore.QRect(1193, 48, 45, 25))
        self.label_252.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_252.setText("")
        self.label_252.setAlignment(QtCore.Qt.AlignCenter)
        self.label_252.setObjectName("label_252")
        self.label_215 = QtWidgets.QLabel(self.frame_5)
        self.label_215.setGeometry(QtCore.QRect(849, 2, 45, 25))
        self.label_215.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_215.setAlignment(QtCore.Qt.AlignCenter)
        self.label_215.setObjectName("label_215")
        self.label_479 = QtWidgets.QLabel(self.frame_5)
        self.label_479.setGeometry(QtCore.QRect(1150, 232, 45, 25))
        self.label_479.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_479.setText("")
        self.label_479.setAlignment(QtCore.Qt.AlignCenter)
        self.label_479.setObjectName("label_479")
        self.label_473 = QtWidgets.QLabel(self.frame_5)
        self.label_473.setGeometry(QtCore.QRect(849, 255, 45, 25))
        self.label_473.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_473.setText("")
        self.label_473.setAlignment(QtCore.Qt.AlignCenter)
        self.label_473.setObjectName("label_473")
        self.label_270 = QtWidgets.QLabel(self.frame_5)
        self.label_270.setGeometry(QtCore.QRect(462, 71, 45, 25))
        self.label_270.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_270.setText("")
        self.label_270.setAlignment(QtCore.Qt.AlignCenter)
        self.label_270.setObjectName("label_270")
        self.label_430 = QtWidgets.QLabel(self.frame_5)
        self.label_430.setGeometry(QtCore.QRect(1064, 186, 45, 25))
        self.label_430.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_430.setText("")
        self.label_430.setAlignment(QtCore.Qt.AlignCenter)
        self.label_430.setObjectName("label_430")
        self.label_569 = QtWidgets.QLabel(self.frame_5)
        self.label_569.setGeometry(QtCore.QRect(677, 301, 45, 25))
        self.label_569.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_569.setText("")
        self.label_569.setAlignment(QtCore.Qt.AlignCenter)
        self.label_569.setObjectName("label_569")
        self.label_239 = QtWidgets.QLabel(self.frame_5)
        self.label_239.setGeometry(QtCore.QRect(806, 48, 45, 25))
        self.label_239.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_239.setText("")
        self.label_239.setAlignment(QtCore.Qt.AlignCenter)
        self.label_239.setObjectName("label_239")
        self.label_255 = QtWidgets.QLabel(self.frame_5)
        self.label_255.setGeometry(QtCore.QRect(849, 48, 45, 25))
        self.label_255.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_255.setText("")
        self.label_255.setAlignment(QtCore.Qt.AlignCenter)
        self.label_255.setObjectName("label_255")
        self.label_446 = QtWidgets.QLabel(self.frame_5)
        self.label_446.setGeometry(QtCore.QRect(1064, 163, 45, 25))
        self.label_446.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_446.setText("")
        self.label_446.setAlignment(QtCore.Qt.AlignCenter)
        self.label_446.setObjectName("label_446")
        self.label_439 = QtWidgets.QLabel(self.frame_5)
        self.label_439.setGeometry(QtCore.QRect(763, 186, 45, 25))
        self.label_439.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_439.setText("")
        self.label_439.setAlignment(QtCore.Qt.AlignCenter)
        self.label_439.setObjectName("label_439")
        self.label_289 = QtWidgets.QLabel(self.frame_5)
        self.label_289.setGeometry(QtCore.QRect(763, 71, 45, 25))
        self.label_289.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_289.setText("")
        self.label_289.setAlignment(QtCore.Qt.AlignCenter)
        self.label_289.setObjectName("label_289")
        self.label_578 = QtWidgets.QLabel(self.frame_5)
        self.label_578.setGeometry(QtCore.QRect(892, 324, 45, 25))
        self.label_578.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_578.setText("")
        self.label_578.setAlignment(QtCore.Qt.AlignCenter)
        self.label_578.setObjectName("label_578")
        self.label_406 = QtWidgets.QLabel(self.frame_5)
        self.label_406.setGeometry(QtCore.QRect(978, 186, 45, 25))
        self.label_406.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_406.setText("")
        self.label_406.setAlignment(QtCore.Qt.AlignCenter)
        self.label_406.setObjectName("label_406")
        self.label_563 = QtWidgets.QLabel(self.frame_5)
        self.label_563.setGeometry(QtCore.QRect(462, 324, 45, 25))
        self.label_563.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_563.setText("")
        self.label_563.setAlignment(QtCore.Qt.AlignCenter)
        self.label_563.setObjectName("label_563")
        self.label_210 = QtWidgets.QLabel(self.frame_5)
        self.label_210.setGeometry(QtCore.QRect(364, 25, 51, 25))
        self.label_210.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_210.setText("")
        self.label_210.setAlignment(QtCore.Qt.AlignCenter)
        self.label_210.setObjectName("label_210")
        self.label_558 = QtWidgets.QLabel(self.frame_5)
        self.label_558.setGeometry(QtCore.QRect(1150, 324, 45, 25))
        self.label_558.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_558.setText("")
        self.label_558.setAlignment(QtCore.Qt.AlignCenter)
        self.label_558.setObjectName("label_558")
        self.label_576 = QtWidgets.QLabel(self.frame_5)
        self.label_576.setGeometry(QtCore.QRect(505, 347, 45, 25))
        self.label_576.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_576.setText("")
        self.label_576.setAlignment(QtCore.Qt.AlignCenter)
        self.label_576.setObjectName("label_576")
        self.label_312 = QtWidgets.QLabel(self.frame_5)
        self.label_312.setGeometry(QtCore.QRect(1107, 94, 45, 25))
        self.label_312.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_312.setText("")
        self.label_312.setAlignment(QtCore.Qt.AlignCenter)
        self.label_312.setObjectName("label_312")
        self.label_405 = QtWidgets.QLabel(self.frame_5)
        self.label_405.setGeometry(QtCore.QRect(462, 209, 45, 25))
        self.label_405.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_405.setText("")
        self.label_405.setAlignment(QtCore.Qt.AlignCenter)
        self.label_405.setObjectName("label_405")
        self.label_230 = QtWidgets.QLabel(self.frame_5)
        self.label_230.setGeometry(QtCore.QRect(1021, 2, 45, 25))
        self.label_230.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_230.setAlignment(QtCore.Qt.AlignCenter)
        self.label_230.setObjectName("label_230")
        self.label_355 = QtWidgets.QLabel(self.frame_5)
        self.label_355.setGeometry(QtCore.QRect(548, 117, 45, 25))
        self.label_355.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_355.setText("")
        self.label_355.setAlignment(QtCore.Qt.AlignCenter)
        self.label_355.setObjectName("label_355")
        self.label_326 = QtWidgets.QLabel(self.frame_5)
        self.label_326.setGeometry(QtCore.QRect(849, 94, 45, 25))
        self.label_326.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_326.setText("")
        self.label_326.setAlignment(QtCore.Qt.AlignCenter)
        self.label_326.setObjectName("label_326")
        self.label_409 = QtWidgets.QLabel(self.frame_5)
        self.label_409.setGeometry(QtCore.QRect(236, 209, 61, 25))
        self.label_409.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_409.setText("")
        self.label_409.setAlignment(QtCore.Qt.AlignCenter)
        self.label_409.setObjectName("label_409")
        self.label_381 = QtWidgets.QLabel(self.frame_5)
        self.label_381.setGeometry(QtCore.QRect(295, 209, 71, 25))
        self.label_381.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_381.setText("")
        self.label_381.setAlignment(QtCore.Qt.AlignCenter)
        self.label_381.setObjectName("label_381")
        self.label_274 = QtWidgets.QLabel(self.frame_5)
        self.label_274.setGeometry(QtCore.QRect(1193, 71, 45, 25))
        self.label_274.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_274.setText("")
        self.label_274.setAlignment(QtCore.Qt.AlignCenter)
        self.label_274.setObjectName("label_274")
        self.label_244 = QtWidgets.QLabel(self.frame_5)
        self.label_244.setGeometry(QtCore.QRect(236, 48, 61, 25))
        self.label_244.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_244.setText("")
        self.label_244.setAlignment(QtCore.Qt.AlignCenter)
        self.label_244.setObjectName("label_244")
        self.label_368 = QtWidgets.QLabel(self.frame_5)
        self.label_368.setGeometry(QtCore.QRect(1064, 94, 45, 25))
        self.label_368.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_368.setText("")
        self.label_368.setAlignment(QtCore.Qt.AlignCenter)
        self.label_368.setObjectName("label_368")
        self.label_427 = QtWidgets.QLabel(self.frame_5)
        self.label_427.setGeometry(QtCore.QRect(1193, 163, 45, 25))
        self.label_427.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_427.setText("")
        self.label_427.setAlignment(QtCore.Qt.AlignCenter)
        self.label_427.setObjectName("label_427")
        self.label_321 = QtWidgets.QLabel(self.frame_5)
        self.label_321.setGeometry(QtCore.QRect(413, 140, 51, 25))
        self.label_321.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_321.setText("")
        self.label_321.setAlignment(QtCore.Qt.AlignCenter)
        self.label_321.setObjectName("label_321")
        self.label_353 = QtWidgets.QLabel(self.frame_5)
        self.label_353.setGeometry(QtCore.QRect(0, 117, 30, 25))
        self.label_353.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_353.setAlignment(QtCore.Qt.AlignCenter)
        self.label_353.setObjectName("label_353")
        self.label_548 = QtWidgets.QLabel(self.frame_5)
        self.label_548.setGeometry(QtCore.QRect(295, 301, 71, 25))
        self.label_548.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_548.setText("")
        self.label_548.setAlignment(QtCore.Qt.AlignCenter)
        self.label_548.setObjectName("label_548")
        self.label_249 = QtWidgets.QLabel(self.frame_5)
        self.label_249.setGeometry(QtCore.QRect(1107, 48, 45, 25))
        self.label_249.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_249.setText("")
        self.label_249.setAlignment(QtCore.Qt.AlignCenter)
        self.label_249.setObjectName("label_249")
        self.label_316 = QtWidgets.QLabel(self.frame_5)
        self.label_316.setGeometry(QtCore.QRect(28, 117, 141, 25))
        self.label_316.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_316.setText("")
        self.label_316.setAlignment(QtCore.Qt.AlignCenter)
        self.label_316.setObjectName("label_316")
        self.label_203 = QtWidgets.QLabel(self.frame_5)
        self.label_203.setGeometry(QtCore.QRect(634, 25, 45, 25))
        self.label_203.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_203.setText("")
        self.label_203.setAlignment(QtCore.Qt.AlignCenter)
        self.label_203.setObjectName("label_203")
        self.label_364 = QtWidgets.QLabel(self.frame_5)
        self.label_364.setGeometry(QtCore.QRect(505, 117, 45, 25))
        self.label_364.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_364.setText("")
        self.label_364.setAlignment(QtCore.Qt.AlignCenter)
        self.label_364.setObjectName("label_364")
        self.label_526 = QtWidgets.QLabel(self.frame_5)
        self.label_526.setGeometry(QtCore.QRect(806, 347, 45, 25))
        self.label_526.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_526.setText("")
        self.label_526.setAlignment(QtCore.Qt.AlignCenter)
        self.label_526.setObjectName("label_526")
        self.label_602 = QtWidgets.QLabel(self.frame_5)
        self.label_602.setGeometry(QtCore.QRect(1064, 301, 45, 25))
        self.label_602.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_602.setText("")
        self.label_602.setAlignment(QtCore.Qt.AlignCenter)
        self.label_602.setObjectName("label_602")
        self.label_587 = QtWidgets.QLabel(self.frame_5)
        self.label_587.setGeometry(QtCore.QRect(0, 324, 30, 25))
        self.label_587.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_587.setAlignment(QtCore.Qt.AlignCenter)
        self.label_587.setObjectName("label_587")
        self.label_522 = QtWidgets.QLabel(self.frame_5)
        self.label_522.setGeometry(QtCore.QRect(591, 232, 45, 25))
        self.label_522.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_522.setText("")
        self.label_522.setAlignment(QtCore.Qt.AlignCenter)
        self.label_522.setObjectName("label_522")
        self.label_499 = QtWidgets.QLabel(self.frame_5)
        self.label_499.setGeometry(QtCore.QRect(634, 255, 45, 25))
        self.label_499.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_499.setText("")
        self.label_499.setAlignment(QtCore.Qt.AlignCenter)
        self.label_499.setObjectName("label_499")
        self.label_461 = QtWidgets.QLabel(self.frame_5)
        self.label_461.setGeometry(QtCore.QRect(295, 255, 71, 25))
        self.label_461.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_461.setText("")
        self.label_461.setAlignment(QtCore.Qt.AlignCenter)
        self.label_461.setObjectName("label_461")
        self.label_295 = QtWidgets.QLabel(self.frame_5)
        self.label_295.setGeometry(QtCore.QRect(1107, 140, 45, 25))
        self.label_295.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_295.setText("")
        self.label_295.setAlignment(QtCore.Qt.AlignCenter)
        self.label_295.setObjectName("label_295")
        self.label_324 = QtWidgets.QLabel(self.frame_5)
        self.label_324.setGeometry(QtCore.QRect(1150, 117, 45, 25))
        self.label_324.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_324.setText("")
        self.label_324.setAlignment(QtCore.Qt.AlignCenter)
        self.label_324.setObjectName("label_324")
        self.label_277 = QtWidgets.QLabel(self.frame_5)
        self.label_277.setGeometry(QtCore.QRect(849, 71, 45, 25))
        self.label_277.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_277.setText("")
        self.label_277.setAlignment(QtCore.Qt.AlignCenter)
        self.label_277.setObjectName("label_277")
        self.label_503 = QtWidgets.QLabel(self.frame_5)
        self.label_503.setGeometry(QtCore.QRect(720, 255, 45, 25))
        self.label_503.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_503.setText("")
        self.label_503.setAlignment(QtCore.Qt.AlignCenter)
        self.label_503.setObjectName("label_503")
        self.label_227 = QtWidgets.QLabel(self.frame_5)
        self.label_227.setGeometry(QtCore.QRect(295, 2, 71, 25))
        self.label_227.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_227.setAlignment(QtCore.Qt.AlignCenter)
        self.label_227.setObjectName("label_227")
        self.label_214 = QtWidgets.QLabel(self.frame_5)
        self.label_214.setGeometry(QtCore.QRect(1150, 2, 45, 25))
        self.label_214.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_214.setAlignment(QtCore.Qt.AlignCenter)
        self.label_214.setObjectName("label_214")
        self.label_493 = QtWidgets.QLabel(self.frame_5)
        self.label_493.setGeometry(QtCore.QRect(236, 232, 61, 25))
        self.label_493.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_493.setText("")
        self.label_493.setAlignment(QtCore.Qt.AlignCenter)
        self.label_493.setObjectName("label_493")
        self.label_622 = QtWidgets.QLabel(self.frame_5)
        self.label_622.setGeometry(QtCore.QRect(364, 370, 51, 25))
        self.label_622.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_622.setText("")
        self.label_622.setAlignment(QtCore.Qt.AlignCenter)
        self.label_622.setObjectName("label_622")
        self.label_423 = QtWidgets.QLabel(self.frame_5)
        self.label_423.setGeometry(QtCore.QRect(892, 209, 45, 25))
        self.label_423.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_423.setText("")
        self.label_423.setAlignment(QtCore.Qt.AlignCenter)
        self.label_423.setObjectName("label_423")
        self.label_200 = QtWidgets.QLabel(self.frame_5)
        self.label_200.setGeometry(QtCore.QRect(0, 25, 30, 25))
        self.label_200.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_200.setAlignment(QtCore.Qt.AlignCenter)
        self.label_200.setObjectName("label_200")
        self.label_377 = QtWidgets.QLabel(self.frame_5)
        self.label_377.setGeometry(QtCore.QRect(763, 209, 45, 25))
        self.label_377.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_377.setText("")
        self.label_377.setAlignment(QtCore.Qt.AlignCenter)
        self.label_377.setObjectName("label_377")
        self.label_443 = QtWidgets.QLabel(self.frame_5)
        self.label_443.setGeometry(QtCore.QRect(413, 163, 51, 25))
        self.label_443.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_443.setText("")
        self.label_443.setAlignment(QtCore.Qt.AlignCenter)
        self.label_443.setObjectName("label_443")
        self.label_331 = QtWidgets.QLabel(self.frame_5)
        self.label_331.setGeometry(QtCore.QRect(236, 140, 61, 25))
        self.label_331.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_331.setText("")
        self.label_331.setAlignment(QtCore.Qt.AlignCenter)
        self.label_331.setObjectName("label_331")
        self.label_307 = QtWidgets.QLabel(self.frame_5)
        self.label_307.setGeometry(QtCore.QRect(364, 94, 51, 25))
        self.label_307.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_307.setText("")
        self.label_307.setAlignment(QtCore.Qt.AlignCenter)
        self.label_307.setObjectName("label_307")
        self.label_343 = QtWidgets.QLabel(self.frame_5)
        self.label_343.setGeometry(QtCore.QRect(634, 117, 45, 25))
        self.label_343.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_343.setText("")
        self.label_343.setAlignment(QtCore.Qt.AlignCenter)
        self.label_343.setObjectName("label_343")
        self.label_454 = QtWidgets.QLabel(self.frame_5)
        self.label_454.setGeometry(QtCore.QRect(763, 232, 45, 25))
        self.label_454.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_454.setText("")
        self.label_454.setAlignment(QtCore.Qt.AlignCenter)
        self.label_454.setObjectName("label_454")
        self.label_487 = QtWidgets.QLabel(self.frame_5)
        self.label_487.setGeometry(QtCore.QRect(236, 278, 61, 25))
        self.label_487.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_487.setText("")
        self.label_487.setAlignment(QtCore.Qt.AlignCenter)
        self.label_487.setObjectName("label_487")
        self.label_537 = QtWidgets.QLabel(self.frame_5)
        self.label_537.setGeometry(QtCore.QRect(295, 347, 71, 25))
        self.label_537.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_537.setText("")
        self.label_537.setAlignment(QtCore.Qt.AlignCenter)
        self.label_537.setObjectName("label_537")
        self.label_625 = QtWidgets.QLabel(self.frame_5)
        self.label_625.setGeometry(QtCore.QRect(1193, 370, 45, 25))
        self.label_625.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_625.setText("")
        self.label_625.setAlignment(QtCore.Qt.AlignCenter)
        self.label_625.setObjectName("label_625")
        self.label_267 = QtWidgets.QLabel(self.frame_5)
        self.label_267.setGeometry(QtCore.QRect(236, 71, 61, 25))
        self.label_267.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_267.setText("")
        self.label_267.setAlignment(QtCore.Qt.AlignCenter)
        self.label_267.setObjectName("label_267")
        self.label_580 = QtWidgets.QLabel(self.frame_5)
        self.label_580.setGeometry(QtCore.QRect(935, 301, 45, 25))
        self.label_580.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_580.setText("")
        self.label_580.setAlignment(QtCore.Qt.AlignCenter)
        self.label_580.setObjectName("label_580")
        self.label_359 = QtWidgets.QLabel(self.frame_5)
        self.label_359.setGeometry(QtCore.QRect(0, 140, 30, 25))
        self.label_359.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_359.setAlignment(QtCore.Qt.AlignCenter)
        self.label_359.setObjectName("label_359")
        self.label_384 = QtWidgets.QLabel(self.frame_5)
        self.label_384.setGeometry(QtCore.QRect(364, 186, 51, 25))
        self.label_384.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_384.setText("")
        self.label_384.setAlignment(QtCore.Qt.AlignCenter)
        self.label_384.setObjectName("label_384")
        self.label_401 = QtWidgets.QLabel(self.frame_5)
        self.label_401.setGeometry(QtCore.QRect(1150, 163, 45, 25))
        self.label_401.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_401.setText("")
        self.label_401.setAlignment(QtCore.Qt.AlignCenter)
        self.label_401.setObjectName("label_401")
        self.label_504 = QtWidgets.QLabel(self.frame_5)
        self.label_504.setGeometry(QtCore.QRect(978, 232, 45, 25))
        self.label_504.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_504.setText("")
        self.label_504.setAlignment(QtCore.Qt.AlignCenter)
        self.label_504.setObjectName("label_504")
        self.label_229 = QtWidgets.QLabel(self.frame_5)
        self.label_229.setGeometry(QtCore.QRect(591, 2, 45, 25))
        self.label_229.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_229.setAlignment(QtCore.Qt.AlignCenter)
        self.label_229.setObjectName("label_229")
        self.label_463 = QtWidgets.QLabel(self.frame_5)
        self.label_463.setGeometry(QtCore.QRect(364, 232, 51, 25))
        self.label_463.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_463.setText("")
        self.label_463.setAlignment(QtCore.Qt.AlignCenter)
        self.label_463.setObjectName("label_463")
        self.label_624 = QtWidgets.QLabel(self.frame_5)
        self.label_624.setGeometry(QtCore.QRect(892, 370, 45, 25))
        self.label_624.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_624.setText("")
        self.label_624.setAlignment(QtCore.Qt.AlignCenter)
        self.label_624.setObjectName("label_624")
        self.label_480 = QtWidgets.QLabel(self.frame_5)
        self.label_480.setGeometry(QtCore.QRect(1150, 255, 45, 25))
        self.label_480.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_480.setText("")
        self.label_480.setAlignment(QtCore.Qt.AlignCenter)
        self.label_480.setObjectName("label_480")
        self.label_415 = QtWidgets.QLabel(self.frame_5)
        self.label_415.setGeometry(QtCore.QRect(236, 163, 61, 25))
        self.label_415.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_415.setText("")
        self.label_415.setAlignment(QtCore.Qt.AlignCenter)
        self.label_415.setObjectName("label_415")
        self.label_457 = QtWidgets.QLabel(self.frame_5)
        self.label_457.setGeometry(QtCore.QRect(720, 278, 45, 25))
        self.label_457.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_457.setText("")
        self.label_457.setAlignment(QtCore.Qt.AlignCenter)
        self.label_457.setObjectName("label_457")
        self.label_428 = QtWidgets.QLabel(self.frame_5)
        self.label_428.setGeometry(QtCore.QRect(634, 209, 45, 25))
        self.label_428.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_428.setText("")
        self.label_428.setAlignment(QtCore.Qt.AlignCenter)
        self.label_428.setObjectName("label_428")
        self.label_285 = QtWidgets.QLabel(self.frame_5)
        self.label_285.setGeometry(QtCore.QRect(505, 71, 45, 25))
        self.label_285.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_285.setText("")
        self.label_285.setAlignment(QtCore.Qt.AlignCenter)
        self.label_285.setObjectName("label_285")
        self.label_516 = QtWidgets.QLabel(self.frame_5)
        self.label_516.setGeometry(QtCore.QRect(1021, 255, 45, 25))
        self.label_516.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_516.setText("")
        self.label_516.setAlignment(QtCore.Qt.AlignCenter)
        self.label_516.setObjectName("label_516")
        self.label_468 = QtWidgets.QLabel(self.frame_5)
        self.label_468.setGeometry(QtCore.QRect(1107, 232, 45, 25))
        self.label_468.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_468.setText("")
        self.label_468.setAlignment(QtCore.Qt.AlignCenter)
        self.label_468.setObjectName("label_468")
        self.label_257 = QtWidgets.QLabel(self.frame_5)
        self.label_257.setGeometry(QtCore.QRect(548, 48, 45, 25))
        self.label_257.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_257.setText("")
        self.label_257.setAlignment(QtCore.Qt.AlignCenter)
        self.label_257.setObjectName("label_257")
        self.label_245 = QtWidgets.QLabel(self.frame_5)
        self.label_245.setGeometry(QtCore.QRect(364, 48, 51, 25))
        self.label_245.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_245.setText("")
        self.label_245.setAlignment(QtCore.Qt.AlignCenter)
        self.label_245.setObjectName("label_245")
        self.label_617 = QtWidgets.QLabel(self.frame_5)
        self.label_617.setGeometry(QtCore.QRect(413, 370, 51, 25))
        self.label_617.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_617.setText("")
        self.label_617.setAlignment(QtCore.Qt.AlignCenter)
        self.label_617.setObjectName("label_617")
        self.label_557 = QtWidgets.QLabel(self.frame_5)
        self.label_557.setGeometry(QtCore.QRect(1150, 301, 45, 25))
        self.label_557.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_557.setText("")
        self.label_557.setAlignment(QtCore.Qt.AlignCenter)
        self.label_557.setObjectName("label_557")
        self.label_604 = QtWidgets.QLabel(self.frame_5)
        self.label_604.setGeometry(QtCore.QRect(548, 370, 45, 25))
        self.label_604.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_604.setText("")
        self.label_604.setAlignment(QtCore.Qt.AlignCenter)
        self.label_604.setObjectName("label_604")
        self.label_309 = QtWidgets.QLabel(self.frame_5)
        self.label_309.setGeometry(QtCore.QRect(634, 94, 45, 25))
        self.label_309.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_309.setText("")
        self.label_309.setAlignment(QtCore.Qt.AlignCenter)
        self.label_309.setObjectName("label_309")
        self.label_395 = QtWidgets.QLabel(self.frame_5)
        self.label_395.setGeometry(QtCore.QRect(849, 186, 45, 25))
        self.label_395.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_395.setText("")
        self.label_395.setAlignment(QtCore.Qt.AlignCenter)
        self.label_395.setObjectName("label_395")
        self.label_611 = QtWidgets.QLabel(self.frame_5)
        self.label_611.setGeometry(QtCore.QRect(978, 370, 45, 25))
        self.label_611.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_611.setText("")
        self.label_611.setAlignment(QtCore.Qt.AlignCenter)
        self.label_611.setObjectName("label_611")
        self.label_334 = QtWidgets.QLabel(self.frame_5)
        self.label_334.setGeometry(QtCore.QRect(720, 94, 45, 25))
        self.label_334.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_334.setText("")
        self.label_334.setAlignment(QtCore.Qt.AlignCenter)
        self.label_334.setObjectName("label_334")
        self.label_329 = QtWidgets.QLabel(self.frame_5)
        self.label_329.setGeometry(QtCore.QRect(462, 117, 45, 25))
        self.label_329.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_329.setText("")
        self.label_329.setAlignment(QtCore.Qt.AlignCenter)
        self.label_329.setObjectName("label_329")
        self.label_398 = QtWidgets.QLabel(self.frame_5)
        self.label_398.setGeometry(QtCore.QRect(1021, 163, 45, 25))
        self.label_398.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_398.setText("")
        self.label_398.setAlignment(QtCore.Qt.AlignCenter)
        self.label_398.setObjectName("label_398")
        self.label_511 = QtWidgets.QLabel(self.frame_5)
        self.label_511.setGeometry(QtCore.QRect(548, 255, 45, 25))
        self.label_511.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_511.setText("")
        self.label_511.setAlignment(QtCore.Qt.AlignCenter)
        self.label_511.setObjectName("label_511")
        self.label_365 = QtWidgets.QLabel(self.frame_5)
        self.label_365.setGeometry(QtCore.QRect(413, 94, 51, 25))
        self.label_365.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_365.setText("")
        self.label_365.setAlignment(QtCore.Qt.AlignCenter)
        self.label_365.setObjectName("label_365")
        self.label_198 = QtWidgets.QLabel(self.frame_5)
        self.label_198.setGeometry(QtCore.QRect(1236, 25, 45, 25))
        self.label_198.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_198.setText("")
        self.label_198.setAlignment(QtCore.Qt.AlignCenter)
        self.label_198.setObjectName("label_198")
        self.label_613 = QtWidgets.QLabel(self.frame_5)
        self.label_613.setGeometry(QtCore.QRect(167, 370, 71, 25))
        self.label_613.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_613.setText("")
        self.label_613.setAlignment(QtCore.Qt.AlignCenter)
        self.label_613.setObjectName("label_613")
        self.label_506 = QtWidgets.QLabel(self.frame_5)
        self.label_506.setGeometry(QtCore.QRect(634, 278, 45, 25))
        self.label_506.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_506.setText("")
        self.label_506.setAlignment(QtCore.Qt.AlignCenter)
        self.label_506.setObjectName("label_506")
        self.label_582 = QtWidgets.QLabel(self.frame_5)
        self.label_582.setGeometry(QtCore.QRect(978, 301, 45, 25))
        self.label_582.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_582.setText("")
        self.label_582.setAlignment(QtCore.Qt.AlignCenter)
        self.label_582.setObjectName("label_582")
        self.label_278 = QtWidgets.QLabel(self.frame_5)
        self.label_278.setGeometry(QtCore.QRect(591, 71, 45, 25))
        self.label_278.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_278.setText("")
        self.label_278.setAlignment(QtCore.Qt.AlignCenter)
        self.label_278.setObjectName("label_278")
        self.label_273 = QtWidgets.QLabel(self.frame_5)
        self.label_273.setGeometry(QtCore.QRect(634, 71, 45, 25))
        self.label_273.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_273.setText("")
        self.label_273.setAlignment(QtCore.Qt.AlignCenter)
        self.label_273.setObjectName("label_273")
        self.label_360 = QtWidgets.QLabel(self.frame_5)
        self.label_360.setGeometry(QtCore.QRect(1021, 117, 45, 25))
        self.label_360.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_360.setText("")
        self.label_360.setAlignment(QtCore.Qt.AlignCenter)
        self.label_360.setObjectName("label_360")
        self.label_247 = QtWidgets.QLabel(self.frame_5)
        self.label_247.setGeometry(QtCore.QRect(28, 48, 141, 25))
        self.label_247.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_247.setText("")
        self.label_247.setAlignment(QtCore.Qt.AlignCenter)
        self.label_247.setObjectName("label_247")
        self.label_299 = QtWidgets.QLabel(self.frame_5)
        self.label_299.setGeometry(QtCore.QRect(763, 140, 45, 25))
        self.label_299.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_299.setText("")
        self.label_299.setAlignment(QtCore.Qt.AlignCenter)
        self.label_299.setObjectName("label_299")
        self.label_348 = QtWidgets.QLabel(self.frame_5)
        self.label_348.setGeometry(QtCore.QRect(978, 94, 45, 25))
        self.label_348.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_348.setText("")
        self.label_348.setAlignment(QtCore.Qt.AlignCenter)
        self.label_348.setObjectName("label_348")
        self.label_500 = QtWidgets.QLabel(self.frame_5)
        self.label_500.setGeometry(QtCore.QRect(892, 255, 45, 25))
        self.label_500.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_500.setText("")
        self.label_500.setAlignment(QtCore.Qt.AlignCenter)
        self.label_500.setObjectName("label_500")
        self.label_433 = QtWidgets.QLabel(self.frame_5)
        self.label_433.setGeometry(QtCore.QRect(548, 186, 45, 25))
        self.label_433.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_433.setText("")
        self.label_433.setAlignment(QtCore.Qt.AlignCenter)
        self.label_433.setObjectName("label_433")
        self.label_291 = QtWidgets.QLabel(self.frame_5)
        self.label_291.setGeometry(QtCore.QRect(1193, 140, 45, 25))
        self.label_291.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_291.setText("")
        self.label_291.setAlignment(QtCore.Qt.AlignCenter)
        self.label_291.setObjectName("label_291")
        self.label_596 = QtWidgets.QLabel(self.frame_5)
        self.label_596.setGeometry(QtCore.QRect(1236, 301, 45, 25))
        self.label_596.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_596.setText("")
        self.label_596.setAlignment(QtCore.Qt.AlignCenter)
        self.label_596.setObjectName("label_596")
        self.label_431 = QtWidgets.QLabel(self.frame_5)
        self.label_431.setGeometry(QtCore.QRect(0, 186, 30, 25))
        self.label_431.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_431.setAlignment(QtCore.Qt.AlignCenter)
        self.label_431.setObjectName("label_431")
        self.label_196 = QtWidgets.QLabel(self.frame_5)
        self.label_196.setGeometry(QtCore.QRect(505, 2, 45, 25))
        self.label_196.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_196.setAlignment(QtCore.Qt.AlignCenter)
        self.label_196.setObjectName("label_196")
        self.label_615 = QtWidgets.QLabel(self.frame_5)
        self.label_615.setGeometry(QtCore.QRect(1021, 370, 45, 25))
        self.label_615.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_615.setText("")
        self.label_615.setAlignment(QtCore.Qt.AlignCenter)
        self.label_615.setObjectName("label_615")
        self.label_193 = QtWidgets.QLabel(self.frame_5)
        self.label_193.setGeometry(QtCore.QRect(548, 2, 45, 25))
        self.label_193.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_193.setAlignment(QtCore.Qt.AlignCenter)
        self.label_193.setObjectName("label_193")
        self.label_279 = QtWidgets.QLabel(self.frame_5)
        self.label_279.setGeometry(QtCore.QRect(978, 71, 45, 25))
        self.label_279.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_279.setText("")
        self.label_279.setAlignment(QtCore.Qt.AlignCenter)
        self.label_279.setObjectName("label_279")
        self.label_477 = QtWidgets.QLabel(self.frame_5)
        self.label_477.setGeometry(QtCore.QRect(413, 278, 51, 25))
        self.label_477.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_477.setText("")
        self.label_477.setAlignment(QtCore.Qt.AlignCenter)
        self.label_477.setObjectName("label_477")
        self.label_449 = QtWidgets.QLabel(self.frame_5)
        self.label_449.setGeometry(QtCore.QRect(505, 232, 45, 25))
        self.label_449.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_449.setText("")
        self.label_449.setAlignment(QtCore.Qt.AlignCenter)
        self.label_449.setObjectName("label_449")
        self.label_556 = QtWidgets.QLabel(self.frame_5)
        self.label_556.setGeometry(QtCore.QRect(935, 324, 45, 25))
        self.label_556.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_556.setText("")
        self.label_556.setAlignment(QtCore.Qt.AlignCenter)
        self.label_556.setObjectName("label_556")
        self.label_579 = QtWidgets.QLabel(self.frame_5)
        self.label_579.setGeometry(QtCore.QRect(892, 347, 45, 25))
        self.label_579.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_579.setText("")
        self.label_579.setAlignment(QtCore.Qt.AlignCenter)
        self.label_579.setObjectName("label_579")
        self.label_620 = QtWidgets.QLabel(self.frame_5)
        self.label_620.setGeometry(QtCore.QRect(1236, 370, 45, 25))
        self.label_620.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_620.setText("")
        self.label_620.setAlignment(QtCore.Qt.AlignCenter)
        self.label_620.setObjectName("label_620")
        self.label_536 = QtWidgets.QLabel(self.frame_5)
        self.label_536.setGeometry(QtCore.QRect(591, 324, 45, 25))
        self.label_536.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_536.setText("")
        self.label_536.setAlignment(QtCore.Qt.AlignCenter)
        self.label_536.setObjectName("label_536")
        self.label_474 = QtWidgets.QLabel(self.frame_5)
        self.label_474.setGeometry(QtCore.QRect(1064, 278, 45, 25))
        self.label_474.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_474.setText("")
        self.label_474.setAlignment(QtCore.Qt.AlignCenter)
        self.label_474.setObjectName("label_474")
        self.label_570 = QtWidgets.QLabel(self.frame_5)
        self.label_570.setGeometry(QtCore.QRect(677, 347, 45, 25))
        self.label_570.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_570.setText("")
        self.label_570.setAlignment(QtCore.Qt.AlignCenter)
        self.label_570.setObjectName("label_570")
        self.label_588 = QtWidgets.QLabel(self.frame_5)
        self.label_588.setGeometry(QtCore.QRect(28, 301, 141, 25))
        self.label_588.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_588.setText("")
        self.label_588.setAlignment(QtCore.Qt.AlignCenter)
        self.label_588.setObjectName("label_588")
        self.label_209 = QtWidgets.QLabel(self.frame_5)
        self.label_209.setGeometry(QtCore.QRect(1107, 25, 45, 25))
        self.label_209.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_209.setText("")
        self.label_209.setAlignment(QtCore.Qt.AlignCenter)
        self.label_209.setObjectName("label_209")
        self.label_539 = QtWidgets.QLabel(self.frame_5)
        self.label_539.setGeometry(QtCore.QRect(295, 324, 71, 25))
        self.label_539.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_539.setText("")
        self.label_539.setAlignment(QtCore.Qt.AlignCenter)
        self.label_539.setObjectName("label_539")
        self.label_595 = QtWidgets.QLabel(self.frame_5)
        self.label_595.setGeometry(QtCore.QRect(763, 324, 45, 25))
        self.label_595.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_595.setText("")
        self.label_595.setAlignment(QtCore.Qt.AlignCenter)
        self.label_595.setObjectName("label_595")
        self.label_217 = QtWidgets.QLabel(self.frame_5)
        self.label_217.setGeometry(QtCore.QRect(167, 25, 71, 25))
        self.label_217.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_217.setText("")
        self.label_217.setAlignment(QtCore.Qt.AlignCenter)
        self.label_217.setObjectName("label_217")
        self.label_356 = QtWidgets.QLabel(self.frame_5)
        self.label_356.setGeometry(QtCore.QRect(591, 140, 45, 25))
        self.label_356.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_356.setText("")
        self.label_356.setAlignment(QtCore.Qt.AlignCenter)
        self.label_356.setObjectName("label_356")
        self.label_419 = QtWidgets.QLabel(self.frame_5)
        self.label_419.setGeometry(QtCore.QRect(935, 209, 45, 25))
        self.label_419.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_419.setText("")
        self.label_419.setAlignment(QtCore.Qt.AlignCenter)
        self.label_419.setObjectName("label_419")
        self.label_472 = QtWidgets.QLabel(self.frame_5)
        self.label_472.setGeometry(QtCore.QRect(28, 255, 141, 25))
        self.label_472.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_472.setText("")
        self.label_472.setAlignment(QtCore.Qt.AlignCenter)
        self.label_472.setObjectName("label_472")
        self.label_628 = QtWidgets.QLabel(self.frame_5)
        self.label_628.setGeometry(QtCore.QRect(295, 370, 71, 25))
        self.label_628.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_628.setText("")
        self.label_628.setAlignment(QtCore.Qt.AlignCenter)
        self.label_628.setObjectName("label_628")
        self.label_206 = QtWidgets.QLabel(self.frame_5)
        self.label_206.setGeometry(QtCore.QRect(1021, 25, 45, 25))
        self.label_206.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_206.setText("")
        self.label_206.setAlignment(QtCore.Qt.AlignCenter)
        self.label_206.setObjectName("label_206")
        self.label_538 = QtWidgets.QLabel(self.frame_5)
        self.label_538.setGeometry(QtCore.QRect(548, 301, 45, 25))
        self.label_538.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_538.setText("")
        self.label_538.setAlignment(QtCore.Qt.AlignCenter)
        self.label_538.setObjectName("label_538")
        self.label_593 = QtWidgets.QLabel(self.frame_5)
        self.label_593.setGeometry(QtCore.QRect(0, 347, 30, 25))
        self.label_593.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_593.setAlignment(QtCore.Qt.AlignCenter)
        self.label_593.setObjectName("label_593")
        self.label_515 = QtWidgets.QLabel(self.frame_5)
        self.label_515.setGeometry(QtCore.QRect(0, 278, 30, 25))
        self.label_515.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_515.setAlignment(QtCore.Qt.AlignCenter)
        self.label_515.setObjectName("label_515")
        self.label_256 = QtWidgets.QLabel(self.frame_5)
        self.label_256.setGeometry(QtCore.QRect(1236, 48, 45, 25))
        self.label_256.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_256.setText("")
        self.label_256.setAlignment(QtCore.Qt.AlignCenter)
        self.label_256.setObjectName("label_256")
        self.label_508 = QtWidgets.QLabel(self.frame_5)
        self.label_508.setGeometry(QtCore.QRect(1064, 255, 45, 25))
        self.label_508.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_508.setText("")
        self.label_508.setAlignment(QtCore.Qt.AlignCenter)
        self.label_508.setObjectName("label_508")
        self.label_189 = QtWidgets.QLabel(self.frame_5)
        self.label_189.setGeometry(QtCore.QRect(28, 25, 141, 25))
        self.label_189.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_189.setText("")
        self.label_189.setAlignment(QtCore.Qt.AlignCenter)
        self.label_189.setObjectName("label_189")
        self.label_320 = QtWidgets.QLabel(self.frame_5)
        self.label_320.setGeometry(QtCore.QRect(1021, 94, 45, 25))
        self.label_320.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_320.setText("")
        self.label_320.setAlignment(QtCore.Qt.AlignCenter)
        self.label_320.setObjectName("label_320")
        self.label_441 = QtWidgets.QLabel(self.frame_5)
        self.label_441.setGeometry(QtCore.QRect(892, 163, 45, 25))
        self.label_441.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_441.setText("")
        self.label_441.setAlignment(QtCore.Qt.AlignCenter)
        self.label_441.setObjectName("label_441")
        self.label_376 = QtWidgets.QLabel(self.frame_5)
        self.label_376.setGeometry(QtCore.QRect(763, 163, 45, 25))
        self.label_376.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_376.setText("")
        self.label_376.setAlignment(QtCore.Qt.AlignCenter)
        self.label_376.setObjectName("label_376")
        self.label_407 = QtWidgets.QLabel(self.frame_5)
        self.label_407.setGeometry(QtCore.QRect(462, 186, 45, 25))
        self.label_407.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_407.setText("")
        self.label_407.setAlignment(QtCore.Qt.AlignCenter)
        self.label_407.setObjectName("label_407")
        self.label_512 = QtWidgets.QLabel(self.frame_5)
        self.label_512.setGeometry(QtCore.QRect(591, 278, 45, 25))
        self.label_512.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_512.setText("")
        self.label_512.setAlignment(QtCore.Qt.AlignCenter)
        self.label_512.setObjectName("label_512")
        self.label_460 = QtWidgets.QLabel(self.frame_5)
        self.label_460.setGeometry(QtCore.QRect(548, 232, 45, 25))
        self.label_460.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_460.setText("")
        self.label_460.setAlignment(QtCore.Qt.AlignCenter)
        self.label_460.setObjectName("label_460")
        self.label_304 = QtWidgets.QLabel(self.frame_5)
        self.label_304.setGeometry(QtCore.QRect(548, 94, 45, 25))
        self.label_304.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_304.setText("")
        self.label_304.setAlignment(QtCore.Qt.AlignCenter)
        self.label_304.setObjectName("label_304")
        self.label_434 = QtWidgets.QLabel(self.frame_5)
        self.label_434.setGeometry(QtCore.QRect(591, 209, 45, 25))
        self.label_434.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_434.setText("")
        self.label_434.setAlignment(QtCore.Qt.AlignCenter)
        self.label_434.setObjectName("label_434")
        self.label_238 = QtWidgets.QLabel(self.frame_5)
        self.label_238.setGeometry(QtCore.QRect(1064, 25, 45, 25))
        self.label_238.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_238.setText("")
        self.label_238.setAlignment(QtCore.Qt.AlignCenter)
        self.label_238.setObjectName("label_238")
        self.label_268 = QtWidgets.QLabel(self.frame_5)
        self.label_268.setGeometry(QtCore.QRect(1064, 71, 45, 25))
        self.label_268.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_268.setText("")
        self.label_268.setAlignment(QtCore.Qt.AlignCenter)
        self.label_268.setObjectName("label_268")
        self.label_502 = QtWidgets.QLabel(self.frame_5)
        self.label_502.setGeometry(QtCore.QRect(935, 232, 45, 25))
        self.label_502.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_502.setText("")
        self.label_502.setAlignment(QtCore.Qt.AlignCenter)
        self.label_502.setObjectName("label_502")
        self.label_402 = QtWidgets.QLabel(self.frame_5)
        self.label_402.setGeometry(QtCore.QRect(1150, 186, 45, 25))
        self.label_402.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_402.setText("")
        self.label_402.setAlignment(QtCore.Qt.AlignCenter)
        self.label_402.setObjectName("label_402")
        self.label_382 = QtWidgets.QLabel(self.frame_5)
        self.label_382.setGeometry(QtCore.QRect(548, 163, 45, 25))
        self.label_382.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_382.setText("")
        self.label_382.setAlignment(QtCore.Qt.AlignCenter)
        self.label_382.setObjectName("label_382")
        self.label_263 = QtWidgets.QLabel(self.frame_5)
        self.label_263.setGeometry(QtCore.QRect(634, 48, 45, 25))
        self.label_263.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_263.setText("")
        self.label_263.setAlignment(QtCore.Qt.AlignCenter)
        self.label_263.setObjectName("label_263")
        self.label_298 = QtWidgets.QLabel(self.frame_5)
        self.label_298.setGeometry(QtCore.QRect(763, 94, 45, 25))
        self.label_298.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_298.setText("")
        self.label_298.setAlignment(QtCore.Qt.AlignCenter)
        self.label_298.setObjectName("label_298")
        self.label_197 = QtWidgets.QLabel(self.frame_5)
        self.label_197.setGeometry(QtCore.QRect(0, 2, 30, 25))
        self.label_197.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_197.setAlignment(QtCore.Qt.AlignCenter)
        self.label_197.setObjectName("label_197")
        self.label_282 = QtWidgets.QLabel(self.frame_5)
        self.label_282.setGeometry(QtCore.QRect(28, 71, 141, 25))
        self.label_282.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_282.setText("")
        self.label_282.setAlignment(QtCore.Qt.AlignCenter)
        self.label_282.setObjectName("label_282")
        self.label_275 = QtWidgets.QLabel(self.frame_5)
        self.label_275.setGeometry(QtCore.QRect(935, 71, 45, 25))
        self.label_275.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_275.setText("")
        self.label_275.setAlignment(QtCore.Qt.AlignCenter)
        self.label_275.setObjectName("label_275")
        self.label_387 = QtWidgets.QLabel(self.frame_5)
        self.label_387.setGeometry(QtCore.QRect(634, 163, 45, 25))
        self.label_387.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_387.setText("")
        self.label_387.setAlignment(QtCore.Qt.AlignCenter)
        self.label_387.setObjectName("label_387")
        self.label_527 = QtWidgets.QLabel(self.frame_5)
        self.label_527.setGeometry(QtCore.QRect(505, 301, 45, 25))
        self.label_527.setStyleSheet("font: 18pt \"FC Galaxy\";\n"
"border-radius: 0px;\n"
"background:rgb(255, 255, 255);\n"
"color:rgb(170, 170, 127);\n"
"border: 2px solid rgb(170, 170, 127)")
        self.label_527.setText("")
        self.label_527.setAlignment(QtCore.Qt.AlignCenter)
        self.label_527.setObjectName("label_527")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(830, 105, 113, 22))
        self.dateEdit.setStyleSheet("background:rgb(255, 255, 255);\n"
"font: 18pt \"FC Galaxy\";\n"
"color : rgb(170, 170, 127);\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.frame_5.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_16.raise_()
        self.lineEdit_17.raise_()
        self.lineEdit_18.raise_()
        self.lineEdit_20.raise_()
        self.lineEdit_21.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.dateEdit.raise_()
        self.verticalLayout_5.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.content_bar)
        self.credits_bar = QtWidgets.QFrame(self.GNG_Gauge_frame)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_label_credits.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_label_credits)
        self.label_4.setMinimumSize(QtCore.QSize(21, 21))
        self.label_4.setMaximumSize(QtCore.QSize(21, 21))
        self.label_4.setStyleSheet("image: url(:/image/Sunmipol_logo.png);")
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
        self.content_bar.raise_()
        self.credits_bar.raise_()
        self.title_bar.raise_()
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


        self.min.setValidator(QDoubleValidator(0.99,99.99,2))
        self.max.setValidator(QDoubleValidator(0.99,99.99,2))
        self.amount.setValidator(QDoubleValidator(0.99,99.99,2))


        self.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_maximize.clicked.connect(lambda: self.minizie_or_maximize_window())
        self.btn_close.clicked.connect(lambda: self.close())

        #navigate to Home page
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Tool1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Tool2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Tool3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Tool4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Tool5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Tool6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
                     


    def minizie_or_maximize_window(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            GLOBAL_STATE = 1
            self.showMaximized()
            self.GNG_Gauge_frame_Layer.setContentsMargins(0, 0, 0, 0)
            self.GNG_Gauge_frame.setStyleSheet("background-color : rgb(56, 58, 89); color : rgb(220, 220, 220); border-radius: 0px;")
            
            # SET GLOBAL TO 1
                       
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.GNG_Gauge_frame_Layer.setContentsMargins(0, 0, 0, 0)
            self.GNG_Gauge_frame.setStyleSheet("background-color : rgb(56, 58, 89); color : rgb(220, 220, 220); border-radius: 10px;")
            



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GO-NOGO"))
        self.label_title.setText(_translate("MainWindow", "GO NOGO Test"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "USER"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.checkBox.setText(_translate("MainWindow", "Remember User"))
        self.pushButton.setText(_translate("MainWindow", "CONNECT TO Sumipol"))
        self.NotPass.setText(_translate("MainWindow", "0"))
        self.showText_3.setText(_translate("MainWindow", "ผ่าน"))
        self.Pass.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "ค่า Max"))
        self.label_6.setText(_translate("MainWindow", "ค่าที่วัดได้"))
        self.cancel.setText(_translate("MainWindow", "ยกเลิก"))
        self.showText_5.setText(_translate("MainWindow", "จำนวนชิ้นงาน"))
        self.showText_4.setText(_translate("MainWindow", "ไม่ผ่าน"))
        self.PassORnotPass.setText(_translate("MainWindow", "ผ่าน/ไม่ผ่าน"))
        self.value.setText(_translate("MainWindow", "0"))
        self.process.setText(_translate("MainWindow", "เริ่มคำนวณ"))
        self.showText_2.setText(_translate("MainWindow", "คุณภาพ"))
        self.label.setText(_translate("MainWindow", "จำนวนชิ้นงาน"))
        self.total.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "ค่า Min"))
        self.Report.setText(_translate("MainWindow", "Creat Report"))
        self.label_9.setText(_translate("MainWindow", "Document Name"))
        self.label_11.setText(_translate("MainWindow", "Part Name"))
        self.label_12.setText(_translate("MainWindow", "Process"))
        self.label_13.setText(_translate("MainWindow", "Material"))
        self.label_14.setText(_translate("MainWindow", "Drawing No."))
        self.label_15.setText(_translate("MainWindow", "Department"))
        self.label_16.setText(_translate("MainWindow", "Section"))
        self.label_17.setText(_translate("MainWindow", "Customer Part No."))
        self.label_18.setText(_translate("MainWindow", "Customer"))
        self.label_19.setText(_translate("MainWindow", "TMT Part No."))
        self.label_30.setText(_translate("MainWindow", "Revision"))
        self.label_31.setText(_translate("MainWindow", "Page"))
        self.label_33.setText(_translate("MainWindow", "Reference"))
        self.label_34.setText(_translate("MainWindow", "Date of Production"))
        self.label_35.setText(_translate("MainWindow", "Machine No."))
        self.label_36.setText(_translate("MainWindow", "Checked By"))
        self.label_37.setText(_translate("MainWindow", "Approved By"))
        self.label_38.setText(_translate("MainWindow", "Lot Number"))
        self.label_39.setText(_translate("MainWindow", "Prepared"))
        self.label_573.setText(_translate("MainWindow", "13"))
        self.label_188.setText(_translate("MainWindow", "Description"))
        self.label_219.setText(_translate("MainWindow", "9"))
        self.label_221.setText(_translate("MainWindow", "13"))
        self.label_208.setText(_translate("MainWindow", "8"))
        self.label_213.setText(_translate("MainWindow", "Max"))
        self.label_495.setText(_translate("MainWindow", "10"))
        self.label_207.setText(_translate("MainWindow", "12"))
        self.label_211.setText(_translate("MainWindow", "18"))
        self.label_437.setText(_translate("MainWindow", "9"))
        self.label_619.setText(_translate("MainWindow", "16"))
        self.label_212.setText(_translate("MainWindow", "15"))
        self.label_509.setText(_translate("MainWindow", "11"))
        self.label_417.setText(_translate("MainWindow", "7"))
        self.label_187.setText(_translate("MainWindow", "11"))
        self.label_236.setText(_translate("MainWindow", "5"))
        self.label_201.setText(_translate("MainWindow", "16"))
        self.label_226.setText(_translate("MainWindow", "6"))
        self.label_287.setText(_translate("MainWindow", "3"))
        self.label_228.setText(_translate("MainWindow", "19"))
        self.label_260.setText(_translate("MainWindow", "2"))
        self.label_339.setText(_translate("MainWindow", "4"))
        self.label_237.setText(_translate("MainWindow", "Min"))
        self.label_224.setText(_translate("MainWindow", "7"))
        self.label_199.setText(_translate("MainWindow", "1"))
        self.label_215.setText(_translate("MainWindow", "10"))
        self.label_230.setText(_translate("MainWindow", "14"))
        self.label_353.setText(_translate("MainWindow", "5"))
        self.label_587.setText(_translate("MainWindow", "14"))
        self.label_227.setText(_translate("MainWindow", "Tool"))
        self.label_214.setText(_translate("MainWindow", "17"))
        self.label_200.setText(_translate("MainWindow", "1"))
        self.label_359.setText(_translate("MainWindow", "6"))
        self.label_229.setText(_translate("MainWindow", "4"))
        self.label_431.setText(_translate("MainWindow", "8"))
        self.label_196.setText(_translate("MainWindow", "2"))
        self.label_193.setText(_translate("MainWindow", "3"))
        self.label_593.setText(_translate("MainWindow", "15"))
        self.label_515.setText(_translate("MainWindow", "12"))
        self.label_197.setText(_translate("MainWindow", "No."))
 


