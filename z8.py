def main1():
    from PIL import Image
    img = Image.open("dush.jpg")
    area = (100, 100, 1000, 1000)
    sor_img = img.crop(area)
    sor_img.save("crop_dush.jpg")
main1()
print("изображение успешно обрезано и сохранено")


def main2():
    from PIL import Image
    praz = {"День рождения": "др.jpg",
        "Новый год": "нг.jpg",
        "8 марта": "жендень.jpg",
        "День святого валентина": "вален.jpg"}
    hol = input("к какому празднику хотите открытку?")
    try:
        holx = praz[hol]
        print(f"вот открытка к празднику {hol}:")
    except KeyError:
        print("к такому празднику открытки нет(")
    holx_image = Image.open(holx)
    holx_image.show()
main2()

def main3():
    from PIL import Image, ImageDraw, ImageFont
    name = input("введите имя человека, которого хотите поздравить: ")
    text = f"{name}, поздравляю!"

    image = Image.open("др2.jpg")

    width, height = image.size
    font = ImageFont.truetype("arial.ttf", 40)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(name, font=font)
    draw.text(((width - text_width) // 2, 30), name, font=font, fill="pink")

    text_width, text_height = draw.textsize(text, font=font)
    draw.text(((width - text_width) // 2, height - 60 - text_height), text, font=font, fill="black")

    image.save("poz.png", "PNG")
    image.show()
main3()
