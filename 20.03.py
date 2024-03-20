# # 1

# def k(n):
#     if n % 5 == 0:
#         return 1
#     else:
#         return 0
#
#
# n = int(input('введите число для проверки'))
# if k(n) == 1:
#     print('число делится на 5')
# else:
#     print('число не делится на 5')


# # 2

# def deli(n):
#     if n.isdigit() == False:
#         return ValueError
#     elif int(n) == 0:
#         return ZeroDivisionError
#     return 300 / int(n)
#
#
# n = input('введите число')
# print(deli(n))


# # 3

# def mag_data(n):
#     if str(data_d * data_m) == str(data_y[2:]):
#         return True
#     else:
#         return False
#
#
# n = ''
# data_d = int(input('введите день'))
# data_m = int(input('введите месяц'))
# data_y = input('введите год')
# print(mag_data(n))


# 4

def hap(num):
    if sum(num_1) == sum(num_2):
        return True
    else:
        return False


num = str(input('введите номер билета'))
num_1 = str(num[:len(num) // 2])
num_2 = str(num[len(num) // 2:])
print(hap(num))



