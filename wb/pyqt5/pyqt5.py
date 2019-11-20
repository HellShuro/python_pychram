# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QToolTip, QPushButton,QMessageBox,QDesktopWidget,QHBoxLayout,QVBoxLayout,QTextEdit,QLineEdit,QGridLayout,QLabel,QLCDNumber,QSlider
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication,Qt

class add_application(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        # 设置窗口位置,大小
        # self.setGeometry(300,300,300,220)
        self.resize(400,150)

        # 将窗口设置在屏幕中间
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        # 一下这句不知道啥意思,但是去掉没有影响
        self.move(qr.topLeft())

        # 设置窗口标题,窗口icon
        self.setWindowTitle("rwa字符串转化成json文本")
        self.setWindowIcon(QIcon('../resource/wb_icon.png'))

        # 设置文本字体类型
        # QToolTip.setFont(QFont('SansSerif',10))

        # # 创建一个按钮
        # btn = QPushButton('提交',self)
        # btn.resize(btn.sizeHint())
        # # 创建一个关闭按钮
        # btn = QPushButton('退出',self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.move(100,100)
        # =====================================================
        # 使用水平定位和纵向定位,设置按钮
        ok = QPushButton('O!K')
        no = QPushButton("NO")

        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(no)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # self.setLayout(vbox)
        # =================================================
        # 创建文本输入框
        raw = QLabel('raw_text')
        raw_edit = QLineEdit()
        # 文本编辑器
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(raw, 1, 0)
        grid.addWidget(raw_edit, 1, 1)
        self.setLayout(grid)

        # ======================================================
        # 制作一个数字显示器,和一个滑块,并且关联起来
        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)

        # vbox = QVBoxLayout()
        # vbox.addWidget(lcd)
        # vbox.addWidget(sld)

        # self.setLayout(vbox)

        # sld.valueChanged.connect(lcd.display)

        # self.setGeometry(300, 300, 250, 150)
        # self.setWindowTitle('Signal & slot')

        # ===============================================

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')


        self.show()



    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        self.show()

    def closeEvent(self, QCloseEvent):
        # 创建一个有提示的关闭按钮
        reply = QMessageBox.question(self, '提示', "确认退出?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_application()
    sys.exit(app.exec_())