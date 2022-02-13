from random import randint
from time import sleep

while True:
    # Escolha do Pc.
    pc = randint(0, 5)

    print("\n")
    print("-=-" * 20)
    print("Escolhi um número entre 0 e 5, tente adivinhar! kkk")
    print("-=-" * 20)
    print("Exit = 6")
    print("\n")

    # Sua escolha.
    esc = int(input("Qual número você acha que eu escolhi: "))
    
    
    if esc == pc:
        print("PROCESSANDO...")
        sleep(2)
        print("PARABÉNS!")
        print("Você Acertou.(: ")
        print("-=-" * 20)

    elif esc >= 6:
        print("Saindo!..................................")
        sleep(2)
        break

    else:
        print("PROCESSANDO...")
        sleep(2)
        print("Você ERROu!")
        print("Eu escolhi {} e não {}".format(pc, esc))
        print("-=-" * 20)
