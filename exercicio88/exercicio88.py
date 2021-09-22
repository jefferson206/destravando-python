from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('FAÇA UMA FUNÇÃO PARA VERIFICAR SE UM NÚMERO É POSITIVO OU NEGATIVO.',
                                 'SENDO QUE O VALOR DE RETORNO SERA 1 SE POSITIVO, -1 SE NEGATIVO E 0 SE FOR IGUAL A 0.')

    try:
        valor = float(input('Digite um valor: ').replace(',', '.'))
        validaSePositivoOuNegativo(valor)
    except:
        print('Só pode ser valores numericos')



def validaSePositivoOuNegativo(valor):
    if valor == 0:
        print(0)
    elif valor > 0:
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
