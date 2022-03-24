import time
def run():
    txt=("Добро пожаловать в игру")
    for i in txt:
        time.sleep(0.1)
        print(i, end='', flush=True)
    print('')
    while True:
        txt2=('Перед тобой 10 сундуков. 9 из них заминированы, а в одном лежит ключ, открывающий дверь в следущую комнату. Выбери сундук, который ты откроешь.')
        for i in txt2:
            time.sleep(0.1)
            print(i, end='', flush=True)
        print('')
        a=input()
        if a=="3":
            print('А тебе везёт!')
        else:
            print('KABOOM')
            break
        txt3=('Похоже, что тут 5 ключей, но попытка только одна. Если ключ не подойдёт, вся тестовая камера взлетит на воздух. Время выбора')
        for i in txt3:
            time.sleep(0.1)
            print(i, end='', flush=True)
        print('')
        b=input()
        if b=="1":
            time.sleep(0.1)
            print('Я впечатлён твоим везением. Продолжение выйдет в ближайшее время')
            break
        else:
            print('KABOOM')
            break
while True:
    print('Хочешь начать игру? да/нет')
    a = input()
    b = str.lower(a)
    if b == "да":
        run()
    else:
        break
#задумка отличная и реализация вполне
#я предлагаю доделать небольшое продолжение и выложить в гитхаб
