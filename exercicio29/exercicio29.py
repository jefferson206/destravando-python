from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes(
        'FAÇA UM PROGRAMA QUE LEIA 2 NOTAS DE UM ALUNO, VERIFIQUE SE AS NOTAS SAO VÁLIDAS E EXIBA NA TELA A MÉDIA DESTAS NOTAS. ',
        'UMA NOTA VÁLIDA DEVE SER, OBRIGATORIAMENTE, UM VALOR ENTRE 0.0 E 10. 0, ONDE CASO A NOTA NAO POSSUA UM VALOR VÁLIDO, '
        'ESTE FATO DEVE SER INFORMADO AO USUÁRIO E O PROGRAMA TERMINA.', 180)

    primeiraNota = float(input(f'Digite a 1ª nota: ').replace(',', '.'))
    segundaNota = float(input(f'Digite a 2ª nota: ').replace(',', '.'))

    if validacaoDeNota(primeiraNota) and validacaoDeNota(segundaNota):
        media = (primeiraNota + segundaNota) / 2
        print('A média é de: {}'.format(round(media, 2)))
        return
    print('OOOOOOOPS, Nota invalida')


def validacaoDeNota(nota):
    if nota <= 10 and nota >= 0:
        return True
    return False


if __name__ == '__main__':
    main()
