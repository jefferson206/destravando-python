from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('CALCULE A MÉDIA ARITMÉTICA DAS 3 NOTAS DE UM ALUNO E MOSTRE, ALÉM DO VALOR DA MÉDIA, ',
                                 'UMA MENSAGEM DE " APROVADO", CASO A MÉDIA SEJA IGUAL OU SUPERIOR A 6, OU A MENSAGEM " REPROVADO", CASO CONTRÁRIO.', 140)

    somaDasNotas = 0.0
    for nota in range(1, 4):
        valor = float(input(f'Digite a {nota}ª nota: ').replace(',', '.'))
        somaDasNotas += valor

    media = round(somaDasNotas/3, 2)

    if media >= 6:
        print('Sua média:', media, '\nPARABENS... você foi aprovado!')
    else:
        print('Sua média:', media, '\nOOOOPSSS... te vejo ano que vem.... você foi REPROOVADO!')


if __name__ == '__main__':
    main()
