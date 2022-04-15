import sys, sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import MainWindowFinal
from bd import all_results4, all_results5, all_results6

conn = sqlite3.connect(r'info.db')
cur = conn.cursor()


class ExampleApp(QtWidgets.QMainWindow, MainWindowFinal.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ExampleApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)
        self.comboBox.currentTextChanged.connect(self.combo)
        self.initUI()

    def combo(self):
        if self.comboBox.currentText() == 'Микросхемы интегральные полупроводниковые цифровые':
            self.comboBox_3.clear()
            for i in range(len(all_results4)):
                self.comboBox_3.addItem(all_results4[i][1])
        if self.comboBox.currentText() == 'Микросхемы интегральные полупроводниковые аналоговые':
            self.comboBox_3.clear()
            for i in range(len(all_results5)):
                self.comboBox_3.addItem(all_results5[i][1])
        if self.comboBox.currentText() == 'Микросхемы  интегральные гибридные':
            self.comboBox_3.clear()
            for i in range(len(all_results6)):
                self.comboBox_3.addItem(all_results6[i][1])

    def initUI(self):
        self.setWindowTitle('Руки-крюки')
        self.setWindowIcon(QIcon('icon.ico'))

        self.show()

    def plot(self, hour, temperature):
        self.GraphWidget.plot(hour, temperature)

    def browse_folder(self):
        x = []
        y = []
        T1 = self.comboBox.currentText()
        T = self.comboBox_3.currentText()
        T2 = self.comboBox_2.currentText()
        T3 = self.comboBox_4.currentText()
        X = self.doubleSpinBox.value()
        D = self.doubleSpinBox_2.value()
        if T1 == 'Микросхемы интегральные полупроводниковые цифровые':
            cur.execute("SELECT * FROM digital WHERE name=?", (T,))
            data = cur.fetchone()
            k = float(data[2])
            b = float(data[3])
        elif T1 == 'Микросхемы интегральные полупроводниковые аналоговые':
            cur.execute("SELECT * FROM analog WHERE name=?", (T,))
            data = cur.fetchone()
            k = float(data[2])
            b = float(data[3])
        elif T1 == 'Микросхемы  интегральные гибридные':
            cur.execute("SELECT * FROM hybrid WHERE name=?", (T,))
            data = cur.fetchone()
            k = float(data[2])
            b = float(data[3])
        temp = (k * X + b)
        cur.execute("SELECT * FROM groups WHERE name=?", (T1,))
        group = cur.fetchone()
        A = float(group[2])
        cur.execute("SELECT * FROM app WHERE name=?", (T2,))
        app = cur.fetchone()
        B = float(app[2])
        cur.execute("SELECT * FROM material WHERE name=?", (T3,))
        material = cur.fetchone()
        C = float(material[2])
        self.listWidget.clear()
        try:
            Y = (1 / (A * B * C * temp * D * 10 ** (-6)))
            self.listWidget.addItem(
                ('Данный компонент прослужит примерно ' +
                 str(round(Y / (24 * 365), 2)) + ' лет или год(а).'))
            self.listWidget.addItem(
                'Данный компонент прослужит примерно ' +
                str(round(Y, 2)) + ' часов.')
            self.listWidget.addItem('График выхождения из строя представлен в годах службы от процента износа.')
        except ZeroDivisionError:
            self.listWidget.addItem("Введите значения температуры и напряжения!")

        for i in range(1, 101):
            x.append(int(i))
            y.append((float((Y / (24 * 365)) / i)))
            self.GraphWidget.clear()
            self.plot(x, y)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
