# # 1
# def a():
#     b = [0, 1, 2, 3, 4]
#     num = int(input('введите число'))
#     if num in b:
#         return ('Поздравляю, Вы угадали число!')
#     else:
#         return ('Нет такого числа!')
#
#
# print(a())
import random


# # 2
# def b():
#     n = int(input('введите кол-во элементов в списке'))
#     a = []
#     for i in range(n):
#         el = input('введите элемент')
#         a.append(el)
#     pov = [elem for elem in a if a.count(elem) > 1]
#     if pov:
#         return (set(pov))
#     else:
#         return ('нет повторяющихся значений')
#
#
# print(b())

# # 3
# def c():
#     day = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
#     vishodnoi = int(input('сколько выходных на неделе вы хотите?'))
#     b = tuple(day)
#     if vishodnoi == 0:
#         return (f"Ваши рабочие дни: {b}")
#     elif vishodnoi == 1:
#         return (f"Ваши выходные дни: {b[6:]}"), (f"Ваши рабочие дни: {b[:6]}")
#     elif vishodnoi == 2:
#         return (f"Ваши выходные дни: {b[5:]}"), (f"Ваши рабочие дни: {b[:5]}")
#     elif vishodnoi == 3:
#         return (f"Ваши выходные дни: {b[4:]}"), (f"Ваши рабочие дни: {b[:4]}")
#     elif vishodnoi == 4:
#         return (f"Ваши выходные дни: {b[3:]}"), (f"Ваши рабочие дни: {b[:3]}")
#     elif vishodnoi == 5:
#         return (f"Ваши выходные дни: {b[2:]}"), (f"Ваши рабочие дни: {b[:2]}")
#     elif vishodnoi == 6:
#         return (f"Ваши выходные дни: {b[1:]}"), (f"Ваши рабочие дни: {b[:1]}")
#
#
# print(c())


# 4
def d():
    last_name_1 = ['Анисимов', 'Гусева', 'Токарева', 'Поспелова', 'Орел', 'Идрисова', 'Зотова', 'Бречалова', 'Екимова',
                   'Свиреденко']
    last_name_2 = ['Семенов', 'Козодерова', 'Кучев', 'Блисгарев', 'Федоров', 'Белкина', 'Гагельганс', 'Соколенко',
                   'Дзя',
                   'Матвеев']
    a = []  # спорт команда
    for i in range(5):
        q = random.randint(0, 9)
        if a.count(last_name_1[q]) == 0:
            a.append(last_name_1[q])
        else:
            q = random.randint(0, 9)
            a.append(last_name_1[q])

    for i in range(5):
        q = random.randint(0, 9)
        if a.count(last_name_2[q]) == 0:
            a.append(last_name_2[q])
        else:
            q = random.randint(0, 9)
            a.append(last_name_2[q])

    return last_name_1, last_name_2, a, len(a), sorted(a), a.count('Иванов')


print(d())
