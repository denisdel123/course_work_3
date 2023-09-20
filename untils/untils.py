import json
import re

from datetime import datetime


def get_operation(info):
    """получаю json и преобразую в python формат"""
    with open(info, 'r', encoding='utf-8') as file:
        operations = json.load(file)

    return operations


def operation_executed(operations):
    """сортерую по ключевому слову EXECUTED и так же делаю проверку from и записываю в новый список"""
    operation = []

    for oper in operations:
        if not oper.get('from'):
            continue

        if oper['state'] == 'EXECUTED':
            date = datetime.strptime(oper['date'], '%Y-%m-%dT%H:%M:%S.%f')
            date = date.strftime('%d, %m, %Y, %H, %M, %S')
            operation.append({
                "id": oper['id'],
                "state": oper['state'],
                "date": date.split(', '),
                "operationAmount": {
                    "amount": oper["operationAmount"]['amount'],
                    "currency": {
                        "name": oper["operationAmount"]['currency']['name'],
                        "code": oper["operationAmount"]['currency']['code']
                    }
                },
                "description": oper['description'],
                "from": oper['from'],
                "to": oper['to']
            })

    return operation


def check_time(oper):
    """сортерую дату от самой ранней до самой поздней"""
    list_date = []
    operr = oper

    for time in operr:
        test = time['date']

        t1 = datetime(int(test[2]), int(test[1]), int(test[0]), int(test[3]), int(test[4]), int(test[5]))

        list_date.append(t1)

    return sorted(list_date)


def enter_info(time, oper):
    """ищу в json первые 5 дат которые добавил в массив и выписываю весь словарь в список"""
    operation_list = []
    cont = 0

    for i in range(0, 5):

        for times in oper:
            test = times['date']

            t1 = datetime(int(test[2]), int(test[1]), int(test[0]), int(test[3]), int(test[4]), int(test[5]))

            if time[i] == t1:
                operation_list.append(times)

    return operation_list


def print_info(result):
    """преобразую информацию в нужный формат и вывоже пользователю"""

    for info in result:

        date = f"{info['date'][0]}.{info['date'][1]}.{info['date'][2]}"
        transfer = info["description"]

        visa = info['from'].split(' ')
        vis = [''.join(visa[-1][::-1][i:i + 4])[::-1] for i in range(0, len(visa[-1]), 4)]
        vis[-2] = f"{''.join(vis[-1])[:2]}**"
        vis[-3] = "****"
        visa_ans = ' '.join(visa[:-1])

        next = info['to'].split(' ')
        nex = [''.join(next[-1][::-1][i:i + 4])[::-1] for i in range(0, len(next[-1]), 4)]

        amont = info['operationAmount']['amount']
        name = info['operationAmount']['currency']['name']

        print(f"{date} {transfer}\n{visa_ans} {' '.join(vis[::-1])} -> **{''.join(nex[-1])}\n{amont} {name}\n")
