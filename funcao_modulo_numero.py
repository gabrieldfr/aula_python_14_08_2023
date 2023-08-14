import math
def modulo(x):
    result = math.sqrt(x**2)**1/2
    return result
num = int(input('Digite um número: '))
print(f'O módulo de {num} é {modulo(num)}')
