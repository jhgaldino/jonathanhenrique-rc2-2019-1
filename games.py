import guess_game
import hangman_game


def choose_game():
    print("\n**************************")
    print("Bem vindo ao poli games")
    print("♫Musica de programa♫")
    print("*************************\n")

    while 1:
        game = int(input("(1)forca (2)advinhação\n"))

        if game == 1:
            print("Vamos jogar forca...\n")
            hangman_game.play()
            break
        elif game == 2:
            print("Vamos jogar advinhação...\n")
            guess_game.play()
            break
        else:
            print("Digita direito caralho\n")
            continue


if __name__ == "__main__":
    choose_game()
