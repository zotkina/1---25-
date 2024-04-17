from PIL import Image


# def a():
#     im = Image.open('надо.webp')
#     im.show()
#     print('размер', im._size)
#     print('формат', im.format)
#     print('цветовая модель', im.mode)
#
#
# a()


# noinspection PyTypeChecker
def b():
    im = Image.open('надо.webp')
    a = int(im.width // 3)
    im.resize_width_proportionally(a)
    c = int(im.height // 3)
    im.resize_height_proportionally(c)
    im.show()
    im_f_g = im.transpose(Image.flip_right_left)
    im_f_g.show()


b()
