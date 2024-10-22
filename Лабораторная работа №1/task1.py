numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
end_sly = 4 # номер элемента до пустого значения
beg_sly = 5 # номер индекса после пустого значения
first_part = sum(numbers[:end_sly]) # поэлементное суммирование до пустого значения
second_part = sum(numbers[beg_sly:]) # поэлементное суммирование после пустого значения
sum_of_numbers = first_part+second_part # сумма всех элементов, исключая пустое значение
count_of_numbers = len(numbers) # количество элементов в списке с учетом пустого значения
mean_of_numbers = sum_of_numbers/count_of_numbers # подсчет среднего арифметического
switch_point = 4 # индекс заменяемого элемента
numbers[switch_point] = mean_of_numbers # присваивание элементу значение среднего арифметического
print("Измененный список:", numbers)
