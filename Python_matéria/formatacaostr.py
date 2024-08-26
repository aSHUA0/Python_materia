#formatação de STR
nome = 'Guilherme Silva Tavares'
altura = 1.85
peso = 70
imc = peso / (altura ** 2)

print(nome, 'tem', altura, 'de altura')

#f-strings
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é: {imc:.2f}'
print(linha_1)
print(linha_2)

#formato
a = 'A'
b = 'B'
c = 1.1
string = 'a = {1} b = {0} c = {2:.2f}'
formato = string.format(a, b, c)

print(formato)