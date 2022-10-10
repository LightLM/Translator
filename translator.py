import requests

URL = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'NmE2MmVmMGMtYjY1NS00MTMyLTkxN2MtMDNlNTg2OWJkMzMzOmIxODkxMWQwYmM2MTQ3MDA5NjliM2JkYjYwMDk0ODE4'

headers = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL, headers=headers)
countinue = 'да'
# print(auth.text)
private_dict = {}

if auth.status_code == 200:
    print('Переводчик.')
    choice = int(
        input('\nВыберите перевод.\n1 - перевод с русского на английский\n2 - перевод с английского на русский\n'))

    if choice == 1:
        in_lang = 1049
        out_lang = 1033
    else:
        in_lang = 1033
        out_lang = 1049

    while countinue == 'да':

        text = input('\nВведите слово для перевода: ').lower()
        # print(text)

        token = auth.text
        headers_word = {'Authorization': 'Bearer ' + token}
        params = {
            'text': text,
            'srcLang': in_lang,
            'dstLang': out_lang
        }

        if text in private_dict:
            print('Перевод слова:', private_dict[text])

        else:
            r = requests.get(URL_TRANSLATE, headers=headers_word, params=params)
            result = r.json()

            try:
                print('Перевод слова:', result['Translation']['Translation'])

            except:

                print('Не найдено варианта перевода!')
                add = input('Хочешь добавить слово/перевод в словарь?(Да/Нет)\n').lower()
                if add == 'да':
                    translation_private = input('\nНапишите перевод слова: ').lower()
                    private_dict.update({text: translation_private})
                    private_dict.update({translation_private: text})

        countinue = input('\nХочешь продолжить?(Да/Нет)\n').lower()
else:
    print('Error!')
