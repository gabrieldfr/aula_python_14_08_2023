def bhaskara():
    a = int(input('Type the a argument: '))
    b = int(input('Type the b argument: '))
    c = int(input('Type the c argument: '))
    delta = b**2 - 4* a*c
    if delta >= 0:
        raiz1 = -b + delta**0.5/2*a
        raiz2 = -b - delta**0.5/2*a
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b/(2*a)
        return raiz, raiz
    
print(bhaskara())