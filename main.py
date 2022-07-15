from lib import Parse


def main():
    word = input("Введите слово информацию о котором вы хотите получить (с маленькой буквы): ")
    ParseDict = Parse(word)    
    print("Cловарь Даля:")
    print(ParseDict.parse("https://diclist.ru/slovar/dalya"))
    print("Cловарь Ожегова:")
    print(ParseDict.parse("https://diclist.ru/slovar/ozhegova"))
    print("Cловарь Ушакова:")
    print(ParseDict.parse("https://diclist.ru/slovar/ushakova"))
    print("Cловарь Ефремовой:")
    print(ParseDict.parse("https://diclist.ru/slovar/efremovoy"))


if __name__ == '__main__':
    main()
    input()
