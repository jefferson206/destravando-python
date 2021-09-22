from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('FAÇA UM PROGRAMA QUE LEIA O VALOR DA HORA DE TRABALHO (EM REAIS) E NÉMERO DE HORAS TRABALHADAS NO MÊS. ',
                     'IMPRIMA O VALOR A SER PAGO AO FUNCIONÁRIO, ADICIONANDO  10 % SOBRE O VALOR CALCULADO', 120)

    valorHora = float(input(f'Digite o valor da hora de trabalho: ').replace(',', '.'))
    horasTrabalhadas = float(input(f'Digite a quantidade de horas trabalhadas no mês: ').replace(',', '.'))

    valorASerPago = (valorHora*horasTrabalhadas)
    valorASerPagoComReajuste = (valorASerPago*0.10)+valorASerPago
    print('Seu salarial é de:', round(valorASerPagoComReajuste, 2))

if __name__ == '__main__':
    main()