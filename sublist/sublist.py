SUBLIST = "Sublist"
SUPERLIST = "Superlist"
EQUAL = "Equal"
UNEQUAL = "Unequal"
def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    first_list = "".join([str(x) + ":" for x in first_list])
    second_list = "".join([str(x) + ":" for x in second_list])
    # ":" for distinct list elements in string
    if first_list in second_list:
        return SUBLIST
    if second_list in first_list:
        return SUPERLIST
    else:
        return UNEQUAL





