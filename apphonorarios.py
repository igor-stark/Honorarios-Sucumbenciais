import PySimpleGUIQt as sg
import fixar_honorarios as fh

sg.theme('dark grey 5')
layout = [[sg.Text("Salário Mínimo:", key='_key_')],
          [sg.InputText(background_color='white')],
          [sg.Text("Valor da condenação:")],
          [sg.InputText(background_color='white')],
          [sg.Output(background_color='white', key='_OUT_')],
          [sg.Button('Ok')],
          [sg.Button('Limpar')],
          [sg.Button('Fechar')]]

window = sg.Window('Fixação de Honorários', layout)

while True:
    event, value = window.Read()
    if event in (sg.WIN_CLOSED, 'Fechar'):
        break
    if event == 'Limpar':
        window['_OUT_'].update('')
    if event in (sg.Ok, 'Ok'):
        try:
            a = (fh.honorarios_min(float(value[0]), float(value[1])))
            b = (fh.honorarios_max(float(value[0]), float(value[1])))
            print(a[0] + " " + str(a[1]))
            print(b[0] + " " + str(b[1]))
            window.Refresh()
        except Exception:
            sg.PopupError("""Somente números são aceitos e não esqueça de
                          \nusar . no lugar de , para valores com decimais.""",
                          title='Atenção!')
