from random import randint
print("")
x = 1
while 1:
    rand = randint(1, 6)
    rand2 = randint(1, 6)
    print(f'tentativa {x} \n'
          f'dado 1 = {rand} e dado 2 = {rand2}')
    if rand == 1:
        if rand2 == 1:
            break
    elif rand == 2:
        if rand2 == 2:
            break
    elif rand == 3:
        if rand2 == 3:
            break
    elif rand == 4:
        if rand2 == 4:
            break
    elif rand == 5:
        if rand2 == 5:
            break
    elif rand == 6:
        if rand2 == 6:
            break
    x = x + 1