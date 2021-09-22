from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('ELABORE UMA FUNÇÃO QUE RECEBA TRÊS NOTAS DE UM ALUNO COMO PARÂMETROS E UMA LETRA.',
                                 'SE A LETRA FOR A, A FUNÇÃO DEVERÁ CALCULAR A MÉDIA ARITMÉTICA DAS NOTAS DO ALUNO;'
                                 ' SE FOR P, DEVERÁ CALCULAR A MÉDIA PONDERADA, COM PESOS 5, 3 E 2.', 160)

    primeiro = float(input('Digite 1º nota: ').replace(',', '.'))
    segundo = float(input('Digite 2º nota: ').replace(',', '.'))
    terceiro = float(input('Digite 3º nota: ').replace(',', '.'))
    opcao = str(input('Digite A para média aritmética e P para ponderada: ').capitalize())

    calculoDeMedia(primeiro, segundo, terceiro, opcao)


def calculoDeMedia(primeiro, segundo, terceiro, letra):
    if(letra != 'A' and letra != 'P'):
        letra = 'A'
    if(letra == 'A'):
        media = (primeiro + segundo + terceiro)/3
        print('\nMédia Aritmética:', media)
    else:
        media = ((primeiro*5) + (segundo*3) + (terceiro*2))/ (5+3+2)
        print('\nMédia Ponderada:', media)


if __name__ == '__main__':
    main()
