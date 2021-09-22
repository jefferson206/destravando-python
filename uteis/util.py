class Util:
    def enunciado(self, nome):
        espaco = ' '
        align = '^'
        width = len(nome)+15
        print('-' * width + '----')
        print('| {0:{1}{2}} |'.format(espaco, align, width))
        print('| {0:{1}{2}} |'.format(nome, align, width))
        print('| {0:{1}{2}} |'.format(espaco, align, width))
        print('-' * width + '----')

    def enunciadoEmDuasPartes(self, parte1, parte2, width=100):
        espaco = ' '
        align = '^'
        print('-' * width + '----')
        print('| {0:{1}{2}} |'.format(espaco, align, width))
        print('| {0:{1}{2}} |'.format(parte1, align, width))
        print('| {0:{1}{2}} |'.format(parte2, align, width))
        print('| {0:{1}{2}} |'.format(espaco, align, width))
        print('-' * width + '----')
