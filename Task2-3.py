print("Выберите направление перевода:")
print("1 — Цельсий → Фаренгейт")
print("2 — Фаренгейт → Цельсий")

choice = input("Введите 1 или 2: ")

if choice == "1":
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
elif choice == "2":
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
else:
    print("Ошибка: выберите 1 или 2.")