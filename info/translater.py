import requests
import json

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
KEY = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'
# text = 'Hello'
# lang = 'en-ru'

# print(r.text)

def translate(text, lang = 'ru-en'):
    r = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
    data = json.loads(r.text)
    return data['text'][0]

def main():
    text = input('Введите текст для перевода - ')
    print(f'Ваше слово переведено - {translate(text)}')

if __name__ == "__main__":
    main()