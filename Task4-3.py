height = int(input("Введите высоту ёлочки: "))
symbol = input("Введите символ для ёлочки: ")

print("\nРисуем ёлочку:\n")

# Рисуем саму ёлочку
for i in range(height):
    # Количество символов в строке: 2*i + 1
    num_symbols = 2 * i + 1
    # Центрируем строку по ширине последней строки
    line = symbol * num_symbols
    print(line.center(2 * height - 1))  # ширина основания ёлочки

# Рисуем ствол
print("||".center(2 * height - 1))
print("||".center(2 * height - 1))