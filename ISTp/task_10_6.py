# Задача 10. Вариант 3.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно
# быть предоставлено 30 пунктов, которые можно распределить между четырьмя
# характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
# пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
# туда из характеристик, которым он решил присвоить другие значения.
# Gamidov A. Z.
# 02.11.2016

from collections import OrderedDict
import os


stats = OrderedDict.fromkeys(["Сила", "Здоровье", "Мудрость", "Ловкость"], 0)
max_points = 30
used_points = 0
old_used_points = None
selected_stat = None
new_stat_value = None
action = None
while True:

    print("Осталось очков: {} из {}".format(used_points, max_points))
    for stat, value in stats.items():
        if selected_stat == stat:
            print("  [*]{}\t\t\t{}({})".format(stat, new_stat_value, value))
        else:
            print("  []{}\t\t\t{}".format(stat, value))
    if not selected_stat:
        choice = input("Выберете характеристику, которую хотите изменить.\nДля выхода нажмите Enter, оставив поле пустым\n>")
        if not choice:
            break
        elif choice in stats.keys():
            selected_stat = choice
            new_stat_value = stats[selected_stat]
            old_used_points = used_points
    else:
        if not action:
            act = input("П - повысить характеристику. У - уменьшить характеристику\nС - сохранить. О - отмена\n>")
            if act == "С":
                stats[selected_stat] = new_stat_value
                new_stat_value = None
                selected_stat = None
            elif act == "О":
                selected_stat = None
                new_stat_value = None
                used_points = old_used_points
            elif act == "П" or act == "У":
                action = act
        else:
            delta = int(input("Введите число на которое вы хотите повысить или уменьшить характеристику\n>"))
            if action == "П" and delta + new_stat_value + used_points <= max_points:
                new_stat_value += delta
                used_points += delta
            elif action == "У" and new_stat_value - delta >= 0:
                new_stat_value -= delta
                used_points -= delta
            else:
                input("Введённые данные не верны. Нажмите Enter и попробуйте ещё раз.")
            action = None
