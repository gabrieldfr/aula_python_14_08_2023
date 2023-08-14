def menor_num():
    num1 = int(input('digite um número: '))
    num2 = int(input('digite outro número: '))
    if num1 < num2:
        return num1
    else:
        return num2
print('o menor número é', menor_num())