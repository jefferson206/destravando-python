from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA 10 INTEIROS POSITIVOS, IGNORANDO NAO POSITIVOS, E IMPRIMA SUA MÉDIA.')

    somaDosValores = 0
    valoresParaMedia = 0
    for contador in range(1, 11):
        valor = int(input(f'Digite o {contador}ª valor: '))
        if valor >= 0:
            valoresParaMedia += 1
            somaDosValores += valor

    media = float(somaDosValores/valoresParaMedia)

    print('\nA média dos valoores positivos ignorando os negatiivos foi de:', media)

if __name__ == '__main__':
    main()
