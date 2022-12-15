
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

class cssden(QMainWindow,main.Ui_MainWindow):
    def __init__(self):
        super().__init__()


        self.mwidget = QMainWindow(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
       
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):











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


    def minizie_or_maximize_window(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            GLOBAL_STATE = 1
            self.showMaximized()
            # SET GLOBAL TO 1
                       
        else:
            GLOBAL_STATE = 0
            self.showNormal()






if __name__ == "__main__":
    
   
    
    app = QApplication(sys.argv)
    # app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
    MainWindow = QtWidgets.QMainWindow()


    ex = cssden()
    sys.exit(app.exec_())
