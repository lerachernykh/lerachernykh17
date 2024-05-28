import os
from PIL import Image, ImageFilter
from pathlib import Path
import csv
def main1():
    os.mkdir("laba2")
    files = os.listdir("laba")
    for i in files:
        if Path(i).suffix == ".jpg":
            image = Image.open(os.path.join('laba', i))
            img_smooth = image.filter(ImageFilter.DETAIL)
            img_smooth.save(f"filter({i}).jpg")
            f = open(os.path.join("laba2", f"filter({i}).jpg"), "a")
            os.remove(f"filter({i}).jpg")
        else:
            f = open(os.path.join("laba2", i), "a")
main1()
def main3():
    print("Нужно купить:")
    with open("fail.csv", "r") as file:
        filereader = csv.reader(file)
        for row in filereader:
            name, col, price = " ".join(row).split(";")
            print (f"{name} - {col} шт. за {price} руб.")

main3()