import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets, Qt, QtCore, QtGui, uic

import MainWindow2  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, MainWindow2.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ExampleApp, self).__init__(*args, **kwargs)
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        # при нажатии кнопки

    def plot(self, hour, temperature):
        self.GraphWidget.plot(hour, temperature)

    def browse_folder(self):
        x = []
        y = []
        T1 = self.comboBox.currentText()
        r1 = self.doubleSpinBox.value()
        r2 = self.doubleSpinBox_2.value()
        for i in range(0, 100):
            x.append(int(r1 + i))
            y.append(int((r1 + i) ** 2))

        if T1 == "Транзистор":
            self.GraphWidget.clear()
            self.listWidget.clear()
            self.listWidget.addItem(str(r1 * r2))
            self.plot(x, y)
        if T1 == "Резистор":
            self.GraphWidget.clear()
            self.listWidget.clear()
            self.listWidget.addItem(str(r1 + r2))
            self.plot(x, y)
        if T1 == "Конденсатор":
            self.GraphWidget.clear()
            self.listWidget.clear()
            self.listWidget.addItem(str(r1 // r2))
            self.plot(x, y)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
