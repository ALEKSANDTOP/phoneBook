from csv import DictReader, DictWriter
from os.path import exists


def get_data():
    first_name = 'Иван'
    last_name = 'Иванов'
    phone = '+79641232323'
    return [first_name, last_name,phone]


def create_file(file_name):
    with open(file_name, 'w', encoding= 'utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(file_name):
     with open(file_name, 'r', encoding= 'utf-8') as data:
         f_r = DictReader(data)
         return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1],  'Телефон': lst[2]}
    res.append(obj)
    standard_write(file_name, res)


def row_search(file_name):
    last_name = input('Введите фамилию: ')
    res = read_file(file_name)
    for row in res:
        if last_name == row['Фамилия']:
            return row
        return 'запись не найдена.'


def delete_row(file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    res.pop(row_number-1)
    standard_write(file_name, res)


def standard_write(file_name, res):                                   #
    with open(file_name, 'w', encoding= 'utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def change_row(file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    data = get_data()
    res[row_number-1]['Имя'] = data[0]
    res[row_number-1]['Фамилия'] = data[1]
    res[row_number-1]['Телефон'] = data[2]
    standard_write(file_name, res)



def copy_file(file_name, file_name2):
    row_number = int(input("Введите номер строки: "))
    res1 = read_file(file_name)
    res2 = read_file(file_name2)
    res2.append(res1[row_number - 1])
    standard_write(file_name2, res2)




file_name = 'phone.csv'
file_name2 = 'phone2.csv'

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_data())
        elif command == 'r':
            if not exists(file_name):
                print('Файл не существует, создайте его.')
                continue
            print(read_file(file_name))
        elif command == 'f':
            if not exists(file_name):
                print('Файл не существует, создайте его.')
                continue
            print(row_search(file_name)) 
        elif command == 'd':
            if not exists(file_name):
                print('Файл не существует, создайте его.')
                continue
            delete_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('Файл не существует, создайте его.')
                continue
            change_row(file_name)
        elif command == "p":
            if not exists (file_name2):
                create_file(file_name2)
            copy_file(file_name, file_name2)


main()