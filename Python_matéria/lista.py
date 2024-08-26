notas = [8, 9, 7.8]

#Lista vazia
"""lista = []
lista = list()"""

#Listas diferentes

lista = [19, 'Guilherme', 3.14, True]

for i in range(4):
    print(lista[i])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[0:6:2])
print(lista[0::2])

#Interação com FOR

for i in lista:
    print(i)

print('Comprimento da lista:', len(lista))