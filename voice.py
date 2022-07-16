import pyttsx3
from lib import Parse

engine = pyttsx3.init()
engine.say(
    "Я протокольный дроид Линг 01. Назовите мне слово, и я расскажу всё о нём")
engine.runAndWait()
word = input("")
ParseDicts = Parse(word)
engine.say("Согласно словарю Даля:")
engine.runAndWait()
engine.say(ParseDicts.parse("https://diclist.ru/slovar/dalya"))
engine.runAndWait()
engine.say("Согласно словарю Ожегова:")
engine.runAndWait()
engine.say(ParseDicts.parse("https://diclist.ru/slovar/ozhegova"))
engine.runAndWait()
engine.say("Согласно словарю Ушакова:")
engine.runAndWait()
engine.say(ParseDicts.parse("https://diclist.ru/slovar/ushakova"))
engine.runAndWait()
engine.say("Согласно словарю Ефремовой:")
engine.runAndWait()
engine.say(ParseDicts.parse("https://diclist.ru/slovar/efremovoy"))
engine.runAndWait()

