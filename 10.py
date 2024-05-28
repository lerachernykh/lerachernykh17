import json
def main12():
    n = input("Какой продукт Вы хотите добавить?")
    p = input("Сколько он будет стоить?")
    a = input("Он в есть в наличии? ")
    dictionary = {}
    dictionary["name"] = n
    dictionary["price"] = p
    if a == "Да":
        dictionary["available"] = True
    else:
        dictionary["available"] = False
    with open('prod10.json', encoding="utf-8") as fcc_file:
        text = json.load(fcc_file)
        text["products"].append(dictionary)
        with open('prod10.json', 'w', encoding="utf-8") as outfile:
            json.dump(text, outfile, ensure_ascii=False, indent=4)
    with open('prod10.json', 'r', encoding="utf-8") as f:
        t = json.load(f)
    for txt in t["products"]:
        if  txt["available"] == True:
            print("Название:", txt["name"], "\n", "Цена:", txt["price"], "\n", "В наличии","\n","\n")
        else:
            print("Название:", txt["name"], "\n", "Цена:", txt["price"], "\n", "Нет в наличии!","\n","\n")
main12()
def main3():
    import json
    filename = 'en-ru.txt'
    dict1 = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip("-")
    out_file = open("slov10.json", "w")
    json.dump(dict1, out_file, ensure_ascii=False, indent=4, sort_keys=False)
    out_file.close()
    with open('slov10.json', 'r', encoding="utf-8") as f:
        t = json.load(f)
        swapped = { value: key for key, value in t.items()}
        with open('slov10.json', 'w', encoding="utf-8") as outfile:
            json.dump(swapped, outfile, ensure_ascii=False, indent=4, sort_keys=True)
    with open('slov10.json', 'r', encoding="utf-8") as d:
        w = json.load(d)
        with open('ru-en.txt', 'w', encoding="utf-8") as file:
            for key, value in w.items():
                file.write(f'{key} - {value}\n')
main3()