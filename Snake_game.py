import pygame
import os
import colors_rgb as cl
import random
pygame.init()
G_text=pygame.font.SysFont("arial", 60, bold=True, italic=False)

# global variables
SCREEN_WIDTH=1300
SCREEN_HEIGHT=600

WindowScreen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
score=0
# start window
def Start_window(*args):
    s_window=True
    while s_window:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                s_window=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    s_window=False
        WindowScreen.fill(cl.black)
        Start_text=G_text.render(f"Press Enter to START",True,cl.green)
        WindowScreen.blit(Start_text,(int(SCREEN_WIDTH/2-200),int(SCREEN_HEIGHT/2)))
        pygame.display.update()
        pass
    pass
# main function
def Main_fun(*args):
    # player
    def plot_snake(WindowScreen, color, snake_list, sizes):
        if starts==True:
            for play_x,play_y in snake_list:
                pygame.draw.circle(WindowScreen, cl.yellow, (play_x,play_y), sizes)
        pass
    play_x=int(SCREEN_HEIGHT/2+200)
    play_y=int(SCREEN_WIDTH/2-100)
    vel_x=0
    vel_y=0
    # food
    food_x=random.randint(40,SCREEN_WIDTH-40)
    food_y=random.randint(40,SCREEN_HEIGHT-40)
    snake_list=[]
    snake_length=1
    # clock
    clk=pygame.time.Clock()
    # start
    starts=True
    # startgame
    startgame=True
    while startgame:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                startgame=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if starts==True:
                        vel_y=-3
                        vel_x=0
                if event.key==pygame.K_DOWN:
                    if starts==True:
                        vel_y=3
                        vel_x=0
                if event.key==pygame.K_LEFT:
                    if starts==True:
                        vel_x=-3
                        vel_y=0
                if event.key==pygame.K_RIGHT:
                    if starts==True:
                        vel_x=3
                        vel_y=0
                if event.key==pygame.K_TAB:
                    starts=False
                if event.key==pygame.K_SPACE:
                    starts=True
        # background
        WindowScreen.fill(cl.dark_grey)
        head=[]
        head.append(play_x)
        head.append(play_y)
        snake_list.append(head)
        plot_snake(WindowScreen, cl.yellow,snake_list, 15)
        pygame.draw.circle(WindowScreen, cl.red, (play_x,play_y), 15, 3)
        # pygame.draw.circle(WindowScreen, cl.yellow, (play_x,play_y), 20)
        pygame.draw.circle(WindowScreen, cl.green, (food_x,food_y), 15)
        if starts==True:
            play_x+=vel_x
            play_y+=vel_y
            if play_x>=(SCREEN_WIDTH-15) or play_x<=15:
                vel_x=0
                starts=False
            if play_y>=(SCREEN_HEIGHT-15) or play_y<=15:
                vel_y=0
                starts=False
            if abs(play_x-food_x)<=17 and abs(play_y-food_y)<=17:
                global score
                score+=1
                snake_length+=15
                food_x=random.randint(40,SCREEN_WIDTH-40)
                food_y=random.randint(40,SCREEN_HEIGHT-40)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                starts=False
            pass
        if starts==False:
            scores_x=int(SCREEN_WIDTH/2-80)
            scores_y=int(SCREEN_HEIGHT/2-100)
            T1=G_text.render(f"Score:-{score}",True,cl.yellow)
            WindowScreen.blit(T1,(scores_x,scores_y))
            pass
        pygame.display.update()
        clk.tick(100)
    pass

Start_window()
Main_fun()