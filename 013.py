#calculadora Básica
def calculadora_basica():
    from time import sleep
    while True:
        print('-=' * 20)
        print('           \033[35:40mCalculadora Básica\033[m')
        print('-=' * 20)
        print("""        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Sair""""")
        opcao = int(input('Qual desejas escolher: '))
        if opcao == 1:
            print('-=' * 20)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o outro valor: '))
            resu = v1 + v2
            sleep(3)
            print(f'{v1} + {v2} = {resu}')
            print('-=' * 20)
        elif opcao == 2:
            print('-=' * 20)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o outro valor: '))
            resu = v1 - v2
            sleep(3)
            print(f'{v1} - {v2} = {resu}')
            print('-=' * 20)
        elif opcao == 3:
            print('-=' * 20)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o outro valor: '))
            resu = v1 * v2
            sleep(3)
            print(f'{v1} x {v2} = {resu}')
            print('-=' * 20)
        elif opcao == 4:
            print('-=' * 20)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o outro valor: '))
            resu = v1 / v2
            sleep(3)
            print(f'{v1} / {v2} = {int(resu)}')
            print('-=' * 20)
        elif opcao == 5:
            break1
        resp = ' '
        while resp not in 'SN':
            resp = input('Quer continuar [S-N]: ').strip().upper()[0]
            print('-=' * 20)
        if resp == 'N':
            break
    sleep(1)
21
#Calcular Desconto
def calcular_desconto():
    from time import sleep
    while True:
        print('-=' * 20)
        print('          \033[32:40mCalculo de Desconto\033[m')
        print('-=' * 20)
        valor = float(input('Qual o valor:R$'))
        desconto = float(input('Quanto de desconto:'))
        vd = valor - (valor * desconto / 100)
        sleep(3)
        print(f'O valor do produto é R$\033[32m{float(valor):.2f}\033[m, descontando \033[34m{int(desconto)}\033[m% fica R$\033[31m{float(vd):.2f}\033[m')
        resp = ' '
        while resp not in 'SN':
            print('-=' * 20)
            resp = input('Quer continuar [S/N]:').strip().upper()[0]
            print('-=' * 20)
            sleep(2)
        if resp == 'N':
            sleep(2)
            break

#Acréscimo
def Calculo_Acrecimo():
    from time import sleep
    while True:
        print('-=' * 20)
        print('          \033[34:40mCalculo de Acréscimo\033[m')
        print('-=' * 20)
        valor = float(input('Qual o valor:R$'))
        acrescimo = float(input('Quanto será acrescido:'))
        vd = valor + (valor * acrescimo / 100)
        sleep(3)
        print(f'O valor do produto é R$\033[32m{float(valor):.2f}\033[m, com o acréscimo de \033[34m{int(acrescimo)}\033[m% fica R$\033[31m{float(vd):.2f}\033[m')
        resp = ' '
        while resp not in 'SN':
            print('-=' * 20)
            resp = input('Quer continuar [S/N]:').strip().upper()[0]
            print('-=' * 20)
            sleep(2)
        if resp == 'N':
            sleep(2)
            break


#Conversor de Real para Dolar

def Calculo_RealDolar():
    from time import sleep
    while True:
        print('-=' * 20)
        print('          \033[34:40mCalculo de Conversão de Real a Dolar\033[m')
        print('-=' * 20)
        valoreal = float(input('Qual o valor:R$'))
        vcrd = valoreal / 4.66
        sleep(3)
        print(f"O valor R$\033[34m{valoreal}\033[m, convertido em dolar fica $\033[32m{vcrd:.2f'}\033[m")
        resp = ' '
        while resp not in 'SN':
            print('-=' * 20)
            resp = input('Quer continuar [S/N]:').strip().upper()[0]
            print('-=' * 20)
            sleep(2)
        if resp == 'N':
            sleep(2)
            break

#Menu Principal
from time import sleep
while True:
    print('-=' * 20)
    print('           \033[31:40mMenu Principal\033[m')
    print('-=' * 20)

    print("""    1 - Calculadora Básica
    2 - Calcular Desconto
    3 - Calcular Acréscimo
    4 - Calculadora de Conversão de Real para Dolar
    5 - Sair""")
    print('-=' * 20)
    esco = int(input('Qual desejas escolher: '))
    print('-=' * 20)
    if esco == 1:
        calculadora_basica()
    elif esco == 2:
        calcular_desconto()
    elif esco == 3:
        Calculo_Acrecimo()
    elif esco == 4:
        Calculo_RealDolar()
    elif esco == 5:
        print('Saindo...')
        sleep(3)
        break

#Final
print('-=' * 20)
print('Obrigado por nos escolher!')
print('-=' * 20)
