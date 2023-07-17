import sys
import numpy as np

from PySide2 import QtWidgets
from PySide2.QtGui import QFont, QBrush, QPixmap

from matplotlib.backends.backend_qt5agg import (FigureCanvas)
from matplotlib.figure import Figure

class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setWindowTitle("Plot")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()
        self.setCentralWidget(self._main)
        self.layout = QtWidgets.QGridLayout(self._main)

        self.setAutoFillBackground(True)
        p = self.palette()
        brush = QBrush(QPixmap("imgs/background.jpg"))
        p.setBrush(self.backgroundRole(), brush)
        self.setPalette(p)

        # ---- Labels and Textfields ---- 
        #       Equation label 
        self.label1 = QtWidgets.QLabel(self._main)
        self.label1.setText("Please enter your equation")
        self.label1.setFont(QFont('Arial', 16)) 

        #       Equation textfield
        self.textfield1 = QtWidgets.QLineEdit(self._main)        
        self.textfield1.setFont(QFont('Arial', 16)) 
        self.textfield1.setStyleSheet("color: rgb(128,128,128)")
        self.textfield1.setToolTip("Equation must be variable of x and the supported operators are: + - / * ^")
        
        #       Min-value label
        self.label2 = QtWidgets.QLabel(self._main)
        self.label2.setText("Please enter the min value")
        self.label2.setFont(QFont('Arial', 16)) 

        #       Min-value textfield
        self.textfield2 = QtWidgets.QLineEdit(self._main)        
        self.textfield2.setFont(QFont('Arial', 16)) 
        self.textfield2.setStyleSheet("color: rgb(128,128,128)")

        #       Max-value label
        self.label3 = QtWidgets.QLabel(self._main)
        self.label3.setText("Please enter the max value")
        self.label3.setFont(QFont('Arial', 16)) 

        #       Max-value textfield
        self.textfield3 = QtWidgets.QLineEdit(self._main)        
        self.textfield3.setFont(QFont('Arial', 16)) 
        self.textfield3.setStyleSheet("color: rgb(128,128,128)")

        # ---- Button ----
        self.button = QtWidgets.QPushButton('Run', self._main)
        self.button.setFont(QFont('Arial', 16))
        self.button.setStyleSheet("QPushButton:pressed { background-color: rgb(46,139,87); }")
        self.button.setToolTip('Press to plot the function')
        self.button.clicked.connect(self.plotting)

        # ---- Message box for errors ----  
        self.mbox = QtWidgets.QMessageBox()

        # Figures ui
        self.figure = Figure(figsize=(10, 5))
        self.canvas = FigureCanvas(self.figure)
        self.main_layout.addWidget(self.canvas)

        # Widgets ui
        self.layout.addWidget( self.label1, 0, 0)
        self.layout.addWidget( self.textfield1, 0, 2)
        self.layout.addWidget( self.label2, 1,0)
        self.layout.addWidget( self.textfield2, 1,2)
        self.layout.addWidget( self.label3, 2,0)
        self.layout.addWidget( self.textfield3, 2,2)
        self.layout.addWidget( self.button, 3,5,1,2)
        self.layout.addWidget( self.canvas, 4,0,1,0)

    # Setting up the window ui
    def setup_ui(self):
        self.setup_main_window()
        self.setup_menu_bar()

    def setup_main_window(self):
        self.main_widget = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

    def setup_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.view_menu = self.menu_bar.addMenu("View")
        self.help_menu = self.menu_bar.addMenu("Help")

    # Error messaage window
    def error_mess(self, mess):
        self.mbox = QtWidgets.QMessageBox()
        self.mbox.setText(mess)
        self.mbox.setStyleSheet("color: rgb(220,20,60)")
        self.mbox.setWindowTitle("Error")
        self.mbox.setStandardButtons(QtWidgets.QMessageBox.Close)
        self.mbox.exec_()

    # --- Checks ---
    #    Equation checks
    def equation_check(self):
        eq = self.textfield1.text()
        if eq == "" or eq == " ":
            self.error_mess("Please enter the equation")
            self.textfield1.setFocus()
            return False
        
        if eq.endswith('+') or eq.endswith('-') or eq.endswith('*') \
            or eq.endswith('/') or eq.endswith('^'):
                self.error_mess("Equation could not with an operator")
                self.textfield1.setFocus()
                return False

        for i in eq:
            if  (i == ' ') or (i == 'x') or (i == 'X')  or (i == '+') \
                or (i == '-') or (i == '*') or (i == '/') or (i == '^') \
                or (i.isdigit()):
                continue
            else:
                self.error_mess("Please enter a valid equation variable in x and valid operator from: + - * / ^")
                self.textfield1.setFocus()
                return False

        return True    

    #    Minimum checks 
    def minimum_check(self):
        minval = self.textfield2.text()
        if minval == "":
            self.error_mess("Please enter minimum value")
            self.textfield2.setFocus()
            return False
        
        # Use of try-catch as if entered value is string program craches
        try:
            float(minval)
        except:
            self.error_mess("Minimum value must be a number")
            self.textfield2.setFocus()
            return False  

        return True  

    #    Maximum checks   
    def maximum_check(self):
        maxval = self.textfield3.text()
        if maxval == "":
            self.error_mess("Please enter maximum value")
            self.textfield3.setFocus()
            return False
        
        # Use of try-catch as if entered value is string program craches
        try:
            float(maxval)
        except:
            self.error_mess("Maximum value must be a number")
            self.textfield3.setFocus()
            return False  

        return True  

    def plotting(self):
        if self.equation_check() and self.minimum_check() and self.maximum_check():
            # check that min value not exceed the max value
            if float(self.textfield2.text()) > float(self.textfield3.text()):
                self.error_mess("Minimum value must be smaller than maximum value")
                return
            # replace ^ with ** for power 
            eq = self.textfield1.text()
            eq = eq.replace('^', '**')

            minval = float(self.textfield2.text())
            maxval = float(self.textfield3.text())
            step = np.arange(minval, maxval, 0.1)

            # Figures ui
            self.figure = Figure(figsize=(10, 5))
            self.canvas = FigureCanvas(self.figure)
            self.layout.addWidget(self.canvas, 4,0,1,0)
            self.axes = self.figure.add_subplot()
            self.axes.set_title("Plotter")
            self.axes.set_xlabel(r'$x$')
            self.axes.set_ylabel(r'$f(x)$')
            # self.axes.grid()
            try: 
                self.axes.plot(step, eval(eq, {'x': step}))
            except:
                self.axes.plot(step, eval(eq, {'X': step}))
            self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())

