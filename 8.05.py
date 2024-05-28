# 1
from PIL import Image
import os

soufil = '../../Downloads/im'
tarfil = '../../Downloads/imgs'

if not os.path.exists(tarfil):
    os.makedirs(tarfil)

# Функция обрабатывания изображения
def proc(im):
    img = Image.open(im)
    img = image.convert('RGB')
    img = image.point(lambda x: 255 - x)
    imgs = os.path.join(tarfil, os.path.basename(im))
    img.save(images)

# Обход всех файлов в исходной папке
for img in os.listdir(soufil):
    if img.endswith('.jpg') or img.endswith('.png'):
        file_path = os.path.join(soufil, imag)
        proc(file_path)


# 3
import csv
total = 0
with open('zadanieaip.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)
    print("Нужно купить:")
    for i in reader:
        product = i[0]
        q= int(i[1])
        cost = float(i[2])
        total += q * cost
        print(f"{product} - {q} шт. за {cost} руб.")

print(f"Итоговая сумма: {total} руб.")