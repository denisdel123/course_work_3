from untils import get_operation, operation_executed


file_json = 'data/operations.json'


if __name__ == '__main__':
    operations = get_operation(file_json)
    operation_executed(operations)



