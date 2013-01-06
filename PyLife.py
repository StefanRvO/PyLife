#!/usr/bin/python2
#Conway's game of Life written in python. For more info, see the README


import pygame
from pygame.locals import *
import time
import random
from sys import exit

#Set screensize
SCREENSIZE=(1300,700)

#Set colour of the cells
ALIVECOLOUR=(255,255,255)
DEADCOLOUR=(0,0,0)
DEADCOLOUR=BACKGROUNDCOLOUR=(17,20,70)
TICKRATE=2
GOTHROUGH=0

#SET size of cells in pixels

UNITSIZE=20

class unit(object):
    def __init__ (self, sizex, sizey=None ,screensize=SCREENSIZE):
        self.x=sizex
        if sizey==None:
            self.y=self.x
        else:
            self.y=sizey
        self.gridsize=(screensize[0]/self.x,screensize[1]/self.y)
    def __str__ (self):
        return str(self.x)+"*"+str(self.y)

class Tick(object):
    def __str__ (self):
        alive=0
        #if we try to print this, give number of alive cells
        for x in range(len(self.current)):
            for y in self.current[x]:
                if y==1:
                    alive+=1
        return str(alive)
    def __int__ (self):
        alive=0
        #if we try to print this, give number of alive cells
        for x in range(len(self.current)):
            for y in self.current[x]:
                if y==1:
                    alive+=1
        return alive
    def generate(self,seed, sizex,sizey):
        self.current = [[0]*sizey for i in range(sizex)]
        self.previous=self.current
        random.seed(seed)
        self.sizex=sizex
        self.sizey=sizey
        for x in range(sizex):
            for y in range(sizey):
                if (random.randint(0,10)==10):
                    self.current[x][y]=1
                else:
                    self.current[x][y]=0
    def nexttick(self):
        #run with go-through borders
        self.previous=self.current
        for x in range(self.sizex):
            for y in range(self.sizey):
                besideCellsAlive=0
                #if we run with go-through borders:
                #if in end of array, loop around and check index 0
                #else we asume cells outside of area is dead, and thus don't check 
                if x==self.sizex-1 and y==self.sizey-1:
                    if self.previous[x-1][y]:
                        besideCellsAlive+=1
                    if self.previous[x-1][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x][y-1]:   
                        besideCellsAlive+=1
                    if GOTHROUGH:
                        if self.previous[x-1][0]:   
                            besideCellsAlive+=1
                        if self.previous[x][0]:   
                            besideCellsAlive+=1
                        if self.previous[0][y]:
                            besideCellsAlive+=1
                        if self.previous[0][y-1]:   
                            besideCellsAlive+=1
                        if self.previous[0][0]:   
                            besideCellsAlive+=1
                elif x==self.sizex-1:
                    if self.previous[x-1][y]:
                        besideCellsAlive+=1
                    if self.previous[x-1][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x-1][y+1]:   
                        besideCellsAlive+=1
                    if self.previous[x][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x][y+1]:   
                        besideCellsAlive+=1
                    if GOTHROUGH:
                        if self.previous[0][y]:
                            besideCellsAlive+=1
                        if self.previous[0][y-1]:   
                            besideCellsAlive+=1
                        if self.previous[0][y+1]:   
                            besideCellsAlive+=1
                elif y==self.sizey-1:
                    if self.previous[x-1][y]:
                        besideCellsAlive+=1
                    if self.previous[x-1][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x+1][y]:
                        besideCellsAlive+=1
                    if self.previous[x+1][y-1]:   
                        besideCellsAlive+=1
                    if GOTHROUGH:
                        if self.previous[x-1][0]:   
                            besideCellsAlive+=1
                        if self.previous[x+1][0]:   
                            besideCellsAlive+=1
                        if self.previous[x][0]:   
                            besideCellsAlive+=1
                else:
                    if GOTHROUGH:
                        if self.previous[x+1][y-1]:   
                            besideCellsAlive+=1
                        if self.previous[x-1][y]:
                            besideCellsAlive+=1
                        if self.previous[x-1][y-1]:   
                            besideCellsAlive+=1
                        if self.previous[x-1][y+1]:   
                            besideCellsAlive+=1
                        if self.previous[x][y-1]:   
                            besideCellsAlive+=1
                    else:
                        if y:
                            if self.previous[x][y-1]:   
                                besideCellsAlive+=1
                            if self.previous[x+1][y-1]:   
                                besideCellsAlive+=1
                        if x:
                            if self.previous[x-1][y+1]:   
                                besideCellsAlive+=1
                            if self.previous[x-1][y]:
                                besideCellsAlive+=1
                        if x and y:
                            if self.previous[x-1][y-1]:   
                                besideCellsAlive+=1
                            
                            
                    if self.previous[x][y+1]:   
                        besideCellsAlive+=1
                    if self.previous[x+1][y]:
                        besideCellsAlive+=1
                    if self.previous[x+1][y+1]:   
                        besideCellsAlive+=1
                if besideCellsAlive<2:
                    self.current[x][y]=0
                elif besideCellsAlive==3:
                    self.current[x][y]=1
                elif besideCellsAlive>3:
                    self.current[x][y]=0
                elif besideCellsAlive==2 and self.current[x][y]==1:
                    self.current[x][y]=1
def DrawScreen():
    screen.fill(BACKGROUNDCOLOUR)
    for x in range (game.sizex):
        for y in range(game.sizey):
            if game.current[x][y]:
                pygame.draw.rect(screen,ALIVECOLOUR,pygame.Rect((x*UNITSIZE,y*UNITSIZE),(UNITSIZE,UNITSIZE)))
            elif not DEADCOLOUR==BACKGROUNDCOLOUR:
               pygame.draw.rect(screen,DEADCOLOUR,pygame.Rect((x*UNITSIZE,y*UNITSIZE),(UNITSIZE,UNITSIZE)))
    pygame.display.flip()
    
              
    

#initialize unit
U=unit(UNITSIZE)
#INITIALIZE game structure
game=Tick()

pygame.init()
screen=pygame.display.set_mode((U.gridsize[0]*U.x,(U.gridsize[1])*U.y),0,32)
clock=pygame.time.Clock()

#generate initial state
game.generate(time.gmtime(),U.gridsize[0],U.gridsize[1])

#Gameloop
while 1:
    #generate next generation
    if not TICKRATE==0:
        game.nexttick()
    
     #event loop for controls
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        elif event.type==KEYDOWN:
            #Control speed on left and right
            if event.key==K_LEFT and TICKRATE>0:
                TICKRATE-=1
            if event.key==K_RIGHT and TICKRATE>0:
                TICKRATE+=1
            #Pause on space (and unpause going back to previous value
            if event.key==K_SPACE:
                if not TICKRATE==0:
                    PrevTICKRATE=TICKRATE
                    TICKRATE=0
                else:
                    TICKRATE=PrevTICKRATE
                    PrevTICKRATE=0
                #Run at max speed if shift is pressed
            if event.key==K_RSHIFT:
                if not TICKRATE==-1:
                    PrevTICKRATE=TICKRATE
                    TICKRATE=-1
                else:
                    TICKRATE=PrevTICKRATE
                    PrevTICKRATE=0
    


    #Do not draw if board is paused. Except if forced by some event
    if not TICKRATE==0 or DrawNext==1:
        DrawScreen()
        DrawNext=0
    if not TICKRATE==0:
        tickingtime=clock.tick(TICKRATE)
    else:
        #Only run with 10 loops per second if paused. Should be enough
        tickingtime=clock.tick(10)
    
#    if(int(game)>7000):               #debug 
#        game.generate(time.gmtime(),U.gridsize[0],U.gridsize[1])
#    print((1./tickingtime)*1000) #debug
#    print(TICKRATE)
#    print(int(game))              #debug
