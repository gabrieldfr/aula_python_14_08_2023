def area_triangulo(a, b):
    return a * b/2

altura = float(input('Digite a altura do triângulo: '))
base = float(input('Digite a base do triângulo: '))
print(f'A área do triângulo é: {area_triangulo(altura, base)}')