# Задача №22

n = int(input('Введите размер первого множества: '))
m = int(input('Введите размер второго множества: '))

result_1 = set()

for i in range(n):
    num = int(input("Введите числа: "))
    result_1.add(num)

result_2 = set()

for i in range(m):
    num2 = int(input("Введите числа: "))
    result_2.add(num2)

result_3 = set.union(result_1, result_2)

print(sorted(result_3))
