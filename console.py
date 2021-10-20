from lib import ParseDicts


def main():
    wordi = input("Введите слово информацию о котором вы хотите получить (с маленькой буквы): ")
    print("Cловарь Даля:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/dalya"))
    print("Cловарь Ожегова:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/ozhegova"))
    print("Cловарь Ушакова:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/ushakova"))
    print("Cловарь Ефремовой:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/efremovoy"))


if __name__ == '__main__':
    main()
    input()
