def bubble_count(a_list):
    comparisons, exchanges = 0, 0
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            comparisons += 1
            if a_list[i] > a_list[i + 1]:
                exchanges += 1
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return comparisons, exchanges


def insertion_count(a_list):
    comparisons, exchanges = 0, 0
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0:
            comparisons += 1
            if a_list[position - 1] > current_value:
                exchanges += 1
                a_list[position] = a_list[position - 1]
                position = position - 1
            else:
                break

        a_list[position] = current_value

    return comparisons, exchanges