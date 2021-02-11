from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from generator import RSAgenerator
from PyQt5 import QtTest

import sys, os, numpy, re, random 

class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno, self).__init__(*args,*kwargs)
        self.setWindowTitle("RSA")
        
        titleText = QLabel()
        titleText.setText("RSA")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Comic Sans',50))
        titleText.setStyleSheet("QLabel {color : #cae8d5}")

        titleText2 = QLabel()
        titleText2.setText("ENCRYPTOR")
        titleText2.setAlignment(Qt.AlignCenter)
        titleText2.setFont(QFont('Comic Sans',50))
        titleText2.setStyleSheet("QLabel {color : #cae8d5}")

        self.subtitleText = QLabel()
        self.subtitleText.setText(" ")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Comic Sans',20))
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")

        self.filePath = QLineEdit()
        self.filePath.setReadOnly(True)
        self.filePath.setPlaceholderText("File path")
        self.filePath.setAlignment(Qt.AlignCenter)
        self.filePath.setFont(QFont('Comic Sans',10))
        self.filePath.setStyleSheet("QLineEdit {color : #84a9ac}")

        self.keyPath = QLineEdit()
        self.keyPath.setReadOnly(True)
        self.keyPath.setPlaceholderText("Key path")
        self.keyPath.setAlignment(Qt.AlignCenter)
        self.keyPath.setFont(QFont('Comic Sans',10))
        self.keyPath.setStyleSheet("QLineEdit {color : #84a9ac}")

        self.infoButton = QPushButton()
        self.infoButton.setText("Info")
        self.infoButton.setFont(QFont('Comic Sans',12))
        self.infoButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.infoButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.infoButton.clicked.connect(self.infoClicked)

        generateButton = QPushButton()
        generateButton.setText("Generate")
        generateButton.setFont(QFont('Comic Sans',12))
        generateButton.setStyleSheet("QPushButton {background : #3b6978}")
        generateButton.setStyleSheet("QPushButton {color : #cae8d5}")
        generateButton.clicked.connect(self.generateClicked)

        self.checkTextButton = QPushButton()
        self.checkTextButton.setText("Check text")
        self.checkTextButton.setFont(QFont('Comic Sans',12))
        self.checkTextButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.checkTextButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.checkTextButton.clicked.connect(self.checkTextClicked)

        self.checkResultButton = QPushButton()
        self.checkResultButton.setText("Check result")
        self.checkResultButton.setFont(QFont('Comic Sans',12))
        self.checkResultButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.checkResultButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.checkResultButton.clicked.connect(self.checkResultClicked)

        self.textFromFileButton = QFileDialog()
        self.textFromFileButton.setNameFilter("Text files (*.txt)")
        self.textFromFileButton.hide()

        fileButton = QPushButton()
        fileButton.setText("Get File")
        fileButton.setFont(QFont('Comic Sans',12))
        fileButton.setStyleSheet("QPushButton {background : #3b6978}")
        fileButton.setStyleSheet("QPushButton {color : #cae8d5}")
        fileButton.clicked.connect(self.fileButtonClicked)

        keyButton = QPushButton()
        keyButton.setText("Get Key")
        keyButton.setFont(QFont('Comic Sans',12))
        keyButton.setStyleSheet("QPushButton {background : #3b6978}")
        keyButton.setStyleSheet("QPushButton {color : #cae8d5}")
        keyButton.clicked.connect(self.keyButtonClicked)

        encryptButton = QPushButton()
        encryptButton.setText("Encrypt")
        encryptButton.setFont(QFont('Comic Sans',12))
        encryptButton.setStyleSheet("QPushButton {background : #3b6978}")
        encryptButton.setStyleSheet("QPushButton {color : #cae8d5}")
        encryptButton.clicked.connect(self.encryptClicked)

        decryptButton = QPushButton()
        decryptButton.setText("Decrypt")
        decryptButton.setFont(QFont('Comic Sans',12))
        decryptButton.setStyleSheet("QPushButton {background : #3b6978}")
        decryptButton.setStyleSheet("QPushButton {color : #cae8d5}")
        decryptButton.clicked.connect(self.decryptClicked)

        fileLayout = QHBoxLayout()
        fileLayout.addWidget(fileButton)
        fileLayout.addWidget(keyButton)
        fileLayoutW = QWidget()
        fileLayoutW.setLayout(fileLayout)

        encryptPathLayout = QHBoxLayout()
        encryptPathLayout.addWidget(self.filePath)
        encryptPathLayout.addWidget(self.keyPath)
        encryptPathLayoutW = QWidget()
        encryptPathLayoutW.setLayout(encryptPathLayout)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(encryptButton)
        buttonsLayout.addWidget(generateButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)

        checkLayout = QHBoxLayout()
        checkLayout.addWidget(self.checkTextButton)
        checkLayout.addWidget(self.checkResultButton)
        checkLayoutW = QWidget()
        checkLayoutW.setLayout(checkLayout)

        infoButtonsLayout = QHBoxLayout()
        infoButtonsLayout.addWidget(self.infoButton)
        infoButtonsLayout.addWidget(decryptButton)
        infobuttonsLayoutW = QWidget()
        infobuttonsLayoutW.setLayout(infoButtonsLayout)

        #Main Layout
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(titleText2)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(encryptPathLayoutW)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(infobuttonsLayoutW)
        mainMenu.addWidget(fileLayoutW)

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)

    def fileButtonClicked(self):
        self.textFromFileButton.show()
        if self.textFromFileButton.exec():
            files = self.textFromFileButton.selectedFiles()
            self.filePath.setText(files[0])
    
    def keyButtonClicked(self):
        self.textFromFileButton.show()
        if self.textFromFileButton.exec():
            files = self.textFromFileButton.selectedFiles()
            self.keyPath.setText(files[0])

    def encryptClicked(self):
        self.subtitleText.setText("ENCRYPT MODE")
        QtTest.QTest.qWait(10)
        self.encrypt()
        self.subtitleText.setStyleSheet("color: green")
        self.subtitleText.setText("DONE")
        QtTest.QTest.qWait(3000)
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")
        self.subtitleText.setText("")

    def decryptClicked(self):
        self.subtitleText.setText("DECRYPT MODE")
        QtTest.QTest.qWait(10)
        self.decrypt()
        self.subtitleText.setStyleSheet("color: green")
        self.subtitleText.setText("DONE")
        QtTest.QTest.qWait(3000)
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")
        self.subtitleText.setText("")

    def generateClicked(self):
        self.subtitleText.setText("GENERATE MODE")
        QtTest.QTest.qWait(10)
        self.genKey()
        self.subtitleText.setStyleSheet("color: green")
        self.subtitleText.setText("DONE")
        QtTest.QTest.qWait(3000)
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")
        self.subtitleText.setText("")

    def checkTextClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Text")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("text.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()

    def checkResultClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Result")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("output.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()
    
    def saveClicked(self):
        f = open("result.txt", "w",encoding="utf-8")
        f.write("Encrypted text: "+self.encryptedText.text())
        f.write("\nDecrypted text: "+self.decryptedText.text())
        f.write("\nKey: "+self.genKey())
        f.close()

    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("info.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()
    
    def encrypt(self):
        with open(self.filePath.text(),"r") as fileinput: 
            data = fileinput.read()
        with open(self.keyPath.text(),"r") as fileinput: 
            publicKey = fileinput.read()
        publicKey = re.sub(r'[^0-9 ]+', '', publicKey).split()
        
        asciiText = [ord(letter) for letter in data]
        encrypted = [RSAgenerator.formula(letter, int(publicKey[0]), int(publicKey[1])) for letter in asciiText]

        filename = QFileDialog.getSaveFileName(self, "Open Text File", os.path.abspath(os.getcwd()), "Text Files (*.txt)")
        with open(filename[0],"w") as outputfile:
            for x in encrypted:
                outputfile.write(str(x) + " ")

    def decrypt(self):
        with open(self.filePath.text(),"r") as file:
            text = file.read()
        text = text.split()
        for i in range(len(text)):
            text[i] = int(text[i])

        with open(self.keyPath.text(),"r") as fileinput: 
            privateKey = fileinput.read()
        privateKey = re.sub(r'[^0-9 ]+', '', privateKey).split()
            
        text = [RSAgenerator.formula(c, int(privateKey[0]), int(privateKey[1])) for c in text]
        text2 = ""
        for letter in text:
            if letter in range(0x110000):
                text2 += chr(letter)
            else:
                self.subtitleText.setStyleSheet('color: red')
                self.subtitleText.setText("Invalid key")
                QtTest.QTest.qWait(3000)

        filename = QFileDialog.getSaveFileName(self, "Open Text File", os.path.abspath(os.getcwd()), "Text Files (*.txt)")
        with open(filename[0],"w") as outputfile:
            for x in text2:
                outputfile.write(str(x))
    
    def genKey(self):
        self.r = RSAgenerator()
        filename = QFileDialog.getSaveFileName(self, "Open Text File", os.path.abspath(os.getcwd()), "Text Files (*.txt)")
        if filename[0] != '':
            path = filename[0]
            i = len(path)-1
            while True:
                path = path[:-1]
                i-=1
                if path[i] == '.':
                    path = path[:-1]
                    break
            dir1 = path + '_private.txt'
            dir2 = path + '_public.txt'
            with open(dir1,"w") as outputfile: 
                outputfile.write(str(self.r.privateKey()))
            with open(dir2,"w") as outputfile: 
                outputfile.write(str(self.r.publicKey()))

                     
#MAIN
app = QApplication(sys.argv)
window = Okno()
window.setFixedSize(650,400)
window.setStyleSheet("background-color: #204051")
window.show()

app.exec_()