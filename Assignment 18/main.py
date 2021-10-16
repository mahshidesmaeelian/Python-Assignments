import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('sodoko.ui')
        self.change_theme = 'light'

        self.game = [[None for i  in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                textbox_object = QLineEdit()
                textbox_object.setStyleSheet('font-size: 30px ; text-align:center')
                textbox_object.setSizePolicy(QSizePolicy.Preferred , QSizePolicy.Preferred)
                self.game[i][j] = textbox_object #back_end
                self.ui.gridLayout.addWidget(textbox_object, i , j) #front_end
                self.game[i][j].setAlignment(Qt.AlignHCenter)
                textbox_object.textChanged[str].connect(self.check_game)

        self.ui.show()
        self.ui.btn_newgame.clicked.connect(self.new_game)
        self.ui.btn_check.clicked.connect(self.check_game)
        self.ui.btn_theme.clicked.connect(self.theme)
        self.ui.btn_clear.clicked.connect(self.clear)

    def check_game(self):

        self.flag = '0'

        for row in range(9):
            for col in range(9):
                for i in range(9):
                    for j in range(9):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '' :
                            self.game[row][i].setStyleSheet('font-size: 32px ; background-color : pink')       
                            self.flag = '0'                 
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 32px ; background-color : pink') 
                            self.flag = '0'                   
                                             
        for row in range(3):
            for col in range(3):
                for i in range(3):
                    for j in range(3):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                            self.game[row][i].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
                        elif self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   

        for row in range(3,6):
            for col in range(3,6):
                for i in range(3,6):
                    for j in range(3,6):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                            self.game[row][i].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'    
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'    
                        elif self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
        
        for row in range(6,9):
            for col in range(6,9):
                for i in range(6,9):
                    for j in range(6,9):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                            self.game[row][i].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
                        elif self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'     

        for row in range(3,6):
            for col in range(3):
                for i in range(3,6):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')    
                            self.flag = '0'   

        for row in range(6,9):
            for col in range(3):
                for i in range(6,9):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink') 
                            self.flag = '0'   
        
        for row in range(3):
            for col in range(3,6):
                for i in range(3):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
        
        for row in range(6,9):
            for col in range(3,6):
                for i in range(6,9):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
        
        for row in range(3,6):
            for col in range(6,9):
                for i in range(3,6):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'   
        
        for row in range(3):
            for col in range(6,9):
                for i in range(3):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 32px ; background-color : pink')
                            self.flag = '0'  

        for i in range(9):
            for(j) in range(9):
                if self.game[i][j].text() != '':
                    self.flag == '1' 

        if self.flag == '1':
            you_win_messagebox = QMessageBox()
            you_win_messagebox.setText('You win\^0^/')
            you_win_messagebox.exec()



    def new_game(self):
        self.empty_cells = []
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')


        r = random.randint(1,6)
        file_path = f"data/s{r}.txt"

        open_file = open(file_path , 'r')

        long_text = open_file.read()
        rows = long_text.split('\n')

        for i in range(9):
            numbers = rows[i].split(' ')
            for j in range(9):
                if numbers[j] != '0':
                    self.game[i][j].setStyleSheet('font-size : 32px  ; color:green ; text-align:center')
                    self.game[i][j].setText(numbers[j])

                else:
                    self.game[i][j].setStyleSheet('font-size : 32px  ; color:black ; text-align:center')
                    self.game[i][j].setText('')
                    self.empty_cells.append(numbers[j])
                
                    


                
    def clear(self):
        pass


    def theme(self):
        if self.change_theme == 'light':
            self.ui.setStyleSheet('background-color : #3d3d3d')
            self.change_theme = 'dark'

        elif self.change_theme == 'dark':
            self.ui.setStyleSheet('background-color : white')
            self.change_theme = 'light'
        
                     


app = QApplication([])
window = MainWindow()
app.exec_()
 