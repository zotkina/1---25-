from PIL import Image, ImageFilter


# def f_1():
#     im = Image.open('надо.webp')
#     im.show()
#     print('размер', im._size)
#     print('формат', im.format)
#     print('цветовая модель', im.mode)
#
#
# f_1()


# # noinspection PyTypeChecker
# def f_2():
#     im = Image.open("надо.webp")
#     a = int(im.width) // 3
#     c = int(im.height) // 3
#     im_n = im.resize((a, c))
#     im_n.show()
#     im_n.save("изм.jpg")
#     img1 = im_n.transpose(Image.FLIP_TOP_BOTTOM)
#     img1.show()
#     im_n.save("горизонтальный.jpg")
#     img2 = im_n.transpose(Image.FLIP_RIGHT_LEFT)
#     img2.show()
#     im_n.save("вертикальный.jpg")
#
#
# f_2()


# def f_3():
#     im = '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg'
#     for im_n in im:
#         img = Image.open(im_n)
#         im_f = img.filter(ImageFilter.FIND_EDGES)
#         im_f.show()
#
# f_3()


def f4():
    im = "надо.webp"
    im_w = im
    im_w.drawstring()
    im_w.show()
    im_w.save("new")


f4()
