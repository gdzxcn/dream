import random
import time
text = ("Рандомайзер beta")
for i in text:
    time.sleep(0.1)
    print(i, end='', flush= True)
a = 1
print('')
while a == True:
    text2 = ("От какого числа рандом?")
    for i in text2:
        time.sleep(0.1)
        print(i, end='', flush= True)
    print('')
    first = int(input())
    text3 = ("До какого числа рандом?")
    for i in text3:
        time.sleep(0.1)
        print(i, end='', flush= True)
    print('')
    first2 = int(input())
    b = random.randint(first, first2)
    txt = (f"Сгенерированное число = {b}")
    for i in txt:
        time.sleep(0.1)
        print(i, end='', flush=True)
    print('')
    txt2 = ("Еще раз?")
    for i in txt2:
        time.sleep(0.1)
        print(i, end='', flush=True)
    print('')
    c = input()
    if c != "да":
        break
txt3 = ("До свидания!")
for i in txt3:
    time.sleep(0.1)
    print(i, end='', flush=True)
print('')