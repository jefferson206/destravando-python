from listaExercicio.uteis.util import Util
from datetime import date

def main():
    Util().enunciado('MPLEMENTE UM PROGRAMA QUE CALCULE O ANO DE NASCIMENTO DE UMA PESSOA A PARTIR DE SUA IDADE E DO ANO ATUAL.')

    anoAtual = date.today().year
    idade = int(input(f'Digite o sua idade: '))

    print('Você é nascido no ano de:', anoAtual-idade)

if __name__ == '__main__':
    main()