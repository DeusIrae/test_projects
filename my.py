#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QMessageBox, QMainWindow, QAction, qApp, QTextEdit, QLabel
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
 
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
		# Top menu 
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar().showMessage('You choose menu!')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
		# Quit button 1               
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('Press <b>Quit</b> button')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(10, 30)       
        
        # Test quit button (change to Print)
        abtn = QPushButton('Print', self)
        abtn.clicked.connect(QCoreApplication.instance().quit)
        abtn.setToolTip('Press <b>Print</b> button to print msg')
        abtn.resize(qbtn.sizeHint())
        abtn.move(10, 60)
        
        #Set statusbar and Title
        self.statusBar().showMessage('Ready')
        self.setGeometry(200, 200, 350, 250)
        self.setWindowTitle('Quit button')  
        
        #Set central widget
        #textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)

        # Test some labels
        lbl1 = QLabel('My new label', self)
        lbl1.move(75, 85)
        
        #Initiate of window
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.statusBar().showMessage('Slabak nerishitelniy!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
