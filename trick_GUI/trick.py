from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QMessageBox
from PyQt5.QtCore import *
import random
import sys



class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(180, 70, 430, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self._True)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 360, 93, 28))
        self.pushButton_2.setStyleSheet("color: rgb(255, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.installEventFilter(self)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "你愿意做我女朋友吗？"))
        self.pushButton.setText(_translate("Form", "同意"))
        self.pushButton_2.setText(_translate("Form", "不同意"))



    #重写窗口事件过滤器
    def eventFilter(self,object,event):
        if object == self.pushButton_2:
            if event.type() == QEvent.Enter:
                self.Move()
        return QWidget.eventFilter(self,object,event)
    
    #同意时
    def _True(self):
        QMessageBox.information(self,'哈哈',"愚人节快乐~")
        sys.exit()

    #重写窗口关闭函数
    def closeEvent(self,event):
         reply = QMessageBox.question(self,"关闭","确定退出么？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
         if reply == QMessageBox.Yes:
             QMessageBox.warning(self, "呵呵", "不同意你跑得了吗~")
         else:
             QMessageBox.warning(self, "嗯嗯~", "这就对了嘛~")
         event.ignore()

    def Move(self):
        if self.pushButton_2.pos() == QPoint(330,360):
            self.anim = QtCore.QPropertyAnimation(self.pushButton_2,b"geometry")
            self.x = random.randint(0,707)
            self.y = random.randint(0,572)
            self.anim.setDuration(100)
            self.anim.setStartValue(QtCore.QRect(330, 360, 93, 28))
            self.anim.setEndValue(QtCore.QRect(self.x, self.y, 93, 28))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()
        elif self.pushButton_2.pos() == QPoint(self.x,self.y):
            self.anim = QtCore.QPropertyAnimation(self.pushButton_2,b"geometry")
            self.anim.setDuration(100)
            self.anim.setStartValue(QtCore.QRect(self.x, self.y, 93, 28))
            self.x = random.randint(0,707)
            self.y = random.randint(0,572)
            self.anim.setEndValue(QtCore.QRect(self.x, self.y, 93, 28))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())

