from lib import ParseDicts


def main():
    wordi = input("Введите слово информацию о котором вы хотите получить: ")
    print("Cловарь Даля:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/dalya"))
    print("Cловарь Ожегова:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/ozhegova"))
    print("Cловарь Ушакова:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/ushakova"))
    print("Cловарь Ефремовой:")
    print(ParseDicts.Parse1(wordi, "https://diclist.ru/slovar/efremovoy"))
    print("Синонимы:")
    print(ParseDicts.Parse2(wordi, "https://sinonim.org/s"))
    print("Антонимы:")
    print(ParseDicts.Parse2(wordi, "https://sinonim.org/a"))
    print("Этимология:")
    print(ParseDicts.Etimology(wordi))


if __name__ == '__main__':
    main()
    input()
