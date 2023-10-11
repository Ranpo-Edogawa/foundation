import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
# from qtwidgets import PasswordEdit

from core import *


class Window(QWidget):

    
    def __init__(self):

        super().__init__()

        self.setFixedSize(600,400)
        self.setWindowTitle('Menu')
        self.__initUI()
        self.show()


    def __initUI(self):

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.btnCreateUser = QPushButton('Create new user')
        self.btnReadUsers = QPushButton('List of users')
        self.btnUpdateUser = QPushButton('Update user')
        self.btnDeleteUser = QPushButton('Delete user')

        self.vBox.addStretch()
        self.vBox.addWidget(self.btnCreateUser)
        self.vBox.addWidget(self.btnReadUsers)
        self.vBox.addWidget(self.btnUpdateUser)
        self.vBox.addWidget(self.btnDeleteUser)
        self.vBox.addStretch()

        self.setLayout(self.vBox)

        self.btnCreateUser.clicked.connect(self.showCreateWindow)
        self.btnReadUsers.clicked.connect(self.showListUsersWindow)
        self.btnUpdateUser.clicked.connect(self.showUpdateWindow)
        self.btnDeleteUser.clicked.connect(self.showDeleteWindow)


    def showCreateWindow(self):
        self.close()
        self.cU = CreateUserWindow()


    def showListUsersWindow(self):
        self.close()
        self.rUs = ListUsersWindow()


    def showUpdateWindow(self):
        self.close()
        self.uU = UpdateUserWindow()   


    def showDeleteWindow(self):
        self.close()
        self.dU = DeleteUserWindow() 



class CreateUserWindow(QWidget):
 
 
    def __init__(self):

        super().__init__()
        self.core = Core()
        self.setFixedSize(600,400)
        self.setWindowTitle('Create user')
        self.__initUI()
        self.show()


    def __initUI(self):

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.editFullName = QLineEdit()
        self.editFullName.setPlaceholderText('Full Name')
        self.editUserName = QLineEdit()
        self.editUserName.setPlaceholderText('Username')
        # self.editPassword = PasswordEdit()
        self.editPassword.setPlaceholderText('Password')
        self.editMobileNumber = QLineEdit()
        self.editMobileNumber.setPlaceholderText('Mobile Number')

        self.labelMsg = QLabel()

        self.btnSave = QPushButton('Save')
        self.btnMenu = QPushButton('Menu')

        self.vBox.addStretch()
        self.vBox.addWidget(self.editFullName)
        self.vBox.addWidget(self.editUserName)
        self.vBox.addWidget(self.editPassword)
        self.vBox.addWidget(self.editMobileNumber)
        self.vBox.addWidget(self.labelMsg)
        self.vBox.addWidget(self.btnSave)
        self.vBox.addStretch()
        self.vBox.addWidget(self.btnMenu)

        self.setLayout(self.vBox)

        self.btnSave.clicked.connect(self.insertUser)
        self.btnMenu.clicked.connect(self.showMenu)


    def showMenu(self):
        self.close()
        self.menu = Window()

    

    def null_line_edits(self, text):
        self.editFullName.setText('')
        self.editUserName.setText('')
        self.editPassword.setText('')
        self.editMobileNumber.setText('')
        self.labelMsg.setText(text)
        
    


    def insertUser(self):
        fname = self.editFullName.text()
        uname = self.editUserName.text()
        pwd = self.editPassword.text()
        mobnum = self.editMobileNumber.text()

        if fname and uname and pwd and mobnum:
            user = {
                'full name': fname,
                'username': uname,
                'password': pwd,
                'mobile number': mobnum
            }

            message = self.core.createUser(user)
            self.null_line_edits(message)
        


class ListUsersWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()
        self.setFixedSize(1000,400)
        self.setWindowTitle('List of users')
        self.__initUI()
        self.show()


    def __initUI(self):
        self.showAllUsers()

        self.vBox = QVBoxLayout()

        self.table = QTableWidget()
        self.btn_menu = QPushButton('Menu') 


        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)

        self.table.setHorizontalHeaderLabels(self.users[0].keys())
        self.table.setRowCount(len(self.users))

        row = 0
        for user in self.users:
            self.table.setItem(row, 0, QTableWidgetItem(user['id']))
            self.table.setItem(row, 1, QTableWidgetItem(user['full name']))
            self.table.setItem(row, 2, QTableWidgetItem(user['username']))
            self.table.setItem(row, 3, QTableWidgetItem(user['password']))
            self.table.setItem(row, 4, QTableWidgetItem(user['mobile number']))
            row += 1

        self.vBox.addWidget(self.table)
        self.vBox.addWidget(self.btn_menu)
        
        self.btn_menu.clicked.connect(self.showMenu)

        self.setLayout(self.vBox)
        

    def showMenu(self):
        self.close()
        self.menu = Window()
        


    def showAllUsers(self):
        self.users = self.__getData()

        print(self.users)

    def __getData(self):
        users = self.core.getAllUsers()
        users = list(map(lambda user: {
            'id': str(user[0]), 
            'full name': user[1], 
            'username': user[2], 
            'password': user[3], 
            'mobile number': user[4]}, 
            users))

        return users



class UpdateUserWindow(QWidget):
 
 
    def __init__(self):

        super().__init__()

        self.setFixedSize(600,400)
        self.setWindowTitle('Update user')
        self.__initUI()
        self.show()


    def __initUI(self):

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.msg_label = QLabel()
        self.editID = QLineEdit()
        self.editID.setPlaceholderText('ID')
        self.editFullName = QLineEdit()
        self.editFullName.setPlaceholderText('Full Name')
        self.editUserName = QLineEdit()
        self.editUserName.setPlaceholderText('Username')
        # self.editPassword = PasswordEdit()
        self.editPassword.setPlaceholderText('Password')
        self.editMobileNumber = QLineEdit()
        self.editMobileNumber.setPlaceholderText('Mobile Number')

        self.btnUpdate = QPushButton('Update')
        self.btnMenu = QPushButton('Menu')

        self.vBox.addStretch()
        self.vBox.addWidget(self.editID)
        self.vBox.addWidget(self.editFullName)
        self.vBox.addWidget(self.editUserName)
        self.vBox.addWidget(self.editPassword)
        self.vBox.addWidget(self.editMobileNumber)
        self.vBox.addWidget(self.btnUpdate)
        self.vBox.addWidget(self.msg_label)
        self.vBox.addStretch()
        self.vBox.addWidget(self.btnMenu)

        self.setLayout(self.vBox)

        self.btnUpdate.clicked.connect(self.updateUser)
        self.btnMenu.clicked.connect(self.showMenu)


    def showMenu(self):
        self.close()
        self.menu = Window()


    def null_line_edits(self, text):
        self.editFullName.setText('')
        self.editUserName.setText('')
        self.editPassword.setText('')
        self.editMobileNumber.setText('')
        self.msg_label.setText(text)



    def updateUser(self):
        cr = Core()
        
        Id = self.editID.text()
        FullName = self.editFullName.text()
        UserName = self.editUserName.text()
        Password = self.editPassword.text()
        mobileNumber = self.editMobileNumber.text()
        user = {
            'id': Id,
            'full name': FullName,
            'username': UserName,
            'password': Password,
            'mobile number': mobileNumber
        }
        
        msg = cr.update_user_info(user)
        self.null_line_edits(msg)



class DeleteUserWindow(QWidget):
 
 
    def __init__(self):

        super().__init__()

        self.setFixedSize(600,400)
        self.setWindowTitle('Delete user')
        self.__initUI()
        self.show()


    def __initUI(self):

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.editID = QLineEdit()
        self.editID.setPlaceholderText('ID')
        self.msg_label = QLabel()
        self.btnDelete = QPushButton('Delete')
        self.btnMenu = QPushButton('Menu')

        self.vBox.addStretch()
        self.vBox.addWidget(self.editID)
        self.vBox.addWidget(self.btnDelete)
        self.vBox.addWidget(self.msg_label)
        self.vBox.addStretch()
        self.vBox.addWidget(self.btnMenu)

        self.setLayout(self.vBox)

        self.btnDelete.clicked.connect(self.deleteUser)
        self.btnMenu.clicked.connect(self.showMenu)


    def showMenu(self):
        self.close()
        self.menu = Window()


    def deleteUser(self):
        Id = self.editID.text()
        cr = Core()
        msg = cr.delete_user(Id)
        self.msg_label.setText(msg)
        self.editID.setText('')
        


app = QApplication(sys.argv)

win = Window()

# cU = CreateUserWindow()
# lU = ListUsersWindow()
# lU.showAllUsers()
# UU = UpdateUserWindow()
# dU = DeleteUserWindow()

sys.exit(app.exec_())