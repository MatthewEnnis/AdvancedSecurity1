from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit
from functools import partial
#I'm using Qt for the gui, if you don't have this installed you can do "pip install pyqt5"

def buttonclicked(x):
	if x == "=": #evaluate if it's equals
		result.setText(str(eval(result.text())))
	elif x == "C": #clear if it's C
		result.setText("")
	else: #otherwise just add the number
		result.setText(result.text()+x)

app = QApplication([])
window = QWidget()

#Setting up the grid of numbers and symbols
grid = QGridLayout()
numbers = ["7","8","9","/","4","5","6","*","1","2","3","-","C","0","=","+"]
for i in range(4):
	for j in range(4):
		number = numbers[i*4+j]
		button = QPushButton(number)
		button.clicked.connect(partial(buttonclicked, number))
		grid.addWidget(button,i,j)

#Sorting out the layout
layout = QVBoxLayout()
result = QLineEdit()
result.setReadOnly(True)
layout.addWidget(result)
layout.addLayout(grid)
window.setLayout(layout)
window.setWindowTitle("Calculator")
window.show()
app.exec()