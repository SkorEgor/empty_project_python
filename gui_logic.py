from gui import Ui_Dialog


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # ПОЛЯ КЛАССА


        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс
