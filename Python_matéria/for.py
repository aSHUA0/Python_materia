"""for i in range(10):
    print(i)"""

"""for i in range(1, 11):
    print(i)"""

"""Primeira casa: Onde começa
Segunda casa: Final
Terceira casa: Quantidade que aumenta"""

"""for i in range(1, 14, 3):
    print(i)"""

contador = 0

for i in range(3):
    nota = float(input(f"Informe a sua nota {i + 1}: "))
    contador = contador + nota

print(contador / 3)