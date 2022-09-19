from random import randrange


def success():
    print("You nailed it!")


def fail():
    print("You're a loser!")


def loop_condition():
    return True


def main() -> None:
    secret_number = randrange(1, 11)

    while loop_condition():
        user_guess = int(input("Enter your guess: "))
        if secret_number == user_guess:
            success()
            break
        else:
            fail()


if __name__ == "__main__":
    main()
