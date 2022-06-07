import os

while True:
    site = input('Введите название сайта: \n')

    if 'https://' in site:
        os.system('start ' + site)
        print('if')
        break
    elif 'www.' in site:
        sayt = 'https://' + site
        os.system('start ' + site)
        print('elif')
    else:
        sayt = 'https://www.' + site
        os.system('start ' + site)
        print('elsa')
