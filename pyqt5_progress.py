import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLineEdit, QListWidget, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
from core import Massage


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Init()
    
    def Init(self):
        self.setStyleSheet("background-color: white;")
        self.setFixedSize(600, 700)
        
        self.line_name = QLineEdit(self)
        self.line_maassage = QLineEdit(self)
        self.list_widget = QListWidget(self)
        self.btn_send = QPushButton("Send", self)
        
        self.line_name.setPlaceholderText("Enter your name")
        self.line_maassage.setPlaceholderText("Enter your message")
        
        self.qv_box = QVBoxLayout()
        self.qh2_box = QHBoxLayout()
        self.qh_box = QHBoxLayout()
        
        self.qv_box.addWidget(self.line_name)
        self.qv_box.addWidget(self.list_widget)
        self.qh2_box.addWidget(self.line_maassage)
        self.qh2_box.addWidget(self.btn_send)
        self.qv_box.addLayout(self.qh2_box)
        
        self.qh_box.addLayout(self.qv_box)
        self.setLayout(self.qh_box)
        
        self.btn_send.clicked.connect(lambda : Massage().send)
        
        
      
      
      
app = QApplication([])
win = Window()
win.show()
app.exec_()  