print("\n**************************")
print("Bem vindo ao jogo de advinhação")
print("*************************\n")

tries = 3
run = 1
secret_game = 42
for run in range(tries):
    print("\nTentativa{} de {}".format(run+1,tries))
    guess_str = input("Digite numero :")
    guess = int(guess_str)

    correct = guess == secret_game
    bigger = guess > secret_game
    smaller = guess < secret_game

    if correct:
        print("Certa Resposta")
    else:
        if bigger:
            print("Erro, o seu numero é maior")
        elif smaller:
            print("Erro, o seu numero é menor")

    run += 1
    tries -= 1


print("*********FIM DE JOGO***********")