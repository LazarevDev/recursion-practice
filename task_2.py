def print_odd(pos=1):
    n = int(input("Введите число (0 для конца): "))
    if n == 0:
        return
    if pos % 2 == 1:
        print(f"Число на позиции {pos}: {n}")
    print_odd(pos + 1)

print_odd()
