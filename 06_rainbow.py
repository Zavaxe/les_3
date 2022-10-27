# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (500, 500)

#def rainbow():
   # x = 50
    #x1 = 350
    #for color in rainbow_colors:
     #   x += 5
      #  x1 += 5
       # point_st = sd.get_point(x, 50)
        #point_end = sd.get_point(x1, 450)
        #sd.line(start_point=point_st, end_point=point_end, color=color, width=4)

#rainbow()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
def rainbow_circle():
    point = sd.get_point(250, 50)
    radius = 300
    for color in rainbow_colors:
        radius += 5
        sd.circle(center_position=point, radius= radius, color=color, width=4)

rainbow_circle()

sd.pause()
