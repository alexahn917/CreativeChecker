# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 497)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn_checker_zip = QtWidgets.QPushButton(self.centralWidget)
        self.btn_checker_zip.setGeometry(QtCore.QRect(220, 20, 201, 51))
        self.btn_checker_zip.setObjectName("btn_checker_zip")
        self.btn_checker_img = QtWidgets.QPushButton(self.centralWidget)
        self.btn_checker_img.setGeometry(QtCore.QRect(220, 70, 201, 51))
        self.btn_checker_img.setObjectName("btn_checker_img")
        self.result_txt_box = QtWidgets.QTextBrowser(self.centralWidget)
        self.result_txt_box.setGeometry(QtCore.QRect(40, 180, 551, 241))
        self.result_txt_box.setObjectName("result_txt_box")
        self.btn_checker_resize = QtWidgets.QPushButton(self.centralWidget)
        self.btn_checker_resize.setGeometry(QtCore.QRect(220, 120, 201, 51))
        self.btn_checker_resize.setObjectName("btn_checker_resize")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 637, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMoloco_Creative_Checker = QtWidgets.QMenu(self.menuBar)
        self.menuMoloco_Creative_Checker.setObjectName("menuMoloco_Creative_Checker")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuMoloco_Creative_Checker.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_checker_zip.setText(_translate("MainWindow", "Check Creative ZIP File"))
        self.btn_checker_img.setText(_translate("MainWindow", "Check Creative Image Files"))
        self.btn_checker_resize.setText(_translate("MainWindow", "Creative Auto Resize"))
        self.menuMoloco_Creative_Checker.setTitle(_translate("MainWindow", "Moloco Creative Checker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

