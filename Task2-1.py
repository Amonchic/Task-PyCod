# Получаем номер месяца от пользователя
month = int(input("Введите номер месяца (от 1 до 12): "))

# Проверяем, валидный ли номер
if month < 1 or month > 12:
    print("Ошибка: номер месяца должен быть от 1 до 12!")
else:
    
    if month in [12, 1, 2]:
        season = "зима"
    elif month in [3, 4, 5]:
        season = "весна"
    elif month in [6, 7, 8]:
        season = "лето"
    else:  # month in [9, 10, 11]
        season = "осень"

    print(f"Месяц {month} — это {season}.")