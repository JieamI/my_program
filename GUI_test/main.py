from PyQt5 import QtCore,QtWidgets,QtGui
import GUI

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = GUI.Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
