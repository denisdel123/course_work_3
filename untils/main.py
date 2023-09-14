import json

if __name__ == '__main__':
    with open('data/operations.json') as file:
        d = json.load(file)
    print(d)