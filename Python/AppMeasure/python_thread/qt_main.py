from PyQt5 import QtWidgets, QtGui, QtCore
import qt_genarate as main
import sys
import time

class Activity(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bindWidget()
        self.show()
        


    def bindWidget(self):

        self.btn_nothread.clicked.connect(self.on_clickNoThread)
        self.btn_havethread.clicked.connect(self.on_clickHaveThread)

    def on_clickNoThread(self):
        self.lb_result.setText("กำลังโหลด.")
        time.sleep(1)
        self.progressBar.setValue(20)
        time.sleep(1)
        self.progressBar.setValue(40)
        time.sleep(1)
        self.progressBar.setValue(60)
        time.sleep(1)
        self.progressBar.setValue(80)
        time.sleep(1)
        self.progressBar.setValue(100)
        self.lb_result.setText("Finish NoThread")

    def on_clickHaveThread(self):
        self.thread = BackgroundThread()
        self.thread.start()
        self.thread.result.connect(self.HaveThread)
        self.thread.countProgressBar.connect(self.updateProgressBar)

    def HaveThread(self,result):
        self.lb_result.setText(result)

    def updateProgressBar(self, count):
        self.progressBar.setValue(count)


class BackgroundThread(QtCore.QThread):

    result = QtCore.pyqtSignal(str)
    countProgressBar = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        self.result.emit("กำลังโหลด.")
        time.sleep(1)
        self.countProgressBar.emit(20)
        time.sleep(1)
        self.countProgressBar.emit(40)
        time.sleep(1)
        self.countProgressBar.emit(60)
        time.sleep(1)
        self.countProgressBar.emit(80)
        time.sleep(1)
        self.countProgressBar.emit(100)
        self.result.emit("Finish HaveThread")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    maina = Activity()
    sys.exit(app.exec_())
