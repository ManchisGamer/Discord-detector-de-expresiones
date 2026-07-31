import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>0123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "SELLO"
    
def dice_roll():
    roll = random.randint(0,5)
    if roll == 0:
        return "Salió 1 En El Dado"
    elif roll == 1:
        return "Salió 2 En El Dado"
    elif roll == 2:
        return "Salió 3 En El Dado"
    elif roll == 3:
        return "Salió 4 En El Dado"
    elif roll == 4:
        return "Salió 5 En El Dado"
    elif roll == 5:
        return "Salió 6 En El Dado"