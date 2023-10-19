import sys
from threading import Thread
from time import sleep

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLineEdit, 
    QListWidget, 
    QPushButton
)

from core import*

class Chat(QWidget):
    def __init__(self) -> None:
        super().__init__()
        Thread(target=self.__updateList).start()
        self.message = Message()
        self.setWindowTitle("NajotGram")
        self.setFixedSize(500, 500)
        self.__initUI()
        self.__css()
        self.show()

    def __initUI(self):
        self.vBox = QVBoxLayout()
        self.hBox = QHBoxLayout()

        self.editName = QLineEdit()
        self.editName.setPlaceholderText('Enter username...')

        self.qlwMessange = QListWidget()
        self.editMsg = QLineEdit()
        self.editMsg.setPlaceholderText('Enter message...')

        self.btnSend = QPushButton('send')

        self.hBox.addWidget(self.editMsg)
        self.hBox.addWidget(self.btnSend)

        self.vBox.addWidget(self.editName)
        self.vBox.addWidget(self.qlwMessange)
        self.vBox.addLayout(self.hBox)

        self.btnSend.clicked.connect(self.__updateMessage)

        self.setLayout(self.vBox)

    def __css(self):
        self.setStyleSheet('font-size: 20px')

    def __updateMessage(self):
        name = self.editName.text()
        msg = self.editMsg.text()
        self.message.send(name, msg)
        # self.__updateList()
        self.editMsg.clear()

    def __updateList(self):
        while True:
            sleep(1)    
            self.qlwMessange.clear()
            data = self.message.getAll()
            for i in data:
                row = '%s %s %s' %(i.get('time'), i.get('name'), i.get('msg'))
                self.qlwMessange.addItem(row)



app = QApplication(sys.argv)
win = Chat()
sys.exit(app.exec_())