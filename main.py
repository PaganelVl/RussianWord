from lib import Parse


def main():
    word = input("Введите слово информацию о котором вы хотите получить (с маленькой буквы): ")
    parse_dict = Parse(word)
    print("Cловарь Даля:")
    print(parse_dict.parse("https://diclist.ru/slovar/dalya"))
    print("Cловарь Ожегова:")
    print(parse_dict.parse("https://diclist.ru/slovar/ozhegova"))
    print("Cловарь Ушакова:")
    print(parse_dict.parse("https://diclist.ru/slovar/ushakova"))
    print("Cловарь Ефремовой:")
    print(parse_dict.parse("https://diclist.ru/slovar/efremovoy"))
    print("ЭСБЕ:")
    print(parse_dict.parse("https://diclist.ru/slovar/brokgauza-efrona"))


if __name__ == '__main__':
    main()
    input()
