import PySimpleGUIQt as sg
import Artigo85 as art

sg.theme("dark grey 5")
layout = [
    [sg.Text("Salário Mínimo:", key="_key_")],
    [sg.InputText(background_color="white")],
    [sg.Text("Valor da condenação:")],
    [sg.InputText(background_color="white")],
    [sg.Output(background_color="white", key="_OUT_")],
    [sg.Button("Ok")],
    [sg.Button("Limpar")],
    [sg.Button("Fechar")],
]

window = sg.Window("Fixação de Honorários", layout)

while True:
    event, value = window.Read()
    if event in (sg.WIN_CLOSED, "Fechar"):
        break
    if event == "Limpar":
        window["_OUT_"].update("")
    if event in (sg.Ok, "Ok"):
        try:
            artigo = art.Artigo85()
            a = artigo.honorarios_min(float(value[0]), float(value[1]))
            b = artigo.honorarios_max(float(value[0]), float(value[1]))
            print(a[0] + " " + "{:.2f}".format(a[1]))
            print(b[0] + " " + "{:.2f}".format(b[1]))
            window.Refresh()

        except Exception:
            sg.PopupError(
                """Somente números são aceitos e não esqueça de
                          \nusar . no lugar de , para valores com decimais.""",
                title="Atenção!",
            )
