def complex_num_sum():
    real1 = int(input('Type the first real number: '))
    j1 = int(input('Typer the first imaginary number: '))
    real2 = int(input('Type the second real number: '))
    j2 = int(input('Type the second imaginary number: '))
    num1 = real1 + real2
    num2 = j1 + j2
    return num1, num2
print(f'The sum of the complex numbers is {complex_num_sum()}')