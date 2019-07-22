def main():
    my_list = user_input()
    sorted_list = bubble_sort(my_list)
    count_string(sorted_list)


def user_input():
    user_list = []
    user_string = input('Enter data to be sorted: ')
    for item in user_string:
        user_list.append(item)
    print('Original Unsorted Data: ', end='')
    for item in range(len(user_list)):
        print(user_list[item], end='')
    print()
    return user_list


def bubble_sort(my_list):
    ascending_list = my_list

    while ' ' in ascending_list:
        ascending_list.remove(' ')
        for x in range(0, len(ascending_list)):
            for y in range(0, len(ascending_list) - 1):
                if ascending_list[y] > ascending_list[y + 1]:
                    temp = ascending_list[y]
                    ascending_list[y] = ascending_list[y + 1]
                    ascending_list[y + 1] = temp

    print('Sorted List (Ascending Order): ', end='')
    for item in range(len(ascending_list)):
        print(ascending_list[item], end='')
    print()

    descending_list = ascending_list

    for x in range(0, len(descending_list)):
        for y in range(0, len(descending_list) - 1):
            if descending_list[y] < descending_list[y + 1]:
                temp = descending_list[y]
                descending_list[y] = descending_list[y + 1]
                descending_list[y + 1] = temp

    print('Sorted List (Descending Order): ', end='')
    for item in range(len(descending_list)):
        print(descending_list[item], end='')
    print()
    print('Largest:', descending_list[0])
    print('Smallest:', descending_list[-1])

    return ascending_list


def count_string(working_list):
    holding_list = []
    for index in range(len(working_list)):
        item_count = working_list.count(working_list[index])
        if working_list.count(working_list[index]) > 1:
            holding_list.append(working_list[index] + ' ' + str(item_count))
    set_list = set(holding_list)
    final_list = list(set_list)
    for x in range(0, len(final_list)):
        for y in range(0, len(final_list) - 1):
            if final_list[y] > final_list[y + 1]:
                temp = final_list[y]
                final_list[y] = final_list[y + 1]
                final_list[y + 1] = temp
    if len(final_list) >= 1:
        print('FREQUENCY')
        for item in final_list:
            print(item)
    else:
        print()
        print('There are no characters in the data that appears more than once.')


main()
