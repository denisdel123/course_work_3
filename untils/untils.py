import json
from datetime import datetime


def get_operation(info):
    with open(info, 'r', encoding='utf-8') as file:
        operations = json.load(file)

    return operations


def operation_executed(operations):
    operation = []

    for oper in operations:
        if not (oper.get('from') and oper.get('state')):
            continue

        if oper['state'] == 'EXECUTED':
            date = datetime.strptime(oper['date'], '%Y-%m-%dT%H:%M:%S.%f')
            date = date.strftime('%d.%m.%Y %H:%M:%S')
            operation.append({
                "id": oper['id'],
                "state": oper['state'],
                "date": date,
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
    print(operation)
