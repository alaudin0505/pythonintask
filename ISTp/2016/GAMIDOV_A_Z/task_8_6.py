# Задача 8. Вариант 3.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
# подсказку в том случае, если у него нет никаких предположений. Разработайте
# систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
# получали больше тех, кто запросил подсказку.
# Gamidov A. Z.
# 02.11.2016

import random


WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

correct = random.choice(WORDS)
word = correct
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[position+1:]

print('''
            Добро пожаловать в игру "Анограммы"!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводя своей версии.)
    (Для получения подсказки введите :п)
''')
print("Вот анаграмма:", jumble)

hint = ""
while True:
    guess = input("\nПопробуйте отгадать исходное слово: ")
    if not guess:
        break
    elif guess == ":п":
        litter = correct[len(hint)]
        hint += litter.upper()
        jumble = jumble.replace(litter, "")
        if len(hint) == len(correct):
            print("Вы проиграли!\nПравильное слово: ", hint)
        else:
            print("Подсказка:", hint+jumble)
    elif guess != correct:
        print("К сожалению, вы не правы.")
    else:
        print("Да, именно так! Вы отгадали!\n")
        print("Вам начислено {} баллов".format((len(correct) - len(hint)) * 100))
        break

print("Спасибо за игру.")
input("\nНажмите Enter для выхода.")
