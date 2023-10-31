#Задача 1: Вывести все четные элементы массива, делящиеся на 4, введенного вручную из n элементов.

n = int(input("Введите количество элементов в массиве: "))
arr = []

for _ in range(n):
    element = int(input("Введите элемент: "))
    arr.append(element)

result = [x for x in arr if x % 2 == 0 and x % 4 == 0]

print("Четные элементы, делящиеся на 4:", result)

#Задача 2: Разделить список на k частей и отсортировать каждую часть. Вывести результат.

n = int(input("Введите количество элементов в списке: "))
k = int(input("Введите количество частей (k < 4): "))
arr = []

for _ in range(n):
    element = int(input("Введите элемент: "))
    arr.append(element)

# Разделим список на k частей
chunk_size = n // k
chunks = [arr[i:i + chunk_size] for i in range(0, n, chunk_size)]

# Отсортируем каждую часть
sorted_chunks = [sorted(chunk) for chunk in chunks]

# Выведем результат
for i, chunk in enumerate(sorted_chunks):
    print(f"Часть {i + 1}: {chunk}")

#Задача 3: Получить две последовательности - квадраты и кубы элементов.

n = int(input("Введите количество элементов в последовательности: "))
sequence = []

for _ in range(n):
    element = int(input("Введите элемент: "))
    sequence.append(element)

squares = [x**2 for x in sequence]
cubes = [x**3 for x in sequence if x % 2 != 0]

print("Квадраты элементов:", squares)
print("Кубы нечетных элементов:", cubes)

#Задача 4: Получить n*m, где m-тая строка есть m-тая степень соответствующего элемента ai, m=1, …, 5.

n = int(input("Введите количество элементов в последовательности: "))
sequence = []

for _ in range(n):
    element = float(input("Введите элемент: "))
    sequence.append(element)

m = 5  # Количество степеней

result = [[element**m for element in sequence] for m in range(1, m + 1)]

for row in result:
    print(row)

#Задача 5: Разбить матрицу на равные части по вертикали.

# Исходная матрица
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Разделение матрицы на части
num_parts = 2  # Количество частей
part_size = len(matrix) // num_parts  # Размер каждой части

parts = [matrix[i:i + part_size] for i in range(0, len(matrix), part_size)]

for part in parts:
    print(part)
