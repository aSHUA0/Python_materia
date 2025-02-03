# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
#PRIMEIRA MANEIRA DE ORDENAR LISTA COM DICIONÁRIO
'''def ordena(item):
    return item['nome']

lista.sort(key=ordena)

for item in lista:
    print(item)'''

#USANDO LAMBDA PARA ORDENAR LISTA COM DICIONÁRIO

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

for item in l1:
    print(item)
print()
for item in l2:
    print(item)

#EXECUTANDO FUNÇÕES

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
       return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)            ///a mesma coisa///
duplica = executa(
    lambda m: lambda n: n * m,            ///a mesma coisa///
    2
)

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
    executa(soma(2,3)),
    soma(2,3)
)                                ///TODOS FAZEM A MESMA COISA///

#LAMBDA PODE RECEBER VÁRIOS ARGS

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
