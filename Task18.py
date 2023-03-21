n = int(input("Введите количество элементов в массиве: "))
mass = []
for elem in range(1, n + 1):
    mass.append(elem)
print(mass)
num = int(input("Введите число в массиве: "))
if num in mass:
    print(num)
elif mass[-1] < num:
    print(mass[-1])
elif mass[0] > num:
    print(mass[0])
else:
    print("Ввели что-то не то!")