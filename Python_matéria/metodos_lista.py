#Metodos

lista = [10, 50, 30, 40, 25, 60, 5]

# append
"""Adcionando elemento na lista (final)"""

print(lista)

lista.append(3)

print(lista)

#insert
"""Escolhe a posição"""

lista.insert(1, 11)

print(lista)

#extend
"""Unir duas listas existentes"""
lista2 = [9, 60, 90]

lista.extend(lista2)

print(lista)

#pop
"""Remover a posição que especificar"""
lista.pop(0)
lista.pop()

print(lista)

#remove
"""Remover o elemento especifico"""
lista.remove(25)

print(lista)

#cout
"""Conta quantas vezes um elemento repete"""

print('O numero 60 se repete:' ,lista.count(60))

#index
"""Mostra o indece(local) de um determinado elemento"""

print('O indice do numero 50 é:' ,lista.index(50))

#sort
"""Ordena os elementos da lista"""
lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

#Funções para listas

#len
"""Ver quantos elementos tem na lista"""
print(len(lista))

#sum
"""Soma todos os elementos da lista"""
print(sum(lista))

#max
"""Mostra o maior elemento da lista"""
print(max(lista))

#min
"""Mostra o menor elemento da lista"""
print(min(lista))