from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('RECEBA O SALÁRIO-BASE DE UM FUNCIONÁRIO. CALCULE E IMPRIMA O SALÃRIO A RECEBER, ',
                     'SABENDO-SE QUE ESSE FUNCIOÁRIO TEM UMA GRATIFICAÇÃO DE 5 % SOBRE O SALÁRIO-BASE. ALÉM DISSO, ELE PAGA 7 % DE IMPOSTO SOBRE O SALÁRIO- BASE.', 180)

    salarioBase = float(input(f'Digite o salário base: ').replace(',', '.'))
    ajuste = (salarioBase*0.05)+salarioBase
    desconto = (ajuste*7/100)

    print('Salario liquido:', round(ajuste-desconto, 2))

if __name__ == '__main__':
    main()