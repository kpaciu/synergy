import random


def guess_number():
    secret_number = random.randint(1, 100)  # случайное число от 1 до 100
    attempts = 7  # количество попыток

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У вас есть 7 попыток, чтобы его угадать.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}: Ваше предположение? "))
            if guess < 1 or guess > 100:
                print("Пожалуйста, введите число от 1 до 100.")
                continue

            if guess < secret_number:
                print("Слишком маленькое число!")
            elif guess > secret_number:
                print("Слишком большое число!")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempt} попыток.")
                return
        except ValueError:
            print("Ошибка: Введите целое число.")

    print(f"Вы исчерпали все попытки. Загаданное число было: {secret_number}")


if __name__ == "__main__":
    guess_number()
