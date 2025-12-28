def mod(a, b):
    if a < b:
        return a 
    return mod(a - b, b)

a = int(input("Введите a: "))
b = int(input("Введите b: "))

print("Остаток:", mod(a, b))
