n = int(input("Введите количество элементов в массиве: "))
mass = []
for elem in range(1, n + 1):
    mass.append(elem)
print(mass)
num = int(input("Введите число в массиве: "))
for i in mass:
    count = 0
    if num in mass:
        count += 1
print(count)