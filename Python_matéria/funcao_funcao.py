def parametro (numero):
    def multiplicador (multiplica):
        return numero*multiplica
    return multiplicador

num_1 = parametro(int(input('Digite um número: ')))
num_2 = parametro(int(input('Digite outro número: ')))

multiplicador = int(input('Multiplicar por: '))

print(num_1(multiplicador))