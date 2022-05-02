import os
import sys
import shutil

bill_sum = 0
history = []

def playAsk(mult, dict):
    points = 0
    for k, v in dict.items():
        answer = input(k)
        if answer == v:
            print("Правильный ответ")
            points=points+mult
    return points


def buy(bill_sum):
    cost = int(input('Введите сумму покупки'))
    if cost > bill_sum:
        print('Недостаточно средств')
    else:
        bill_sum -= cost
        name = input('Введит название покупки')
        history.append((name, cost))
    return bill_sum


def playBank(bill_sum):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {bill_sum}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            cost = int(input('Введите сумму'))
            bill_sum += cost
        elif choice == '2':
            cost = int(input('Введите сумму покупки'))
            if cost > bill_sum:
                print('Недостаточно средств')
            else:
                bill_sum -= cost
                name = input('Введит название покупки')
                history.append((name, cost))
        elif choice == '3':
            print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


def menu_ask(choice):
    if choice == '1':
        dirName = input('Напишите название новой папки:\n')
        if os.path.isdir(dirName):
            print("Папка уже существует")
        else:
            os.mkdir(dirName)
        print("Папка создана")
    elif choice == '2':
        dirName = input('Напишите название папки/файла для удаления:\n')
        if os.path.isdir(dirName):
            os.rmdir(dirName)
            print("Папка удалена")
        elif os.path.isfile(dirName):
            os.remove(dirName)
            print("Файл удалён")
        else:
            print("Папка/файла не существует")
    elif choice == '3':
        dirName = input('Напишите название папки/файла для копирования:\n')
        if not os.path.exists('copyed_files_dirs'):
            os.mkdir('copyed_files_dirs')
        if os.path.exists(dirName):
            if os.path.exists('copyed_files_dirs/' + dirName):
                print("Копия файла уже существует в папке copyed_files_dirs")
            else:
                shutil.copy(os.path.join('.',dirName),os.path.join('copyed_files_dirs', dirName))
                print("Файл скопирован")
        else:
            print("Файла не существует")
    elif choice == '4':
        rez = sorted(os.listdir('.'))
        for n, item in enumerate(rez):
            print(n + 1, item)
    elif choice == '5':
        print("Список папок:")
        with os.scandir('.') as it:
            for entry in it:
                if not entry.is_file():
                    print('> ' + entry.name)
    elif choice == '6':
        print("Список файлов:")
        with os.scandir('.') as it:
            for entry in it:
                if entry.is_file():
                    print('- ' + entry.name)
    elif choice == '7':
        print(sys.platform)
        print(sys.version)
    elif choice == '8':
        print("Создатель программы: KAPTOWE4KA")
    elif choice == '9':
        asks = {"На каком языке написана данная программа? ": "Python", "2 + 2 = ": "4",
                "Сколько создателю данной программы лет(на момент её создания)? ": "23"}
        print("Викторина пройдена. Получено "+ str(playAsk(1, asks)) + " очка(ов)")
    elif choice == '10':
        playBank(bill_sum)
    elif choice == '11':
        print("Текущая директория:")
        print(os.getcwd())
        newDir = input("Введите название директории: ")
        try:
            os.chdir(newDir)
        except BaseException as err:
            print(f"Ошибка {err=}, {type(err)=}")
    elif choice == '0':
        return 0
    else:
        print('Неверный пункт меню')
    print("Нажмите для любую кнопку прододжения")
    input()


def __main__():
    while True:
        # os.system("cls")
        print('1- создать папку;')
        print('2- удалить(файл / папку);')
        print('3- копировать(файл / папку);')
        print('4- просмотр содержимого рабочей директории;')
        print('5- посмотреть только папки;')
        print('6- посмотреть только файлы;')
        print('7- просмотр информации об операционной системе;')
        print('8- создатель программы;')
        print('9- играть в викторину;')
        print('10-мой банковский счет;')
        print('11-смена рабочей директории;')
        print('0- выход.')
        choice = input('Выберите пункт меню:\n')
        if menu_ask(choice) == 0:
            break


__main__()
