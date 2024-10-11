import math

def get_positive_integer():
    while True:
        try:
            num = int(input("Введите положительное целое число: "))
            if num < 0:
                raise ValueError("Число должно быть положительным!")
            return num
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

def calculate_factorial(num):
    return math.factorial(num)

if __name__ == "__main__":
    number = get_positive_integer()
    result = calculate_factorial(number)
    print(f"Факториал числа {number} равен {result}.")
