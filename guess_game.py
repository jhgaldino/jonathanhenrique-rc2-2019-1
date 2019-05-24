from typing import Any, Union
import random
from random import randrange

print("\n**************************")
print("Bem vindo ao jogo de advinhação")
print("*************************\n")

secret_game = int(random.randrange(1,100))
tries = 3

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
        print("Certa Resposta! pan pan pan pan pan pan")
        break
    else:
        if bigger:
            print("Erro, o seu numero é maior")
        elif smaller:
            print("Erro, o seu numero é menor")

    run += 1
    tries -= 1


print("*********FIM DE JOGO***********")