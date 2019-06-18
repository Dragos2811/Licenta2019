# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Mon Jun 17 12:14:57 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore as Q
from PyQt5 import QtMultimedia as M
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 425)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 421))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.generareBtn = QtWidgets.QPushButton(self.tab)
        self.generareBtn.setObjectName("generareBtn")
        self.gridLayout.addWidget(self.generareBtn, 2, 1, 1, 1)
        self.playBtn = QtWidgets.QPushButton(self.tab)
        self.playBtn.setObjectName("playBtn")
        self.gridLayout.addWidget(self.playBtn, 2, 0, 1, 1)
        self.pauseBtn = QtWidgets.QPushButton(self.tab)
        self.pauseBtn.setObjectName("pauseBtn")
        self.gridLayout.addWidget(self.pauseBtn, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "App", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Alege unul dintre muzicieni", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "asdf", None, -1))
        self.generareBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Generare", None, -1))
        self.playBtn.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pauseBtn.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Generare piesa", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "apasa-l", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Creare model", None, -1))
        self.url = Q.QUrl.fromLocalFile(os.path.abspath('byron.mp3'))
        self.content = M.QMediaContent(self.url)
        self.player = M.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(qt_app)
    qt_app.show()
    app.exec_()
