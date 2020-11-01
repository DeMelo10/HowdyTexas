from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
from main import Ui_MainWindow
from dijkstra import *
import sys


'''
	Class
'''

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)

'''
	Functions
'''

def search():
	_translate = QtCore.QCoreApplication.translate
	numbers = []
	graph = {}
	predecessor_isdigit = False
	count = -1

	data = open("data/test.txt", "r")

	in_search = main.ld_search.text()

	for line in data:
		graph.setdefault(int(line.split()[0]), {}).update({int(line.split()[1]) : abs(int(line.split()[1]) - int(line.split()[0]))})
	data.close()

	if in_search != "":
		for ch in in_search:
			if ch.isdigit() and predecessor_isdigit == False:
				numbers.append(ch)
				predecessor_isdigit = True
				count += 1
			elif ch.isdigit() and predecessor_isdigit == True:
				numbers[count] = numbers[count] + ch
			else:
				predecessor_isdigit = False

		for i in range(len(numbers)):
			numbers[i] = int(numbers[i])

		if len(numbers) == 2:
			distance, path = dijkstra(graph, numbers[0], numbers[1])

			if distance != -1 and path != -1:
				main.lb_result.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search result</span></p><p align=\"center\">The <span style=\" font-weight:600;\">shortest distance</span> between <span style=\" font-weight:600;\">{numbers[0]}</span> and <span style=\" font-weight:600;\">{numbers[1]} intersection</span> is: <span style=\" font-weight:600;\">{distance} meters</span>.</p><p align=\"center\">The <span style=\" font-weight:600;\">shortest path</span> between <span style=\" font-weight:600;\">{numbers[0]}</span> and <span style=\" font-weight:600;\">{numbers[1]} intersection</span> is:</p><p align=\"center\"><span style=\" font-weight:600;\">{path}</span></p></body></html>"))
				main.fr_result.show()
			else:
				main.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search result</span></p><p align=\"center\">Sorry, path <span style=\" font-weight:600;\">not reachable</span>. :'(</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
				main.fr_result.show()
		else:
			main.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search result</span></p><p align=\"center\">Please, <span style=\" font-weight:600;\">enter</span> the <span style=\" font-weight:600;\">numbers of the crossroads</span> you want to search for!</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))			
			main.fr_result.show()

	else:
		main.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search result</span></p><p align=\"center\">Please, <span style=\" font-weight:600;\">enter</span> your search!</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
		main.fr_result.show()

	main.btn_close.clicked.connect(lambda: main.fr_result.hide())

'''
	App
'''

if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)    
    main = MainWindow()
    main.fr_result.hide()
    main.btn_search.clicked.connect(lambda: search())
    main.show()
    sys.exit(app.exec_())