import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(from_file, to_file, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    with open(from_file, 'r') as f:
        text = f.read().strip()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=params)
    json_ = response.json()
    print(json_)

    with open(to_file, 'w') as f:
        f.write(''.join(json_['text']))


src_dir = os.path.dirname(__file__)
file_list = [f for f in os.listdir(src_dir) if f.endswith('.txt')]
file_list = list(map(lambda f: os.path.join(src_dir, f), file_list))

for file in file_list:
    file_name = os.path.basename(file).split('.')[0].lower()
    translate_it(file, '{}{}rus_{}.txt'.format(os.path.dirname(file), os.sep, file_name), file_name, 'ru')