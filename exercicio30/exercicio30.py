from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes(
        'FAÇA UM ALGORITMO QUE CALCULE A MÉDIA PONDERADA DAS NOTAS DE 3 PROVAS. A PRIMEIRA E A SEGUNDA PROVA TEM PESO 1 E A TERCEIRA TEM PESO 2. ',
        'AO FINAL, MOSTRAR A MÉDIA DO ALUNO E INDICAR SE O ALUNO FOI APROVADO OU REPROVADO. A NOTA PARA APROVAÇÃO DEVE SER IGUAL OU SUPERIOR A  60 PONTOS.', 160)

    primeiraNota = float(input(f'Digite a 1ª nota: ').replace(',', '.'))
    segundaNota = float(input(f'Digite a 2ª nota: ').replace(',', '.'))
    terceiraNota = float(input(f'Digite a 3ª nota: ').replace(',', '.'))

    pesoUm = 1
    pesoDois = 2

    if validacaoDeNota(primeiraNota) and validacaoDeNota(segundaNota) and validacaoDeNota(terceiraNota):
        mediaPonderada = (primeiraNota*pesoUm + segundaNota*pesoUm + terceiraNota*pesoDois) / (pesoUm+pesoDois)
        if mediaPonderada > 6:
            print('APROVADO')
            return
        print('REPROVADO')
        return
    print('OOOOOOOPS, Nota invalida')


def validacaoDeNota(nota):
    if nota <= 10 and nota >= 0:
        return True
    return False


if __name__ == '__main__':
    main()
