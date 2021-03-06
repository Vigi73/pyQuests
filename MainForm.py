# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/Fish_Movie_35099.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(191, 191, 143);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(250, 140, 281, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(280, 250, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.table2 = QtWidgets.QTableWidget(self.tab)
        self.table2.setGeometry(QtCore.QRect(20, 270, 745, 261))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(9)
        self.table2.setFont(font)
        self.table2.setMouseTracking(True)
        self.table2.setTabletTracking(True)
        self.table2.setAutoFillBackground(True)
        self.table2.setStyleSheet("alternate-background-color: rgb(170, 170, 127);")
        self.table2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table2.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table2.setAlternatingRowColors(True)
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(7)
        self.table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/88_85289.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/42466camping_99131.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/img/location_map_pin_mark_icon_148684.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.table2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/img/arrow-down-a_icon-icons.com_50480.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.table2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/img/arrow-up-a_icon-icons.com_50460.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.table2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/img/2998113-animal-garden-gardening-insect-invertebrate-rain-worm-worm_99853.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.table2.setHorizontalHeaderItem(6, item)
        self.btnTask = QtWidgets.QPushButton(self.tab)
        self.btnTask.setGeometry(QtCore.QRect(644, 50, 121, 23))
        self.btnTask.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btnTask.setObjectName("btnTask")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox.setGeometry(QtCore.QRect(603, 100, 161, 20))
        self.doubleSpinBox.setStyleSheet("border: 1px solid rgb(117, 117, 117);\n"
"border-radius: 5px;\n"
"background-color: rgb(159, 161, 119);")
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setSpecialValueText("")
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 271, 20))
        self.comboBox.setStyleSheet("border: 1px solid rgb(117, 117, 117);\n"
"border-radius: 5px;\n"
"background-color: rgb(159, 161, 119);")
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 745, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(36, 72, 0);\n"
"color: rgb(221, 221, 221);\n"
"text-align: center\n"
"")
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit.setMarkdown("")
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 100, 271, 20))
        self.comboBox_2.setStyleSheet("border: 1px solid rgb(117, 117, 117);\n"
"border-radius: 5px;\n"
"background-color: rgb(159, 161, 119);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.btnSearch = QtWidgets.QPushButton(self.tab)
        self.btnSearch.setEnabled(True)
        self.btnSearch.setGeometry(QtCore.QRect(21, 220, 745, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnSearch.setFont(font)
        self.btnSearch.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btnSearch.setObjectName("btnSearch")
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(21, 160, 745, 61))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon1)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon3)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon6)
        self.table.setHorizontalHeaderItem(2, item)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(24, 80, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(315, 80, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(607, 80, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lcd1 = QtWidgets.QLCDNumber(self.tab)
        self.lcd1.setGeometry(QtCore.QRect(674, 530, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd1.setFont(font)
        self.lcd1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd1.setDigitCount(10)
        self.lcd1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd1.setProperty("value", 0.0)
        self.lcd1.setProperty("intValue", 0)
        self.lcd1.setObjectName("lcd1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 161, 511))
        self.listWidget.setStyleSheet("background-color: rgb(36, 72, 0);\n"
"color: rgb(221, 221, 221);\n"
"selection-color: rgb(255, 255, 127);\n"
"gridline-color: rgb(255, 255, 127);\n"
"selection-background-color: rgb(255, 255, 127);")
        self.listWidget.setObjectName("listWidget")
        self.tableBait = QtWidgets.QTableWidget(self.tab_2)
        self.tableBait.setGeometry(QtCore.QRect(180, 10, 591, 511))
        self.tableBait.setStyleSheet("alternate-background-color: rgb(170, 170, 127);")
        self.tableBait.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableBait.setAlternatingRowColors(True)
        self.tableBait.setObjectName("tableBait")
        self.tableBait.setColumnCount(6)
        self.tableBait.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableBait.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon1)
        self.tableBait.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon4)
        self.tableBait.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon5)
        self.tableBait.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableBait.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon3)
        self.tableBait.setHorizontalHeaderItem(5, item)
        self.pushBait = QtWidgets.QPushButton(self.tab_2)
        self.pushBait.setGeometry(QtCore.QRect(10, 530, 161, 23))
        self.pushBait.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pushBait.setObjectName("pushBait")
        self.lcd2 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcd2.setGeometry(QtCore.QRect(680, 521, 91, 21))
        self.lcd2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd2.setDigitCount(10)
        self.lcd2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd2.setObjectName("lcd2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushSafari = QtWidgets.QPushButton(self.tab_3)
        self.pushSafari.setGeometry(QtCore.QRect(10, 530, 751, 23))
        self.pushSafari.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pushSafari.setObjectName("pushSafari")
        self.tableSafari = QtWidgets.QTableWidget(self.tab_3)
        self.tableSafari.setGeometry(QtCore.QRect(7, 10, 762, 401))
        self.tableSafari.setMinimumSize(QtCore.QSize(762, 0))
        self.tableSafari.setMouseTracking(False)
        self.tableSafari.setTabletTracking(False)
        self.tableSafari.setAutoFillBackground(False)
        self.tableSafari.setStyleSheet("alternate-background-color: rgb(170, 170, 127);")
        self.tableSafari.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableSafari.setAlternatingRowColors(True)
        self.tableSafari.setShowGrid(True)
        self.tableSafari.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableSafari.setObjectName("tableSafari")
        self.tableSafari.setColumnCount(7)
        self.tableSafari.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon1)
        self.tableSafari.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon4)
        self.tableSafari.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon5)
        self.tableSafari.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableSafari.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon3)
        self.tableSafari.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon6)
        self.tableSafari.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/img/3687831-adventure-journey-location-map_108802.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.tableSafari.setHorizontalHeaderItem(6, item)
        self.lcd3 = QtWidgets.QLCDNumber(self.tab_3)
        self.lcd3.setGeometry(QtCore.QRect(668, 410, 101, 23))
        self.lcd3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd3.setDigitCount(10)
        self.lcd3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd3.setObjectName("lcd3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(0, -5, 791, 571))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableMutants = QtWidgets.QTableWidget(self.groupBox)
        self.tableMutants.setGeometry(QtCore.QRect(9, 110, 761, 381))
        self.tableMutants.setStyleSheet("alternate-background-color: rgb(170, 170, 127);")
        self.tableMutants.setLineWidth(1)
        self.tableMutants.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableMutants.setAlternatingRowColors(True)
        self.tableMutants.setObjectName("tableMutants")
        self.tableMutants.setColumnCount(5)
        self.tableMutants.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon1)
        self.tableMutants.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/img/sum_icon_151075.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon8)
        self.tableMutants.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableMutants.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon3)
        self.tableMutants.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon6)
        self.tableMutants.setHorizontalHeaderItem(4, item)
        self.textTaskMutant = QtWidgets.QTextBrowser(self.groupBox)
        self.textTaskMutant.setGeometry(QtCore.QRect(0, 10, 781, 65))
        self.textTaskMutant.setStyleSheet("background-color: rgb(36, 72, 0);\n"
"color: rgb(221, 221, 221);")
        self.textTaskMutant.setObjectName("textTaskMutant")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 80, 281, 22))
        self.comboBox_3.setStyleSheet("border: 1px solid rgb(117, 117, 117);\n"
"border-radius: 5px;\n"
"background-color: rgb(159, 161, 119);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboFishMut = QtWidgets.QComboBox(self.groupBox)
        self.comboFishMut.setGeometry(QtCore.QRect(300, 80, 251, 22))
        self.comboFishMut.setStyleSheet("border: 1px solid rgb(117, 117, 117);\n"
"border-radius: 5px;\n"
"background-color: rgb(159, 161, 119);")
        self.comboFishMut.setObjectName("comboFishMut")
        self.pushSearchMutants = QtWidgets.QPushButton(self.groupBox)
        self.pushSearchMutants.setGeometry(QtCore.QRect(10, 500, 121, 23))
        self.pushSearchMutants.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pushSearchMutants.setObjectName("pushSearchMutants")
        self.pushTaskMutant = QtWidgets.QPushButton(self.groupBox)
        self.pushTaskMutant.setGeometry(QtCore.QRect(559, 80, 211, 23))
        self.pushTaskMutant.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"")
        self.pushTaskMutant.setObjectName("pushTaskMutant")
        self.pushReset = QtWidgets.QPushButton(self.groupBox)
        self.pushReset.setGeometry(QtCore.QRect(256, 500, 111, 23))
        self.pushReset.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pushReset.setObjectName("pushReset")
        self.pushSearchFish = QtWidgets.QPushButton(self.groupBox)
        self.pushSearchFish.setGeometry(QtCore.QRect(137, 500, 111, 23))
        self.pushSearchFish.setStyleSheet("background-color: rgb(124, 124, 93);\n"
"color: #000;\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.pushSearchFish.setObjectName("pushSearchFish")
        self.lcd4 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcd4.setGeometry(QtCore.QRect(669, 490, 101, 23))
        self.lcd4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd4.setDigitCount(10)
        self.lcd4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd4.setObjectName("lcd4")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????? ?????????????? ?????????????? 1.04"))
        self.label.setText(_translate("MainWindow", "??????????????: ?????????????????? ???????????? ?????????????????? ??????????????"))
        self.label_2.setText(_translate("MainWindow", "??????????????: ???????????????? ???????????????? ????????"))
        self.table2.setSortingEnabled(False)
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????-????"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????"))
        item = self.table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "????????"))
        item = self.table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.table2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "??????"))
        item = self.table2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "??????"))
        item = self.table2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "??????????????"))
        self.btnTask.setText(_translate("MainWindow", "1. ???????????????? ??????????????"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri Light\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.btnSearch.setText(_translate("MainWindow", "2. ??????????"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "????????"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "??????????????"))
        self.label_6.setText(_translate("MainWindow", "?????????? ????????:"))
        self.label_7.setText(_translate("MainWindow", "?????????? ????????:"))
        self.label_8.setText(_translate("MainWindow", "?????????????? ??????:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "????????????????????????"))
        self.tableBait.setSortingEnabled(False)
        item = self.tableBait.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????-????"))
        item = self.tableBait.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableBait.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableBait.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableBait.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableBait.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "??????????????"))
        self.pushBait.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "??????????????"))
        self.pushSafari.setText(_translate("MainWindow", "?????????????? ??????????????"))
        self.tableSafari.setSortingEnabled(False)
        item = self.tableSafari.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableSafari.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????"))
        item = self.tableSafari.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "????"))
        item = self.tableSafari.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableSafari.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.tableSafari.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.tableSafari.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "???????????? ????????????"))
        item = self.tableMutants.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableMutants.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableMutants.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableMutants.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.tableMutants.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "??????????????"))
        self.textTaskMutant.setMarkdown(_translate("MainWindow", "?????????????????????????? ???????????? ???????? ?????? (??????????????):\n"
"\n"
""))
        self.textTaskMutant.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">?????????????????????????? ???????????? ???????? ?????? (??????????????):</span></p></body></html>"))
        self.pushSearchMutants.setText(_translate("MainWindow", "2. ?????????? ??????????????"))
        self.pushTaskMutant.setText(_translate("MainWindow", "1. ???????????????? ??????????????"))
        self.pushReset.setText(_translate("MainWindow", "??????????"))
        self.pushSearchFish.setText(_translate("MainWindow", "?????????? ????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "?????????? ????????????????????"))
import res_rc
