#QTextEdit控件使用

import sys
from  PyQt5.QtWidgets import QPushButton,QApplication,QMainWindow,QLineEdit,QFormLayout,QWidget,QTextEdit,QVBoxLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator,QFont
from PyQt5.QtCore import  QRegExp,Qt
class QLineEditDemo(QWidget):
    def __init__(self,parent=None):
        super(QLineEditDemo,self).__init__(parent)

        self.setWindowTitle("QTextEdit控件使用")
        self.resize(500,600)
        self.layout=QVBoxLayout()

        self.textEdit=QTextEdit()
        btn_1=QPushButton("显示文本")
        btn_2=QPushButton("显示HTML")
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(btn_1)
        self.layout.addWidget(btn_2)

        self.setLayout(self.layout)

        btn_1.clicked.connect(self.fn_1)
        btn_2.clicked.connect(self.fn_2)


    def fn_1(self):
        self.textEdit.setPlainText("Hello PyQT5单击按钮")

    def fn_2(self):
        self.textEdit.setHtml("<font color='red' size='20'>HELLO!</font>")

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=QLineEditDemo()
    win.show()
    sys.exit(app.exec_())