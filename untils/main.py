from pathlib import Path

from untils_2 import get_json_operations, change_format_date, write_in_single_list,\
    get_correct_f, sort_json_operations, clear_correct_f, print_info, change_format_output, add_in_list_date

FILE_URL = Path(__file__).parent.joinpath("operations.json")

file_json = 'data/operations.json'

way_correct_f_json = 'data/correct_f.json'


if __name__ == '__main__':

    all_operations = get_json_operations(file_json)

    for one_operation in all_operations:
        if not one_operation.get('from'):
            continue

        if one_operation['state'] == "EXECUTED":

            change_date = change_format_date(one_operation)

            write_in_single_list(change_date, way_correct_f_json)

    correct_json = get_correct_f(way_correct_f_json)

    date_list = add_in_list_date(correct_json)

    date_list_five = sort_json_operations(date_list)
    print(date_list_five)

    for items in date_list_five:
        for item in correct_json["information"]:
            if item["date"] == items:
                prin = change_format_output(item)
                print_info(prin)

    clear_correct_f(way_correct_f_json)





