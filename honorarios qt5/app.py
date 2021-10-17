from honorarios import *
from teste import *
import sys


class App(Ui_Form):
    def __init__(self, window):
        self.setupUi(window)
        self.CalcButton.clicked.connect(self.clickCalc)
        self.CleanButton.clicked.connect(self.clear)
        self.CloseButton.clicked.connect(self.closeApp)

    def clickCalc(self):
        salario = self.SalarioMin.text()
        condenacao = self.Condenacao.text()
        artigo = Artigo85()
        try:
            min = artigo.honorarios_min(salario, condenacao)
            max = artigo.honorarios_max(salario, condenacao)
            self.MinResult.setText("R$:" + str(min))
            self.MaxResult.setText("R$:" + str(max))
            return
        except ValueError:
            return "Erro"

    def clear(self):
        self.SalarioMin.setText("")
        self.Condenacao.setText("")
        self.MinResult.setText("")
        self.MaxResult.setText("")
        return print("Tudo limpo!")

    def closeApp(self):
        app.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App(MainWindow)
    MainWindow.show()
    app.exec_()
