from gui import Ui_Dialog
from PyQt5 import QtWidgets


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создаем окно
        Ui_Dialog.__init__(self)
        # Устанавливаем пользовательский интерфейс
        self.setupUi(dialog)
