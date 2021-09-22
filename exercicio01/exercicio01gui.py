from listaExercicio.uteis.utilGui import UtilGui
import PySimpleGUI as gui

def main():
    enunciado = 'FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E O IMPRIMA.'
    janela1, janela2 = UtilGui.janela_principal(enunciado), None

    while True:
        window, event, values = gui.read_all_windows()
        errorCall = "Please only enter numbers."
        if window == janela1 and event == gui.WINDOW_CLOSED or window == janela2 and event == gui.WINDOW_CLOSED:
            break
        if window == janela1 and event == 'Enviar dados':
            try:
                teste = int(values["valor"])
            except ValueError:
                gui.PopupOKCancel(errorCall)
                return
            janela1.hide()
            janela2 = UtilGui.janela_resultado()
            window = janela2
            window['resultado'].update(f'Valor digitado: { values["valor"] }')
        if window == janela2 and event == 'Voltar':
            janela2.hide()
            janela1.un_hide()
        if window == janela2 and event == 'Fechar':
            gui.WINDOW_CLOSED
            break

if __name__ == '__main__':
    main()