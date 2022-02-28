import random as r

while True:
    if 'x' in input("Roll Dice ( x for eXit) ? : "):
        exit(0)
    print((" ● "*r.randint(1, 6)).center(20))
