import json

def main():
    with open('mydb', 'w') as myfile:
        data = json.dumps({'users': {}, 'posts': {}})
        myfile.write(data)

    if __name__ == '__main__':
        main()