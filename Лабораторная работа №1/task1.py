numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
first_part = sum(numbers[:4])
second_part = sum(numbers[5:])
sum_of_numbers = first_part+second_part
count_of_numbers = len(numbers)
mean_of_numbers = sum_of_numbers/count_of_numbers
switch_point = 4
numbers[switch_point] = mean_of_numbers
print("Измененный список:", numbers)
