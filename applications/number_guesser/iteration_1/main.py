from random import randrange


def success():
    print("You nailed it!")


def fail():
    print("You're a loser!")


def main() -> None:
    secret_number = randrange(1, 11)
    user_guess = int(input("Enter you guess: "))
    if secret_number == user_guess:
        success()
    else:
        fail()


if __name__ == "__main__":
    main()
