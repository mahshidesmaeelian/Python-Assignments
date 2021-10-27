from functools import partial
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('MainWindow.ui')
        self.ui.show()

        self.result = database.get_all()

        self.ReadFromDataBase()

        self.ui.btn_add.clicked.connect(self.AddNewTaskToDataBase)

        for i in range(len(self.remove_btn)):   
            self.remove_btn[i].clicked.connect(partial(self.RemoveTask,self.remove_btn[i],self.lable1[i],self.checkbox[i],self.title_list[i]))

        for i in range(len(self.checkbox)): 
            self.checkbox[i].stateChanged.connect(partial(self.check_if_is_done,self.title_list[i]))



    def AddNewTaskToDataBase(self):

        title1 = self.ui.textbox_title.text()
        description = self.ui.textbox_description.text()
        
        database.add(title1,description)

        self.ui.textbox_title.setText('')
        self.ui.textbox_description.setText('')

        self.ReadFromDataBase()


    def RemoveTask(self,i,j,k,l):
        
        self.ui.gridLayout.removeWidget(i)
        self.ui.gridLayout.removeWidget(j)
        self.ui.gridLayout.removeWidget(k)

        i.deleteLater()
        j.deleteLater()
        k.deleteLater()

        
        database.remove_function(l)
        self.ReadFromDataBase()


    def ReadFromDataBase(self):
        self.remove_btn = []
        self.checkbox = []
        self.lable1 = []
        self.title_list = []
    
        for i in range(len(self.result)):

            self.new_checkbox = QCheckBox()
            
            if self.result[i][3] == 1:
                self.new_checkbox.setChecked(True)
            self.checkbox.append(self.new_checkbox)
            
            
            self.new_lable = QLabel()
            self.new_lable.setText(self.result[i][1])
            self.lable1.append(self.new_lable)
            self.title_list.append(self.result[i][1])

            

            self.new_delete_btn = QPushButton()
            self.new_delete_btn.setText('❌')
            self.remove_btn.append(self.new_delete_btn)

        
            self.ui.gridLayout.addWidget(self.new_lable , i , 0)
            self.ui.gridLayout.addWidget(self.new_checkbox , i , 1)
            self.ui.gridLayout.addWidget(self.new_delete_btn, i , 2)


    def check_if_is_done(self,a,b):

        for i in range(len(self.checkbox)):
            if self.checkbox[i].isChecked():
                print('yes')
                database.update_done(a)
                self.ReadFromDataBase()

            else:
                print('no')
                database.update_not_done(b)
                self.ReadFromDataBase()

            
app = QApplication([])
window = MainWindow()
app.exec()

