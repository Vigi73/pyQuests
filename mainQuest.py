from PyQt5 import QtWidgets
from MainForm import Ui_MainWindow
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from search import search_location_classic, all_fish, all_fish_bait, get_safari
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QCheckBox
from bases import bases_name
from fishes import fish_name
from Fishes_m import fish_m
from Maps import base_mut
import xml.etree.cElementTree as ET
import sys
import re
import pyperclip

app = QtWidgets.QApplication([])


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Constructor of the Main Window class"""
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)  # Forbidding U-turns

        self.ui.tableMutants.horizontalHeader().setDefaultSectionSize(139)  # setting the column size
        self.ui.table.horizontalHeader().setDefaultSectionSize(240)  # setting the column size

        # style for header grid -----------------------------------------------------------------------------
        stylesheet = "::section{Background-color: rgb(36, 72, 0); color: #c6c663}"
        self.ui.table.horizontalHeader().setStyleSheet(stylesheet)
        self.ui.table.verticalHeader().setStyleSheet(stylesheet)
        self.ui.table2.horizontalHeader().setStyleSheet(stylesheet)
        self.ui.table2.verticalHeader().setStyleSheet(stylesheet)
        self.ui.tableBait.horizontalHeader().setStyleSheet(stylesheet)
        self.ui.tableBait.verticalHeader().setStyleSheet(stylesheet)
        self.ui.tableSafari.horizontalHeader().setStyleSheet(stylesheet)
        self.ui.tableSafari.verticalHeader().setStyleSheet(stylesheet)
        self.ui.tableMutants.horizontalHeader().setStyleSheet(stylesheet)
        self.ui.tableMutants.verticalHeader().setStyleSheet(stylesheet)
        # -----------------------------------------------------------------------------------------------------

        # Event for classic
        self.ui.btnTask.clicked.connect(self.insert_task)  # we hang the event on the insert task button(Classic)
        self.ui.btnSearch.clicked.connect(self.search_location)  # we hang the event on the find button (Classic)

        # Event for Bait
        self.ui.pushBait.clicked.connect(self.insert_task_bait)
        self.ui.listWidget.clicked.connect(self.res_result)

        # Event for Safari
        self.ui.pushSafari.clicked.connect(self.table_safari_clicked)  # Click on the insert task button (Safari)

        # Event for get Task Mutant
        self.ui.pushTaskMutant.clicked.connect(self.task_in)

        # Event for search Mutant
        self.ui.pushSearchMutants.clicked.connect(self.search_mutants)

        # Event for Reset Mutant
        self.ui.pushReset.clicked.connect(self.add_all_mutants)

        # Event for search Fish Mutant
        self.ui.pushSearchFish.clicked.connect(self.search_fish_name)

    def search_fish_name(self):
        self.ui.tableMutants.setRowCount(0)  # table clear
        tree = ET.parse('mutants.xml')
        request = tree.findall(f'Mutant[Name="{self.ui.comboFishMut.currentText()}"]')

        for i, elm in enumerate(request):
            try:
                self.ui.tableMutants.setRowCount(i + 1)
                self.ui.tableMutants.setItem(i, 0, QTableWidgetItem(elm[0].text))
                self.ui.tableMutants.setItem(i, 1, QTableWidgetItem(elm[1].text.split()[0]))
                self.ui.tableMutants.setItem(i, 2, QTableWidgetItem(elm[2].text))
                self.ui.tableMutants.setItem(i, 3, QTableWidgetItem(elm[3].text))
                self.ui.tableMutants.setItem(i, 4, QTableWidgetItem(elm[4].text))
            except:
                continue
        self.ui.lcd4.display(self.ui.tableMutants.rowCount())

    def search_mutants(self):
        self.ui.tableMutants.setRowCount(0)  # table clear
        tree = ET.parse('mutants.xml')
        request = tree.findall(f'Mutant[Name="{self.ui.comboFishMut.currentText()}"][Map="{self.ui.comboBox_3.currentText()}"]')

        for i, elm in enumerate(request):
            try:
                self.ui.tableMutants.setRowCount(i + 1)
                self.ui.tableMutants.setItem(i, 0, QTableWidgetItem(elm[0].text))
                self.ui.tableMutants.setItem(i, 1, QTableWidgetItem(elm[1].text.split()[0]))
                self.ui.tableMutants.setItem(i, 2, QTableWidgetItem(elm[2].text))
                self.ui.tableMutants.setItem(i, 3, QTableWidgetItem(elm[3].text))
                self.ui.tableMutants.setItem(i, 4, QTableWidgetItem(elm[4].text))
            except:
                continue
        self.ui.lcd4.display(self.ui.tableMutants.rowCount())

    def task_in(self):
        '''Enter Task in ComboBox for Mutants'''
        try:
            tmp_list = pyperclip.paste()
            self.ui.textTaskMutant.setMarkdown(f"<h3 style='text-align: center; color: #fff;'>{tmp_list}</h3>")

            base_mut = tmp_list[tmp_list.find("	На водоеме ") + 12:][:tmp_list.find("разыскивается") - 13].strip()
            self.ui.comboBox_3.setCurrentText(base_mut)

            fish_mut = tmp_list[tmp_list.find("разыскивается") + 14:].split('.')[0].strip()
            fansw = fish_mut[0].upper() + fish_mut[1:]
            self.ui.comboFishMut.setCurrentText(fansw)

        except:
            pass

    def table_safari_clicked(self):
        ''' Заполняем таблицу сафари'''
        self.ui.tableSafari.setRowCount(0)  # table clear

        # self.tableSafari.appendRow(item)
        try:
            tmp_list = pyperclip.paste()
            j = 0
            for j, elem in enumerate([e for e in re.split(r'[\n]', tmp_list) if e]):
                fish = re.split('-?[0-9]+', elem)[0].strip()
                min_fish = [e for e in re.findall('-?[0-9,]+', elem) if e]
                self.ui.tableSafari.setRowCount(j + 1)
                self.ui.tableSafari.setItem(j, 0, QTableWidgetItem(fish))
                self.ui.tableSafari.setItem(j, 1, QTableWidgetItem(min_fish[0]))
                self.ui.tableSafari.setItem(j, 2, QTableWidgetItem(min_fish[1]))
                self.ui.tableSafari.setItem(j, 3, QTableWidgetItem(get_safari(fish)[2]))
                self.ui.tableSafari.setItem(j, 4, QTableWidgetItem(get_safari(fish)[5]))
                self.ui.tableSafari.setItem(j, 5, QTableWidgetItem(get_safari(fish)[6]))

            # self.tableSafari.setRowCount(j )

            try:
                # self.ui.label_5.setText(f'Найдено: {self.ui.tableSafari.rowCount()}')
                self.ui.lcd3.display(self.ui.tableSafari.rowCount())

            except:
                pass

        except:
            pass

    def res_result(self):
        '''Выводим в таблицу результат по наживке'''
        self.ui.tableBait.setRowCount(0)  # очиска таблицы
        bait = self.ui.listWidget.currentItem().text().split('.')[1].split('(')[0].strip()
        all_baits = all_fish_bait(bait)

        i = 0
        for i, elem in enumerate(all_baits):
            self.ui.tableBait.setRowCount(i + 1)
            self.ui.tableBait.setItem(i, 0, QTableWidgetItem(str(elem[0])))
            self.ui.tableBait.setItem(i, 1, QTableWidgetItem(elem[1]))
            self.ui.tableBait.setItem(i, 2, QTableWidgetItem(str(elem[3])))
            self.ui.tableBait.setItem(i, 3, QTableWidgetItem(str(elem[4])))
            self.ui.tableBait.setItem(i, 4, QTableWidgetItem(elem[2]))
            self.ui.tableBait.setItem(i, 5, QTableWidgetItem(elem[5]))

        try:
            # self.ui.label_4.setText(f'Найдено: {self.ui.tableBait.rowCount()}')
            self.ui.lcd2.display(self.ui.tableBait.rowCount())

        except:
            pass
        self.ui.tableBait.resizeColumnsToContents()

    def insert_task_bait(self):
        '''Добавляем задание в ListEdit'''
        self.ui.listWidget.clear()
        try:
            tmp_list = pyperclip.paste()
            for i, elm in enumerate(tmp_list.split('\n'), start=1):
                self.ui.listWidget.addItem(f'{i}. {elm}')
        except:
            pass

    def add_base(self):
        '''Добавляем список баз'''
        for i in [bas for bas in bases_name.split('\n') if bas]:
            self.ui.comboBox.addItem(i.strip())

    def add_fish(self):
        '''Добавляем список рыб'''
        for i in fish_name.split('\n'):
            self.ui.comboBox_2.addItem(i.strip())

    def add_fish_m(self):
        '''Добавляем список рыб Мутантов'''
        for i in fish_m.split('\n'):
            self.ui.comboFishMut.addItem(i.strip())

    def add_base_m(self):
        '''Добавляем список Баз Мутантов'''
        for i in base_mut.split('\n'):
            self.ui.comboBox_3.addItem(i.strip())

    def add_all_mutants(self):
        """Добавляем в таблицу всех мутов"""
        self.ui.tableMutants.setRowCount(0)  # table clear
        tree = ET.parse('mutants.xml')
        for i, elm in enumerate(tree.findall('Mutant')[1:]):
            try:
                self.ui.tableMutants.setRowCount(i + 1)
                self.ui.tableMutants.setItem(i, 0, QTableWidgetItem(elm[0].text))
                self.ui.tableMutants.setItem(i, 1, QTableWidgetItem(elm[1].text.split()[0]))
                self.ui.tableMutants.setItem(i, 2, QTableWidgetItem(elm[2].text))
                self.ui.tableMutants.setItem(i, 3, QTableWidgetItem(elm[3].text))
                self.ui.tableMutants.setItem(i, 4, QTableWidgetItem(elm[4].text))
            except:
                continue

        self.ui.lcd4.display(self.ui.tableMutants.rowCount())

    def insert_task(self):
        '''Всавляе задачу для классики из буфера'''
        try:
            tmp_list = pyperclip.paste()
            self.ui.textEdit.setText(tmp_list)
            bases = self.ui.textEdit.toPlainText().split('(')[1].split(')')[0].split(':')[0].strip()
            self.ui.comboBox.setCurrentText(bases)
            tmp = self.ui.textEdit.toPlainText().split('(')[1].split(')')[0].split(':')[1]
            # "-?[0-9]+"
            fish = re.split("-?[0-9]+", tmp)[0].strip()
            self.ui.comboBox_2.setCurrentText(fish)
            tw_fish = re.findall("-?[0-9]+", tmp)
            w_fish = f'{tw_fish[0]},{tw_fish[1]}'
            self.ui.doubleSpinBox.setSpecialValueText(w_fish)

            # print(fish)
        except:
            pass

    def search_location(self):
        """Поиск и добовление в таблицу результата классика"""
        self.ui.table.setRowCount(0)
        self.ui.table2.setRowCount(0)
        fish_name = self.ui.comboBox_2.currentText()
        base = self.ui.comboBox.currentText()
        answer = search_location_classic(fish_name, base)
        self.ui.table.setRowCount(1)

        # self.table.setItem(0, 0, QTableWidgetItem(str(answer*[1])))
        try:
            for i in answer:
                self.ui.table.setItem(0, 0, QTableWidgetItem(i[1]))
                self.ui.table.setItem(0, 1, QTableWidgetItem(i[5]))
                self.ui.table.setItem(0, 2, QTableWidgetItem(i[6]))
        except:
            pass
        # self.table.resizeColumnsToContents()
        # self.grid_layout.addWidget(self.table, 0, 0)
        # Другая таблица
        all_result = all_fish(fish_name)
        self.ui.table.resizeColumnsToContents()

        for item, result in enumerate(all_result):
            self.ui.table2.setRowCount(item + 1)
            self.ui.table2.setItem(item, 0, QTableWidgetItem(str(result[0])))
            self.ui.table2.setItem(item, 1, QTableWidgetItem(result[1]))
            self.ui.table2.setItem(item, 2, QTableWidgetItem(result[2]))
            self.ui.table2.setItem(item, 3, QTableWidgetItem(result[5]))
            self.ui.table2.setItem(item, 4, QTableWidgetItem(str(result[3])))
            self.ui.table2.setItem(item, 5, QTableWidgetItem(str(result[4])))
            self.ui.table2.setItem(item, 6, QTableWidgetItem(result[6]))
        # self.table2.resizeColumnsToContents()
        # self.ui.label_3.setText(f'Найдено: {self.ui.table2.rowCount()}')

        self.ui.lcd1.display(self.ui.table2.rowCount())
        self.ui.table.horizontalHeader().setDefaultSectionSize(240)


if __name__ == '__main__':
    application = MyWindow()
    application.add_base()
    application.add_fish()
    application.add_fish_m()
    application.add_base_m()
    application.add_all_mutants()

    application.show()

    sys.exit(app.exec())
