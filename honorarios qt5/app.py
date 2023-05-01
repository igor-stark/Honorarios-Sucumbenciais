from honorarios import *
from teste import *
import sys


class App(Ui_Form):
    def __init__(self, window):
        self.setupUi(window)
        self.CalcButton.clicked.connect(self.clickCalc)
        self.CleanButton.clicked.connect(self.clear)
        self.CloseButton.clicked.connect(self.closeApp)
        
        # Lista de QLabels usadas tanto como input quanto output
        self.label_list = [
            self.SalarioMin,
            self.Condenacao,
            self.MinResult,
            self.MaxResult,
        ]

    def clickCalc(self):
        salario = self.SalarioMin.text()
        condenacao = self.Condenacao.text()
        artigo = Artigo85()
        try:
            min = artigo.honorarios_min(salario, condenacao)
            max = artigo.honorarios_max(salario, condenacao)
            self.MinResult.setText("R$:" + '{:.2f}'.format(min))
            self.MaxResult.setText("R$:" + '{:.2f}'.format(max))
            return
        except ValueError:
            return "Erro"

    def clear(self):
        for label in self.label_list:
            label.clear()
        return

    def closeApp(self):
        app.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
