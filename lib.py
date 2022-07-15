import requests
from bs4 import BeautifulSoup
from transliterate import translit


class Parse:
    def __init__(self, word):
        self.word = word

    def wordManage(FirstLetter):
        """Траслитерация слова и обозначения его первой буквы на латинице"""
        FirstLetter = f"{FirstLetter}"
        word = translit(word, 'ru', reversed=True)
        for i in word:
            if i == "'":
                word = word.replace(i, "")

    def parse(url):
        # Замена ё на е
        for i in word:
            if i == "ё":
                word = word.replace(i, "е")
        # Траслитерация слова и обозначения его первой буквы на латинице
        match word[0]:
            case "е":
                Parse.wordManage('ye')
            case "ж":
                Parse.wordManage('zh')
            case "й":
                Parse.wordManage('iy')
            case "ч":
                Parse.wordManage('ch')
            case "ш":
                Parse.wordManage('sh')
            case "щ":
                Parse.wordManage('sch')
            case "ъ":
                word = "tverdyi-znak"
                FirstLetter = "tznak"
            case "ы":
                word, FirstLetter = "y"
            case "ь":
                word = "myagkii-znak"
                FirstLetter = "mznak"
            case "ю":
                Parse.wordManage('yu')
            case "я":
                Parse.wordManage('ya')
            case _:
                word = translit(word, 'ru', reversed=True)
                FirstLetter = str(word[0])
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
        url = f'{url}/{FirstLetter}/{word}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        dic = soup.find_all('div', class_="found_word")
        res = ""

        for gloses in dic:
            res += gloses.p.text

        if res == "":
            return "Информация не найдена"
        else:
            return res