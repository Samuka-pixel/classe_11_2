from random import randint
rand = randint(0,5)
esc = int(input("Escolha um numero de 0 a 5 "))
if esc == rand:
    print("parabens!")
else:
    print("erraste")