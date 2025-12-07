import math

def area_rectangle(width, height):
    """Возвращает площадь прямоугольника."""
    return width * height

def area_circle(radius):
    """Возвращает площадь круга."""
    return math.pi * radius ** 2

def area_triangle(base, height):
    """Возвращает площадь треугольника."""
    return (base * height) / 2


# Меню выбора фигуры
print("Выберите фигуру для расчёта площади:")
print("1 — Прямоугольник")
print("2 — Круг")
print("3 — Треугольник")

choice = input("Введите номер (1, 2 или 3): ")

if choice == "1":
    w = float(input("Введите ширину прямоугольника: "))
    h = float(input("Введите высоту прямоугольника: "))
    result = area_rectangle(w, h)
    print(f"Площадь прямоугольника: {result:.2f}")

elif choice == "2":
    r = float(input("Введите радиус круга: "))
    result = area_circle(r)
    print(f"Площадь круга: {result:.2f}")

elif choice == "3":
    b = float(input("Введите основание треугольника: "))
    h = float(input("Введите высоту треугольника: "))
    result = area_triangle(b, h)
    print(f"Площадь треугольника: {result:.2f}")

else:
    print("Ошибка: выберите 1, 2 или 3.")