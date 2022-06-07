h = ''
while len(h) < 6:
    y = input('Введите данные: ')
    if y == 'q':
        continue
    elif y == 'Q':
        break
    else:
        h += y
else:
    print(h)
