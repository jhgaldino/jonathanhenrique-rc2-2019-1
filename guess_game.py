print("\n**************************")
print("Bem vindo ao jogo de advinhação")
print("*************************\n")


secret_game = 42

guess_str = input("digite numero")
guess = input(guess_str)


correct = guess == secret_game
bigger = guess > secret_game
smaller = guess < secret_game


if correct:
    print("Certa Resposta")

else :
    if bigger:
        print("Erro, o seu numero é maior")
    elif smaller:
        print("Erro, o seu numero é menor")

print("*********FIM DE JOGO***********")