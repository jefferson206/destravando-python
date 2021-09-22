import PySimpleGUI as gui

class UtilGui:
    def janela_resultado():
        layout = [
            [gui.Text('', key='resultado', size=(50, 1))],
            [gui.Button('Voltar'), gui.Button('Fechar')]
        ]
        return gui.Window('Resultado', layout, finalize=True)

    def janela_principal(enunciado):
        layout = [
            [gui.Text(enunciado, justification='center')],
            [gui.Text('-' * len(enunciado) * 2)],
            [gui.Text('Valor', size=(5, 1)), gui.InputText(size=(len(enunciado)), key='valor')],
            [gui.Button('Enviar dados')],
        ]

        return gui.Window('Programa simples', layout, finalize=True)
