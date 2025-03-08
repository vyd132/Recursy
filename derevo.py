import pygame

pygame.init()

screen=pygame.display.set_mode([1000,1000])

def tree_draw(start_x,start_y,height,width,width_koeff,height_koeff,trees_col,color,side):
    if height<5 or trees_col>=10:
        return
    if side=='left':
        color=[255,0,0]
        side_left = 'left'
        side_right = 'left'
    elif side=='center':
        color=[0,255,0]
        side_left='left'
        side_right = 'right'
    else:
        color = [0, 0, 255]
        side_left = 'right'
        side_right = 'right'
    pygame.draw.line(screen,color,[start_x,start_y],[start_x,start_y-height])
    pygame.draw.line(screen,color,[start_x,start_y-height],[start_x-width,start_y-height])
    pygame.draw.line(screen, color, [start_x, start_y-height], [start_x+width,start_y-height])
    trees_col+=1
    tree_draw(start_x-width,start_y-height,height*height_koeff,width*width_koeff,width_koeff,height_koeff,trees_col,color,side_left)
    tree_draw(start_x+width,start_y-height, height*height_koeff,width*width_koeff,width_koeff,height_koeff,trees_col,color,side_right)

height=200
width=200
height_koeff=0.5
width_koeff=0.5
pygame.key.set_repeat(50)
while True:
    screen.fill([0,0,0])
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and pygame.KMOD_SHIFT & pygame.key.get_mods():
            height-=1
            continue
        if event.type==pygame.KEYDOWN and event.key==pygame.K_1:
            height+=1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and pygame.KMOD_SHIFT & pygame.key.get_mods():
            width-=1
            continue
        if event.type==pygame.KEYDOWN and event.key==pygame.K_2:
            width+=1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3 and pygame.KMOD_SHIFT & pygame.key.get_mods():
            width_koeff -= 0.01
            continue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            width_koeff += 0.01
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4 and pygame.KMOD_SHIFT & pygame.key.get_mods():
            height_koeff -= 0.01
            continue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            height_koeff += 0.01

    tree_draw(500,1000,height,width,width_koeff,height_koeff,1,[0,255,0],'center')
    print(bin(pygame.key.get_mods()))
    pygame.display.flip()