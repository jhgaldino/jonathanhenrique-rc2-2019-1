import random


def play():

    print("\n**************************")
    print("Bem vindo ao jogo de advinhação")
    print("♫Musica de programa♫")
    print("*************************\n")

    secret_game = int(random.randrange(1,100))
    points = 1000

    while 1:
        print("Defina o nivel")
        level = int(input("(1)facil (2)medio (3)dificil\n"))

        if level == 1:
            tries = 20
            break
        elif level == 2:
            tries = 10
            break
        elif level == 3:
            tries = 5
        else:
            continue

    for run in range(tries):
        print("\nTentativa{} de {}".format(run+1,tries))
        guess_str = input("Qual seu chute?(Entre 1 e 100)Digite numero :")
        guess = int(guess_str)

        correct = guess == secret_game
        bigger = guess > secret_game
        smaller = guess < secret_game

        if guess < 1 or guess > 100 :
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        if correct:
            print("Certa Resposta!♫ pan pan pan pan pan pan♫")
            break
        else:
            if bigger:
                print("Erro, o seu numero é maior")
            elif smaller:
                print("Erro, o seu numero é menor")

            points -= abs(secret_game - guess)

    print(f"pontuação: {points}")
    print("*********FIM DE JOGO***********")


if __name__ == "__main__":
    play()
