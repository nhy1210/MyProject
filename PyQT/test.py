from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from PyQt5.QtCore import pyqtSlot

import sys
# Subclass QMainWindow to customise your application's main window
class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&University")
        styleLabel.setBuddy(styleComboBox)

        lineEditGPA = QLineEdit('GPA')
        styleLabel2 = QLabel("&GPA")
        styleLabel2.setBuddy(lineEditGPA)

        self.useStylePaletteCheckBox = QCheckBox("&Top University")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Others")

        #self.createTopLeftGroupBox()
        #self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        #self.createProgressBar()

        styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        #disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        #mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        #mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomRightGroupBox, 1, 0)
        mainLayout.addWidget(self.bottomLeftTabWidget, 1, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Sydney University - Schoolarship point system")
        self.changeStyle('G8')
        #self.gettest()

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 2)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Here is some expanation about your points\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Points convert table")
        self.bottomLeftTabWidget.addTab(tab2, "Explanation")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('4.0')
        lineEdit.setEchoMode(QLineEdit.Password)
        styleLabelLine = QLabel("&GPA")
        styleLabelLine.setBuddy(lineEdit)

        lineEdit1 = QLineEdit('2')
        styleLabelLine1 = QLabel("&SCI paper")
        styleLabelLine1.setBuddy(lineEdit1)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(10)
        styleLabelLine2 = QLabel("&Years")
        styleLabelLine2.setBuddy(spinBox)

        # connect button to function on_click
        #self.lineEdit.clicked.connect(self.on_click)
        #self.show()



        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        styleLabelLine3 = QLabel("&Semester")
        styleLabelLine3.setBuddy(dateTimeEdit)

        #slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        #slider.setValue(40)

        #scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        #scrollBar.setValue(60)

        #dial = QDial(self.bottomRightGroupBox)
        #dial.setValue(30)
        #dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(styleLabelLine, 0, 0, 1, 2)
        layout.addWidget(lineEdit, 0, 1, 1, 2)

        layout.addWidget(styleLabelLine1, 1, 0, 1, 2)
        layout.addWidget(lineEdit1, 1, 1, 1, 2)

        layout.addWidget(styleLabelLine2, 2, 0, 1, 2)
        layout.addWidget(spinBox, 2, 1, 1, 2)

        layout.addWidget(styleLabelLine3,3, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 3, 1, 1, 2)
        #layout.addWidget(slider, 3, 0)
        #layout.addWidget(scrollBar, 4, 0)
        #layout.addWidget(dial, 3, 1, 2, 1)
        #layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)
        
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.lineEdit.text()
        print(textboxValue)

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)
    def gettest(self):
        mytext = self.textEdit.toPlainText()
        print(mytext)


app = QApplication(sys.argv)

window = WidgetGallery()
window.show()

app.exec_()

