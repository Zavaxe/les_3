# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(500, 300)
radius = 25
for _ in range(3):
    radius += 35
    sd.circle(point, radius, color=(0, 0, 0), width=3)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble_b(point, step):
    radius = 25
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color=(0, 0, 0), width=3)

def bubble_w(point, step):
    radius = 25
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color=(255, 255, 255), width=3)

def bubble2(point, step):
    radius = 25
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color=sd.random_color(), width=3)

point = sd.get_point(800, 300)
bubble_b(point=point, step=35)

point = sd.get_point(200, 300)
bubble_b(point=point, step=35)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble2(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
for y in range(200, 401, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble_w(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 20)
    bubble_b(point=point, step=step)


sd.pause()


