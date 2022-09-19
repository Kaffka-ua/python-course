from random import randrange

MAX_AMOUNT_OF_GUESSES = 3


def success():
    print("You nailed it!")


def fail():
    print("You're a loser!")


def game_over():
    print("Game Over!")


def main() -> None:
    secret_number = randrange(1, 11)
    for _ in range(MAX_AMOUNT_OF_GUESSES):
        user_guess = int(input("Enter your guess: "))
        if secret_number == user_guess:
            success()
            break
        else:
            fail()
    else:
        game_over()


if __name__ == "__main__":
    main()
