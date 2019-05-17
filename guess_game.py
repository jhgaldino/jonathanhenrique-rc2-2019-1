print("\n**************************")
print("Bem vindo ao jogo de advinhação")
print("*************************\n")


secret_game = 42

guess = input("digite numero")
print("digitou",guess)

if secret_game == int(guess):
    print("Acerto Miseravi!")

else:
    print("Erro")