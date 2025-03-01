import pygame

pygame.init()

screen=pygame.display.set_mode([1000,1000])

def rhombus_draw(cordx,cordy,rangex,rangey,cycle):
    if cordx>100 or cordy>100 or cycle>900:
        return
    pygame.draw.line(screen,[255,255,255],[400+cordx,400],[500,300+cordy])
    pygame.draw.line(screen, [255, 255, 255], [500, 300+cordy],[600-cordx,400] )
    pygame.draw.line(screen, [255, 255, 255], [600-cordx, 400], [500, 500-cordy])
    pygame.draw.line(screen, [255, 255, 255], [500, 500-cordy], [400+cordx+20,400 ])

    rhombus_draw(cordx+rangex,cordy+rangey,rangex,rangey,cycle+1)
cordx=20
cordy=20
rangex=20
rangey=20

pygame.key.set_repeat(50)
while True:
    screen.fill([0,0,0])
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN and event.key==pygame.K_1:
            cordx+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
            cordx-=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_2:
            cordy+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
            cordy-=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_3:
            rangex+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_e:
            rangex-=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_4:
            rangey+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            rangey-=1
    rhombus_draw(cordx,cordy,rangex,rangey,1)
    pygame.display.flip()