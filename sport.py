spisok = ["Бокс", "Фехтование"]
a = 1
while a == 1:
    print(*spisok)
    num1 = input("Введите свой любимый вид спорта: ")
    spisok.append(num1)
    print(*spisok)
    b = input("Есть еще любимый спорт? y/n: ")
    if b == "n":
        a = 2
    elif b == "y":
        continue


    