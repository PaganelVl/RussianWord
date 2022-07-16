import requests
from bs4 import BeautifulSoup
from transliterate import translit


class Parse:
    def word_manage(self, fl):
        """

        Траслитерация слова
         и обозначения его первой буквы на латинице

        """
        self.FirstLetter = fl
        self.word = translit(self.word, 'ru', reversed=True)
        for i in self.word:
            if i == "'":
                self.word = self.word.replace(i, "")

    def parse(self, url):
        # Замена ё на е
        for i in self.word:
            if i == "ё":
                self.word = self.word.replace(i, "е")
        # Траслитерация слова и обозначения его первой буквы на латинице
        match self.word[0]:
            case "е":
                self.word_manage('ye')
            case "ж":
                self.word_manage('zh')
            case "й":
                self.word_manage('iy')
            case "ч":
                self.word_manage('ch')
            case "ш":
                self.word_manage('sh')
            case "щ":
                self.word_manage('sch')
            case "ъ":
                self.word = "tverdyi-znak"
                self.FirstLetter = "tznak"
            case "ы":
                self.word = "y"
                self.FirstLetter = "y"
            case "ь":
                self.word = "myagkii-znak"
                self.FirstLetter = "mznak"
            case "ю":
                self.word_manage('yu')
            case "я":
                self.word_manage('ya')
            case _:
                self.word_manage(str(self.word[0]))

        search_url = f'{url}/{self.FirstLetter}/{self.word}.html'
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'lxml')
        dic = soup.find_all('div', class_="found_word")
        res = ""

        for gloses in dic:
            res += gloses.p.text

        if res == "":
            return "Информация не найдена"
        else:
            return res

    def __init__(self, word):
        self.word = word
