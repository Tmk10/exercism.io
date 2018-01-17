def is_armstrong(number):
    number_to_list = list(str(number))
    armstrong_counter = 0
    for temp_number in number_to_list:
        armstrong_counter += int(temp_number) ** len(number_to_list)
    if int(number) != armstrong_counter:
        return False
    else:
        return True


print(is_armstrong(153))