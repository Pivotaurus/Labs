#Задача 1: Записать во второй файл все четные числа, делящиеся на 5, из первого файла.
with open('Старый5.txt', 'r') as source_file:
    with open('Новый5.txt', 'w') as target_file:
        numbers = source_file.read().split()

        filt_num = [num for num in numbers if int(num) % 2 == 0 and int(num) % 5 == 0]

        for num in filt_num:
            target_file.write(num + '\n')

#Задача 2: Преобразовать строку, заменив в ней все символы, следующие за минусами числами «-7».

orig_string = "Пример и -75 и -72 и текст."
result_string = ""
i = 0

while i < len(orig_string):
    if orig_string[i:i+2] == "-7":
        result_string += "-7"
        i += 2
    else:
        result_string += orig_string[i]
        i += 1

print(result_string)

#Задача 3: Найти первый номер точки в данной последовательности

sequence = "abc.def.gh"
f_d_i = sequence.find(".")
if f_d_i != -1:
    print("Первая точка найдена в позиции:", f_d_i)
else:
    print("Точка не найдена в строке.")
