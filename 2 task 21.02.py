mesto = int(input('Введите номер места: '))
if mesto % 2 == 0 and 37 <= mesto <= 54:
    print('Ваша полка будет верхняя боковая')
if mesto % 2 == 0 and mesto <= 36:
    print('Ваша полка будет верхняя в купе')
if mesto % 2 == 1 and 37 <= mesto <= 54:
    print('Ваша полка будет нижняя боковая')
else:
    print('Ваша полка будет нижняя в купе')
