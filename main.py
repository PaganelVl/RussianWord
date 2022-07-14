from lib import Parse


def main():
    wordi = input("Введите слово информацию о котором вы хотите получить (с маленькой буквы): ")
    print("Cловарь Даля:")
    print(Parse.parse(wordi, "https://diclist.ru/slovar/dalya"))
    print("Cловарь Ожегова:")
    print(Parse.parse(wordi, "https://diclist.ru/slovar/ozhegova"))
    print("Cловарь Ушакова:")
    print(Parse.parse(wordi, "https://diclist.ru/slovar/ushakova"))
    print("Cловарь Ефремовой:")
    print(Parse.parse(wordi, "https://diclist.ru/slovar/efremovoy"))


if __name__ == '__main__':
    main()
    input()
