import sys,os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
import sys
import QQrc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(534, 410)
        Form.setMinimumSize(QtCore.QSize(534, 410))
        Form.setMaximumSize(QtCore.QSize(534, 410))
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label = new_QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -5, 534, 410))
        self.label.setText("")
        self.gif = QMovie('out.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 534, 265))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 210, 280, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setAttribute(Qt.WA_TranslucentBackground)
        self.lineEdit =  new_QLineEdit1(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 210, 255, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(199, 199, 199);\n"
"border-width:1;\n"
"border-style:solid")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.editingFinished.connect(self.toggle_label1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 210, 22, 35))
        self.label_3.setStyleSheet("border-image: url(:/resource/QQGui_resource/账号-灰.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(120, 256, 22, 35))
        self.label_4.setStyleSheet("border-image: url(:/resource/QQGui_resource/密码-灰.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 =  new_QLineEdit2(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 255, 280, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(199, 199, 199);\n"
"border-width:1;\n"
"border-style:solid")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.editingFinished.connect(self.toggle_label2)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(122, 300, 115, 19))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(150, 150, 150)")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.installEventFilter(Form)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(238, 300, 115, 19))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("color: rgb(150, 150, 150)")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.installEventFilter(Form)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 370, 93, 28))
        font = QtGui.QFont()

        font.setFamily("Century Gothic")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/resource/QQGui_resource/白.png);color: rgb(150, 150, 150)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.installEventFilter(Form)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(344, 295, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(:/resource/QQGui_resource/白.png);color: rgb(150, 150, 150)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.installEventFilter(Form)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(490, 360, 36, 40))
        self.toolButton.setStyleSheet("border-image: url(:/resource/QQGui_resource/二维码.png);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = new_QToolButton2(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(465, 5, 30, 25))
        self.toolButton_2.setStyleSheet("border-image: url(:/resource/QQGui_resource/最小化.png)")
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(Form.showMinimized)
        self.toolButton_3 = new_QToolButton1(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(497, 5, 32, 25))
        self.toolButton_3.setStyleSheet("border-image: url(:/resource/QQGui_resource/关闭.png);")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(Form.close)
        self.toolButton_x = QtWidgets.QToolButton(Form) 
        self.toolButton_x.setGeometry(QtCore.QRect(237, 116, 56, 56))
        self.toolButton_x.setStyleSheet("border-image: url(:/resource/QQGui_resource/加号.png)")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(225, 104, 80, 80))
        self.toolButton_4.setStyleSheet("border-image: url(:/resource/QQGui_resource/头像.png);")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.setMouseTracking(True)
        self.toolButton_4.installEventFilter(Form)
        self.toolButton_5 = QtWidgets.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(392, 258, 28, 28))
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet("border-image: url(:/resource/QQGui_resource/软键盘.png);")
        self.toolButton_5.setText("")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(Form)
        self.toolButton_6.setGeometry(QtCore.QRect(120, 338, 297, 43))
        self.toolButton_6.setStyleSheet("border-image: url(:/resource/QQGui_resource/登录按钮.png);")
        self.toolButton_6.setText("")
        self.toolButton_6.setObjectName("toolButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "QQ号码/手机/邮箱"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "自动登录"))
        self.checkBox_2.setText(_translate("Form", "记住密码"))
        self.pushButton.setText(_translate("Form", "注册账号"))
        self.pushButton_2.setText(_translate("Form", "找回密码"))

    
    #动画效果    
    def animation_enter(self):
        self.anim = QtCore.QPropertyAnimation(self.toolButton_x,b'geometry')
        self.anim.setDuration(150)
        self.anim.setStartValue(QtCore.QRect(237, 116, 56, 56))
        self.anim.setEndValue(QtCore.QRect(340, 116, 56, 56))
        self.anim.start()


    def animation_leave(self):
        self.anim = QtCore.QPropertyAnimation(self.toolButton_x,b'geometry')
        self.anim.setDuration(150)
        self.anim.setStartValue(QtCore.QRect(340, 116, 56, 56))
        self.anim.setEndValue(QtCore.QRect(237, 116, 56, 56))
        self.anim.start()

    def toggle_label1(self):
        self.label_3.setStyleSheet("border-image: url(:/resource/QQGui_resource/账号-灰.png)")

    def toggle_label2(self):
        self.label_4.setStyleSheet("border-image: url(:/resource/QQGui_resource/密码-灰.png)")


    
       


    

#重写窗体事件过滤器
class new_QWidget(QtWidgets.QWidget):
    def eventFilter(self,object,event):
        if object == ui.toolButton_4:
            if event.type() == QEvent.Enter:
                ui.animation_enter()
            elif event.type() == QEvent.Leave:
                ui.animation_leave()
        elif object == ui.checkBox:
            if  event.type() == QEvent.Enter:
                ui.checkBox.setStyleSheet("color: rgb(90, 90, 90)")
            elif event.type() == QEvent.Leave:
                ui.checkBox.setStyleSheet("color: rgb(150, 150, 150)")
        elif object == ui.checkBox_2:
            if  event.type() == QEvent.Enter:
                ui.checkBox_2.setStyleSheet("color: rgb(90, 90, 90)")
            elif event.type() == QEvent.Leave:
                ui.checkBox_2.setStyleSheet("color: rgb(150, 150, 150)")
        elif object == ui.pushButton:
            if  event.type() == QEvent.Enter:
                ui.pushButton.setStyleSheet("border-image: url(:/resource/QQGui_resource/白.png);color: rgb(90, 90, 90)")
            elif event.type() == QEvent.Leave:
                ui.pushButton.setStyleSheet("border-image: url(:/resource/QQGui_resource/白.png);color: rgb(150, 150, 150)")
        elif object == ui.pushButton_2:
            if  event.type() == QEvent.Enter:
                ui.pushButton_2.setStyleSheet("border-image: url(:/resource/QQGui_resource/白.png);color: rgb(90, 90, 90)")
            elif event.type() == QEvent.Leave:
                ui.pushButton_2.setStyleSheet("border-image: url(:/resource/QQGui_resource/白.png);color: rgb(150, 150, 150)")
        return QWidget.eventFilter(self,object,event)

#重写关闭按钮
class new_QToolButton1(QToolButton):                
    def enterEvent(self,event):
        self.setStyleSheet("background-color: rgb(255, 93, 61);border-image: url(:/resource/QQGui_resource/关闭.png)")
    def leaveEvent(self,event):
        self.setStyleSheet("border-image: url(:/resource/QQGui_resource/关闭.png)")

#重写最小化按钮  
class new_QToolButton2(QToolButton):               
    def enterEvent(self,event):
        self.setStyleSheet("background-color: rgba(118, 255, 81, 100);border-image: url(:/resource/QQGui_resource/最小化.png)")
    def leaveEvent(self,event):
        self.setStyleSheet("border-image: url(:/resource/QQGui_resource/最小化.png)")

#重写账号输入框
class new_QLineEdit1(QLineEdit):
    def mousePressEvent(self,event):
        ui.label_3.setStyleSheet("border-image: url(:/resource/QQGui_resource/账号-蓝.png)")

#重写密码输入框
class new_QLineEdit2(QLineEdit):
    def mousePressEvent(self,event):
        ui.label_4.setStyleSheet("border-image: url(:/resource/QQGui_resource/密码-蓝.png)")

#重写标签事件&重写窗口移动函数
class new_QLabel(QLabel):
    def mousePressEvent(self,QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos =  QPoint(QMouseEvent.x(), QMouseEvent.y())
            
        
        
        ui.label_3.setStyleSheet("border-image: url(:/resource/QQGui_resource/账号-灰.png)")
        ui.label_4.setStyleSheet("border-image: url(:/resource/QQGui_resource/密码-灰.png)")
    
        
    def mouseMoveEvent(self, QMouseEvent):
        if self._isTracking:
            _endPos = QMouseEvent.pos() - self._startPos
            Form.move(Form.pos()+_endPos)

            
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
                self._isTracking = False
                self._startPos = None
                self._endPos = None
            
        
##################################################################################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form =  new_QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    






    
