#需求 第一个案例 在一个图形界面上绘制一个hello word

import pygame
import sys
from pygame.locals import *
#初始化pygame

'''pygame.init()

#获得系统的访问 创建一个窗口

screen = pygame.display.set_mode((600, 500))

#思路：利用pygema输入一个字体

#第一步 创建一个字体对象
#第一个参数 使用pygame默认的字体 第二个参数 字体大小
myFont = pygame.font.Font(None, 70)

#定义颜色变量 RGB 0-255 000黑色

white = 255,255,255 #字体颜色为白色

blue = 0,0,255 #界面的背景为蓝色

textTmage = myFont.render('Hello World', True, white)

while True:
    for e in pygame.event.get():
        if e.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)

    screen.blit(textTmage,(100, 100))

    pygame.display.update()'''

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('画圆')
blue = 0,0,255

while True:
    for e in pygame.event.get():
        if e.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)
    color = 255,255,255
    position = 300,250
    radius = 100
    width = 0

    pygame.draw.circle(screen, color, position, radius, width)
    pygame.display.update()