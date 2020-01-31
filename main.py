from ball import *
import pygame
from random import *
pygame.init()  
white = (255, 255, 255)
GREY= (198, 198, 198)
black= (0,0,0)
x=randint(1,155)
print(x)
# assigning values to height and width variable   
height = 1150  
width = 650 
#locical functions

#positional arguments
p1x=0
p1y=450
p2x=1060
p2y=450
ballx=0
bally=0
g1x=0
g1y=width//2+80
g2y=g1y
g2x=height-241+105
yvelocity=15
xvelocity=20
pyvelocity=15
moveballdown=True
moveballright=True

# creating the display surface object   
# of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode((height, width))  
  
# set the pygame window name   
background=pygame.display.set_caption('Head Soccer')  
  
# creating a surface object, image is drawn on it.   
background = pygame.image.load(r'C:\Users\Nikhil\Desktop\head soccer\background.png')  
p1 = pygame.image.load(r'C:\Users\Nikhil\Desktop\head soccer\p1.png')
p2 = pygame.image.load(r'C:\Users\Nikhil\Desktop\head soccer\p2.png')
ball= pygame.image.load(r'C:\Users\Nikhil\Desktop\head soccer\ball.png')
g1 = pygame.image.load(r'C:\Users\Nikhil\Desktop\head soccer\g1.png')
g2 = pygame.image.load(r'C:\Users\Nikhil\Desktop\head soccer\g2.png')

ball.set_colorkey(black)
#p1.set_colorkey(white)
p2.set_colorkey(white)
#ball.set_colorkey(GREY)
# infinite loop

while True:
    groundx=list(i for i in range(0,1150-99))
    groundy=list(i for i in range(0,650-96))
    p1xrange=list(i for i in range(p1x,p1x+87))
    p1yrange=list(i for i in range(p1y,p1y+90))
    p2xrange=list(i for i in range(p2x,p2x+87))
    p2yrange=list(i for i in range(p2y,p2y+103))
    #x,y=pygame.mouse.get_pos()
    #print('x=',x,'y=',y)
    display_surface.fill(white)  
    display_surface.blit(background,(0, 0))
    b=Ball(ballx,bally)    
    display_surface.blit(ball,(ballx, bally))
    display_surface.blit(g1,(g1x, g1y))
    display_surface.blit(g2,(g2x, g2y))
    #print(ballx,bally)
    #print(p2x,p2y)
    #b.y=b.move(b.x,b.y)
    #display_surface.blit(ball,(x, y))
    display_surface.blit(p1,(p1x,p1y))
    display_surface.blit(p2,(p2x,p2y))  
    #bally+=1
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
        # Draws the surface object to the screen.
##        if event.type==pygame.KEYDOWN:    
##            if event.key == pygame.K_DOWN:
##                bally+=yvelocity
##            elif event.key ==pygame.K_UP:
##                bally-=yvelocity
##                
##            elif event.key ==pygame.K_LEFT:
##                ballx-=xvelocity
##                
##            elif event.key ==pygame.K_RIGHT:
##                ballx+=xvelocity
##            else:
##                break
    keys = pygame.key.get_pressed()  #checking pressed keys
##    if keys[pygame.K_UP]:
##        bally -= yvelocity
##    if keys[pygame.K_DOWN]:
##        bally += yvelocity
##    if keys[pygame.K_LEFT]:
##        ballx -= xvelocity
##    if keys[pygame.K_RIGHT]:
##        ballx += xvelocity
    
    if keys[pygame.K_UP]:
        if p1y >0:
            p1y-= pyvelocity
        else:
            p1y+=1
    if keys[pygame.K_DOWN]:
        if p1y <groundy[len(groundy)-1]:
            p1y += pyvelocity
        else:
            p1y-=1
       
    ballx+=xvelocity
    bally+=yvelocity
    if ballx not in groundx :
        xvelocity*=-1
    if bally not in groundy :
        yvelocity*=-1
    if bally in p1yrange and ballx in p1xrange:
        print(ballx,bally)
        xvelocity*=-1
        yvelocity*=-1
    if bally+96 in p2yrange and ballx+99 in p2xrange:
        xvelocity*=-1
        yvelocity*=-1
            #pygame.display.update()
    p2y=bally
    pygame.display.update()   
    
