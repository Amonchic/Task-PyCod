n = int(input("Введите число n: "))

total_sum = 0

# Перебираем числа от 1 до n
for i in range(1, n + 1):
    factorial = 1  # начинаем с 1
    
    # Вычисляем факториал для текущего i
    for j in range(1, i + 1):
        factorial *= j  # умножаем на j
    
    total_sum += factorial  # добавляем факториал к общей сумме

print(f"Сумма 1! + 2! + ... + {n}! = {total_sum}")