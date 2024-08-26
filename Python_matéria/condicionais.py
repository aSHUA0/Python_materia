""""idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Tu pode ser preso")

else:
    print("Tu não pode ser preso")"""""

#Calculo média
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
presença = 100

media = (nota1 + nota2) / 2

if media >= 6 and presença >= 70:
    print('Aprovado')
elif media >= 4:
    print('Recuperação')
else:
    print('Reprovado')