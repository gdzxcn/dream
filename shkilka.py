spisok = ["Математика", "Русский", "Немецкий", "Физкультура", "Информатика", "Физика"] 
#крики necromastery и вопли подо мной, руки дезоляторы, shadow nevermore =)
a = 1
while a == 1:
    print(*spisok)
    txt = input("Введите свой нелюбимый предмет: ")
    spisok.remove(txt)
    print(*spisok)
    txt2 = input("Еще есть нелюбимые предметы? y/n: ")
    if txt2 == "n":
        a = 2
    elif txt2 == "y":
        continue