import random


def generate_number():
    return random.randint(1, 100)


def user_guess():
    return int(input("Digite um número entre 1 e 100: "))


def verify_guess(guess, secret_number):

    if guess == secret_number:
        print(f"Parabéns, você ganhou! O número secreto era {secret_number}")
        return True

    elif guess > 100:
        print("Número inválido, por favor escolha um número entre 1 e 100")

    elif guess < secret_number:
        print("Você errou, o número secreto é maior que o número escolhido!")

    else:
        print("Você errou, o número secreto é menor que o número escolhido!")
        return False


def guessing_the_number(secret_number=int):
    secret_number = generate_number()
    while True:
        guess = user_guess()
        if verify_guess(guess, secret_number):
            break


guessing_the_number()
