def find_common_participants(set_one, set_two, sep=','):
    first_list = set_one.split(sep)
    second_list = set_two.split(sep)

    sum_list = list(set(first_list).intersection(second_list))
    sum_list.sort()

    return sum_list

    participants_first_group = "Иванов|Петров|Сидоров"
    participants_second_group = "Петров|Сидоров|Смирнов"

    participants = find_common_participants(participants_first_group, participants_second_group)
    print("Общие участники:", participants)
