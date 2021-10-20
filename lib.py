import requests
from bs4 import BeautifulSoup
from transliterate import translit


class ParseDicts:
    def Parse1(word, url):
        # Замена ё на е
        if word[0] == "ё":
            word = word.replace("ё", "е")
        # Траслитерация слова и обозначения его первой буквы на латинице
        match word[0]:
            case "е":
                FirstLetter = "ye"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "ж":
                FirstLetter = "zh"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "й":
                FirstLetter = "iy"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "ч":
                FirstLetter = "ch"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "ш":
                FirstLetter = "sh"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "щ":
                FirstLetter = "sch"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "ъ":
                word = "tverdyi-znak"
                FirstLetter = "tznak"
            case "ы":
                word, FirstLetter = "y"
            case "ь":
                word = "myagkii-znak"
                FirstLetter = "mznak"
            case "ю":
                FirstLetter = "yu"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
            case "я":
                FirstLetter = "ya"
                word = translit(word, 'ru', reversed=True)
                for i in word:
                    if i == "'":
                        word = word.replace(i, "")
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

    def Parse2(word, url):
        # Замена ё на е
        if word[0] == "ё":
            word = word.replace("ё", "е")

        url = f'{url}/{word}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        dic = soup.find_all('div', class_="outtable")
        res = ""

        for gloses in dic:
            res += gloses.table.text

        if res == "":
            return "Информация не найдена"
        else:
            return res

    def Etimology(word):
        for i in word:
            if i == "ё":
                word = word.replace(i, "е")
            if i == "й":
                word = word.replace(i, "и")

        url = f'https://gufo.me/dict/vasmer/{word}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        dic = soup.find_all(id="dictionary-acticle")
        res = ""

        for gloses in dic:
            return gloses.p.text
