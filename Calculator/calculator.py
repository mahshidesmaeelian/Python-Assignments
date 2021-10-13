import math
import sympy 
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('cal.ui' , None)
        self.ui.show()

        self.ui.btn1.clicked.connect(partial(self.func_num , '1'))
        self.ui.btn2.clicked.connect(partial(self.func_num , '2'))
        self.ui.btn3.clicked.connect(partial(self.func_num , '3'))
        self.ui.btn4.clicked.connect(partial(self.func_num , '4'))
        self.ui.btn5.clicked.connect(partial(self.func_num , '5'))
        self.ui.btn6.clicked.connect(partial(self.func_num , '6'))
        self.ui.btn7.clicked.connect(partial(self.func_num , '7'))
        self.ui.btn8.clicked.connect(partial(self.func_num , '8'))
        self.ui.btn9.clicked.connect(partial(self.func_num , '9'))
        self.ui.btn0.clicked.connect(partial(self.func_num , '0'))
 

        self.ui.btnsum.clicked.connect(self.sum)
        self.ui.btnsub.clicked.connect(self.sub)
        self.ui.btnmul.clicked.connect(self.mul)
        self.ui.btndiv.clicked.connect(self.div)
        self.ui.btn_equal.clicked.connect(self.equal)


        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_point.clicked.connect(self.point)
        self.ui.btn_pos_neg.clicked.connect(self.sign)

    def func_num(self, x):
        self.ui.textbox.setText(self.ui.textbox.text() + x )

        
    def sum(self):
        self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.operator = '+'

    def sub(self):
        self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.operator = '-'


    def mul(self):
        self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.operator = '*'

    def div(self):
        self.num1 = int(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.operator = '/'

    def equal(self):

        if self.operator == '+':
            self.num2 = int(self.ui.textbox.text())
            res = self.num1 + self.num2
            self.ui.textbox.setText(str(res))


        elif self.operator == '-':
            self.num2 = int(self.ui.textbox.text())
            res = self.num1 - self.num2
            self.ui.textbox.setText(str(res))


        elif self.operator == '*':
            self.num2 = int(self.ui.textbox.text())
            res = self.num1 * self.num2
            self.ui.textbox.setText(str(res))


        elif self.operator == '/':
            self.num2 = int(self.ui.textbox.text())
            if self.num2 == 0 :
                self.ui.textbox.setText('Error ! number can not be divided by 0')
            else:
                res = self.num1 / self.num2
                self.ui.textbox.setText(str(res))


    def sin(self):
        self.num1 = float(self.ui.textbox.text())
        res = math.sin(math.radians(self.num1))
        self.ui.textbox.setText(str(res))

    def cos(self):
        self.num1 = float(self.ui.textbox.text())
        res = math.cos(math.radians(self.num1))
        self.ui.textbox.setText(str(res))

    def tan(self):
        self.num1 = float(self.ui.textbox.text())
        res = math.tan(math.radians(self.num1))
        self.ui.textbox.setText(str(res))

    def cot(self):
        self.num1 = float(self.ui.textbox.text())
        res = sympy.cot(math.radians(self.num1))
        self.ui.textbox.setText(str(res))

    def log(self):
        self.num1 = float(self.ui.textbox.text())
        res = math.log(math.radians(self.num1))
        self.ui.textbox.setText(str(res))

    def sqrt(self):
        self.num1 = float(self.ui.textbox.text())
        res = math.sqrt(math.radians(self.num1))
        self.ui.textbox.setText(str(res))

    def clear(self):
        self.ui.textbox.setText('')

    def point(self):
        for i in self.ui.textbox.text():

            if '.' not in self.ui.textbox.text():

                self.ui.textbox.setText(self.ui.textbox.text()+'.')
       

    def sign(self):
        self.num1 = int(self.ui.textbox.text())
        sign = self.num1 * -1
        self.ui.textbox.setText(str(sign))
        


app = QApplication([])
window = Calculator()
#window_setting = Calculator()

app.exec()


 
 