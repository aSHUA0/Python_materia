#Criação de funções

def saudacao():
    print('Seja bem vindo(a)')
    print('É um prazer fazer esse programa')

saudacao()

#Passando parametro para uma função

def salve(nome, curso):
    print(f'Seja bem vindo(a), {nome}')
    print(f'É um prazer fazer esse programa no {curso}')

salve('Guilherme','Python')

#Função com parâmetros default

def salve(nome, curso = 'Python'):
    print(f'Seja bem vindo(a), {nome}')
    print(f'É um prazer fazer esse programa no {curso}')

salve('Guilherme')

#Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(10, 15)

print('O resultado é:', resultado)

#Calculadora

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        print('Sua operação não existe')

num1 = float(input('Primeiro numero: '))
num2 = float(input('Segundo numero: '))
operacao = input('Qual operação: ')
resultado = calculadora(num1, num2, operacao)

print(resultado)