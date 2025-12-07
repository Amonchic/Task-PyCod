import random

# Загадываем число
secret_number = random.randint(1, 10)
print("Я загадал число от 1 до 10. У тебя 3 попытки!")

# Цикл на 3 попытки
for attempt in range(1, 4):  # попытки: 1, 2, 3
    guess = int(input(f"Попытка {attempt}: введи число: "))

    if guess == secret_number:
        print(f" Поздравляю! Ты угадал с {attempt}-й попытки!")
        break  # выходим из цикла, если угадали
    elif guess < secret_number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")

    # Если это последняя попытка и не угадали
    if attempt == 3:
        print(f" Ты не угадал. Загаданное число было: {secret_number}")