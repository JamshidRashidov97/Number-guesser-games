import random


def sontop(x=10):
    son = random.randint(1,x)
    print(f"Men 1 dan 10 gacha son o'yladim. Topa olasizmi?")
    attempts = 0
    while True:
        attempts += 1
        guess = int(input(">>>"))
        if guess < son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif guess > son:
            print("Xato, men o'ylagan son bundan kamroq. Yana harakat qiling:")
        else:
            break
    print(f"Tabriklaymiz. {attempts} ta taxmin bilan topdingiz!") 
    
    return attempts

    
    
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.")
    quyi = 1
    yuqori = x
    attempts = 0
    while True:
        attempts += 1
        if quyi != yuqori:
            guess = random.randint(quyi, yuqori)
        else:
            guess = quyi
        javob = input(f"Siz {guess} sonini o'yladingiz: tog'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = guess - 1
        elif javob == "+":
            quyi = guess + 1
        else:
            break
    print(f"Men {attempts} ta taxmin bilan topdim!")
    
    return attempts

def play(x=10):
    yana = True
    while yana:
        guess_user = sontop(x)
        guess_pc = sontop_pc(x)
        
        if guess_user>guess_pc:
            print("Men yutdim")
        elif guess_user<guess_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
        
      