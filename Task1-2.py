# Запрашиваем у пользователя два числа
print("Введите первое число:")
num1 = float(input()) 

print("Введите второе число:")
num2 = float(input())

# Выполняем арифметические операции
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Проверка деления на ноль
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Ошибка: деление на ноль!"

print("\nРезультаты арифметических операций:")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {diff_result}")
print(f"{num1} * {num2} = {prod_result}")
print(f"{num1} / {num2} = {div_result}")