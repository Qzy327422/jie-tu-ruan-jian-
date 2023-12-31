from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QAction, QVBoxLayout, QWidget, QFileDialog, QLabel, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, Qt
import pyautogui
import os
import datetime
import webbrowser

qzy_3 = ""
qzy_2 = True


def qzy_1(url):
    webbrowser.open(url)


def qzy_4():
    global qzy_2, qzy_3
    qzy_2 = True
    directory = QFileDialog.getExistingDirectory(window, "选择保存路径")
    if directory:
        qzy_3 = directory
        qzy_5.setText("保存路径：" + directory)


def qzy_6():
    if qzy_3:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"qzy-截图_{timestamp}.png"
        file_path = os.path.join(qzy_3, filename)
        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)


class Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        qzy_6()
        self.finished.emit()


def qzy_2():
    worker = Worker()
    worker.finished.connect(qzy_7)
    worker.run()


def qzy_7():
    pass


def qzy_8():
    app.quit()


def qzy_9():
    msg_box = QMessageBox()
    msg_box.setText("点nm的，老子就是懒得添加")
    msg_box.exec_()


app = QApplication([])
window = QMainWindow()
window.setWindowTitle("截图-by qzy")
window.setGeometry(100, 100, 400, 300)
central_widget = QWidget(window)
layout = QVBoxLayout(central_widget)
qzy_5 = QLabel("保存路径：")
layout.addWidget(qzy_5)
layout.setAlignment(Qt.AlignTop)
button_data = [
    {"text": "截图", "function": qzy_2},
    {"text": "选择保存路径", "function": qzy_4},
    {"text": "退出", "function": qzy_8}
]
for data in button_data:
    button = QPushButton(data["text"])
    button.clicked.connect(data["function"])
    layout.addWidget(button)
    button.setFixedHeight(70)
window.setCentralWidget(central_widget)
qzy_10 = window.menuBar()
qzy_11 = qzy_10.addMenu("简介")
new_action = QAction("作者：qzy Q：3152379317", window)
new_action.triggered.connect(
    lambda: qzy_1("http://3152379317.qzone.qq.com"))
qzy_11.addAction(new_action)
edit_menu = qzy_10.addMenu("选项")
cut_action = QAction("待添加", window)
cut_action.triggered.connect(qzy_9)
edit_menu.addAction(cut_action)
window.show()
app.exec_()
