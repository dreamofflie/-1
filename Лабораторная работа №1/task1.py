numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers[4] = 0
sum_of_numbers = sum(numbers)
count_of_numbers = len(numbers)
mean_of_numbers = sum_of_numbers/count_of_numbers
numbers[4] = mean_of_numbers
# TODO заменить значение пропущенного элемента средним арифметическим


print("Измененный список:", numbers)
