from PIL import Image

img = Image.open("image.jpg")
def a():
    # Область для обрезки (левая верхняя точка (x, y), правая нижняя точка (x, y))
    obl = (100, 100, 400, 400)
    sor_img = img.sor(obl)
    sor_img.save("cropped_image.jpg")
a()
print('Изображение обрезано и сохранено')


prazdnic = {'День рождения': 'др.png';'Новый год': 'нг.jpg'; '8 марта': '8марта.jpg';'День Святого Валентина': 'st_val.jpg'}

def b():
    praz = input('К какому празднику необходима открытка?')
    try:
        praz = prazdnic[hol]
        print(f"Вот открытка к празднику {praz}:")
    except KeyError:
        print('Открытки для выбранного праздника нет')
b()

def с(name, text):
    image = Image.open('др.jpg')

    width, height = image.size
    f = ImageFont.truetype('arial.ttf', 50)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(name, font=f)
    draw.text(((width - text_width) // 2, 50), name, font=f, fill="blue")

    text_width, text_height = draw.textsize(text, font=f)
    draw.text(((width - text_width) // 2, height - 60 - text_height), text, font=f, fill="white")

    image.save("pozdravok.png", "PNG")

name = input('Введите имя человека для поздравления: ')
text = f"{name}, поздравляю!"
create_pozdravok(name, text)
