from datetime import datetime
import json


def get_json_operations(way_json):
    with open(way_json, 'r', encoding='utf-8') as file:
        operations_json = json.load(file)
    return operations_json


def change_format_date(corrected_state):
    date_str = corrected_state['date']
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    correct_date = date_obj.strftime("%d. %m. %Y")
    corrected_state['date'] = correct_date
    return corrected_state


def write_in_single_list(great_json, way_correct_f_json):
    with open(way_correct_f_json, encoding='utf8') as f:
        data_json = json.load(f)

        add_in_json = {
            "date": great_json["date"],
            "amount": great_json["operationAmount"]["amount"],
            "name": great_json["operationAmount"]["currency"]["name"],
            "description": great_json["description"],
            "from": great_json["from"],
            "to": great_json["to"]
        }
        data_json["information"].append(add_in_json)

        with open(way_correct_f_json, 'w', encoding='utf-8') as file:
            json.dump(data_json, file, ensure_ascii=False, indent=4)


def get_correct_f(way_correct_f_json):
    with open(way_correct_f_json, 'r', encoding='utf-8') as file:
        great_json_operations = json.load(file)
        return great_json_operations


def sort_json_operations(list_json_correct_operations):
    items = list_json_correct_operations["information"]
    print(items)
    res = sorted(items, key=lambda user: user["date"])
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return res


def change_format_output(correct_sort_json):
    output = ''
    info = correct_sort_json
    date = info["date"]
    transfer = info["description"]

    visa = info['from'].split(' ')
    vis = [''.join(visa[-1][::-1][i:i + 4])[::-1] for i in range(0, len(visa[-1]), 4)]
    vis[-2] = f"{''.join(vis[-1])[:2]}**"
    vis[-3] = "****"
    visa_ans = ' '.join(visa[:-1])

    next = info['to'].split(' ')
    nex = [''.join(next[-1][::-1][i:i + 4])[::-1] for i in range(0, len(next[-1]), 4)]

    amont = info['amount']
    name = info['name']

    output = f"{date} {transfer}\n{visa_ans} {' '.join(vis[::-1])} -> **{''.join(nex[-1])}\n{amont} {name}\n"

    return output


def print_info(info):
    print(info)


def clear_correct_f(way_correct_f):
    with open(way_correct_f, 'w', encoding='utf-8') as file:
        clear_json = {"information": []}
        json.dump(clear_json, file, ensure_ascii=False, indent=4)
