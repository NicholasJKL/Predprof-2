import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets, Qt

import MainWindow  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        self.doubleSpinBox = Qt.QSpinBox()
        self.doubleSpinBox_2 = Qt.QSpinBox()
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        # при нажатии кнопки

    def browse_folder(self):
        r1 = self.doubleSpinBox.value()
        r2 = self.doubleSpinBox_2.value()
        self.listWidget.clear()
        self.listWidget.addItem(str(r1*r2))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
