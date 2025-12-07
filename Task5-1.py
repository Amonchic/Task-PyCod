def sum_until_minus_one():
    """Считает сумму чисел, вводимых пользователем, до тех пор, пока не будет введено -1."""
    print("Введите числа. Введите -1, чтобы остановиться.")
    
    total = 0

    while True:
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Ошибка: введите целое число!")
            continue  # пропускаем итерацию, если ошибка
        
        if num == -1:
            break  # выходим из цикла
        
        total += num

    return total  # возвращаем сумму


# Используем функцию
result = sum_until_minus_one()
print(f"Сумма введённых чисел (без -1): {result}")