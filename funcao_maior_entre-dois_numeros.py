def maior_num():
    num1 = int(input('digite um número: '))
    num2 = int(input('digite outro número: '))
    if num1 > num2:
        return num1
    else:
        return num2
print('O maior número é', maior_num())