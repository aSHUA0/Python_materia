#Criação de dicionario

dicionario = {}
dicionario = dict

dicionario = {'nome': 'Guilherme', 'idade': 19, 'altura': 1.85}

print(dicionario)
print(dicionario['nome'])

#Adicionar elemento no dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 1.90

print(dicionario)

#Pecorrer os elementos do dicionario

for i in dicionario:
    print(i, dicionario[i])

#Testando se existe uma chave

print('peso' in dicionario)
print('altura' in dicionario)

# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')