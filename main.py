import random

import pygame

pygame.init()

screen=pygame.display.set_mode([1000,1000])

def circle_draw(radius,width,range,water_radius,color,r,g,b):
    if radius<100:
        radius=water_radius
        pygame.draw.circle(screen, [0, 0, 255], [500, 500], radius)
        return
    if width<1:
        width=1
    if range < 5:
        range=5
    color[0]+=r
    color[0]=min(color[0],255)
    color[0] = max(color[0], 0)
    color[1] += g
    color[1]=min(color[1],255)
    color[1] = max(color[1], 0)
    color[2] += b
    color[2]=min(color[2],255)
    color[2] = max(color[2], 0)
    print(color)
    pygame.draw.circle(screen,color,[500,500],radius,width)
    circle_draw(radius-range,width-1,range-2,water_radius,color,r,g,b)


r=5
g=5
b=5
radius=400
width=1
range=10
water_radius=100
pygame.key.set_repeat(50)
while True:
    screen.fill([0,0,0])
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN and event.key==pygame.K_1:
            radius+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
            radius-=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_2:
            width+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
            width-=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_3:
            range+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_e:
            range-=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_4:
            water_radius+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            water_radius-=1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            r += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            r -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            g += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            g -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
            b += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            b -= 1

    circle_draw(radius,width,range,water_radius,[255,255,255],r,g,b)
    pygame.display.flip()
    pass