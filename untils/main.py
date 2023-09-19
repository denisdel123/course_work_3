from untils import get_operation, operation_executed, check_time, enter_info, print_info

file_json = 'data/operations.json'

if __name__ == '__main__':

    operations = get_operation(file_json)

    for_check = operation_executed(operations)

    from_check = check_time(for_check)

    from_enter_info = enter_info(from_check, for_check)

    print_info(from_enter_info)






