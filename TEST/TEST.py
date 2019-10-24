import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QInputDialog示例')
        self.setWindowIcon(QIcon(r'%s\4.图标素材\chuan.ico' % path))
        self.setGeometry(600, 300, 350, 200)

        btn_str = QPushButton('获得字符串')
        btn_int = QPushButton('获得整数')
        btn_item = QPushButton('获得列表选项')
        self.lineEdit_str = QLineEdit()
        self.lineEdit_int = QLineEdit()
        self.lineEdit_item = QLineEdit()

        vbx1 = QVBoxLayout()
        vbx1.addWidget(btn_int)
        vbx1.addWidget(btn_item)
        vbx1.addWidget(btn_str)

        vbx2 = QVBoxLayout()
        vbx2.addWidget(self.lineEdit_int)
        vbx2.addWidget(self.lineEdit_item)
        vbx2.addWidget(self.lineEdit_str)

        hbx = QHBoxLayout()
        hbx.addLayout(vbx1)
        hbx.addLayout(vbx2)
        self.setLayout(hbx)

        btn_item.clicked.connect(self.getItem)
        btn_int.clicked.connect(self.getInt)
        btn_str.clicked.connect(self.getStr)

    def getItem(self):
        items = ['装载机', '平地机', '推土机', '挖掘机', '自卸车']  # 这里设置成列表或元组都可以
        item, ok = QInputDialog.getItem(self, '选择项目', '请选择您的需求', items, 0, False)
        if ok and item:
            self.lineEdit_item.setText(item)

    def getInt(self):
        # num,ok = QInputDialog.getDouble(self,'双精度','输入您得数字')
        num, ok = QInputDialog.getInt(self, '获取整数', '输入您的数字(-10～10)', 0, -10, 10, 1)
        if ok:
            self.lineEdit_int.setText(str(num))

    def getStr(self):
        str, ok = QInputDialog.getText(self, '获取字符串', '请输入您的文本', QLineEdit.Normal, '字符串', )
        if ok:
            self.lineEdit_str.setText(str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
