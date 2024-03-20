# 3.1
n = int(input('Введите количество слов:'))
otv = ''
for i in range(n):
        clova = input('Введите слово:')
        otv = otv + clova + '-'
print(otv[:-1])

# # 3.2
# i = otv = ''
# while i != 'stop':
#     clova = input('Введите слово:')
#     otv = otv + clova + ' '
#     i = input('Если программу необходимо завершить введите "stop", иначе введите любой символ')
# print(otv)

# # 3.3
# clovo = str(input('Введите слово для проверки:'))
# k = 0
# for i in clovo:
#     if 'ф' in clovo:
#         k += 1
#     else:
#         k = k
# if k >= 1:
#     print('Ого! Это редкое слово')
# else:
#     print('Эх, это не очень редкое слово')

# # 3.4
# from random import randint
#
# c = k = 0
# while c < 3:
#     a = randint(0, 9)
#     b = randint(0, 9)
#     otv = a + b
#     print('посчитай', str(a), '+', str(b))
#     otv_1 = int(input('Введи ответ'))
#     if str(otv) == str(otv_1):
#         print('Правильно!')
#         k += 1
#     else:
#         print('Ответ неверный!')
#         c += 1
# print('Игра окончена.Правильных ответов', k)