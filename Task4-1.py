# Получаем два числа
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Определяем направление и выводим числа
if A < B:
    print(f"Числа от {A} до {B} в порядке возрастания:")
    for num in range(A, B + 1):  # B+1 — чтобы включить B
        print(num, end=" ")
elif A > B:
    print(f"Числа от {A} до {B} в порядке убывания:")
    for num in range(A, B - 1, -1):  # B-1 — чтобы включить B, шаг -1
        print(num, end=" ")
else:
    print(f"A и B равны: {A}")

print() 