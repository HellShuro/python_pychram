# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QToolTip, QPushButton,QMessageBox,QDesktopWidget,QHBoxLayout,QVBoxLayout,QTextEdit,QLineEdit,QGridLayout,QLabel,QLCDNumber,QSlider

from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication,Qt

class raw_json(QWidget):
    def __init__(self):
        super().__init__()

        self.UI_raw_json()

    def UI_raw_json(self):
        # 创建窗口,设置大小位置
        self.resize(400,200)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 设置内部基础信息
        self.setWindowTitle('raw转json')
        self.setWindowIcon(QIcon('../resource/wb_icon.png'))

        # 增加一行文本输入行
        # 增加转换按钮
        # 增加大文本编辑输入框
        input_raw = QLabel("raw")
        self.raw_edit = QLineEdit()
        self.json_out = QTextEdit()
        btn = QPushButton('转换')

        grid = QGridLayout()
        grid.setSpacing(10)
        btn.clicked.connect(self.click_change)

        grid.addWidget(input_raw, 1, 0)
        grid.addWidget(self.raw_edit, 1, 1)
        grid.addWidget(btn,1,2)
        grid.addWidget(self.json_out,2,1)

        self.setLayout(grid)

        self.show()

    def click_change(self):
        # 获取行输入的内容
        sender = self.raw_edit.text()




        # 输出变更内容到textedit
        self.json_out.setPlainText(sender)

        self.show()

    def closeEvent(self,QCloseEvent, *args, **kwargs):
        # 创建一个有提示的关闭按钮
        reply = QMessageBox.question(self, '提示', "确认退出?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = raw_json()
    sys.exit(app.exec_())