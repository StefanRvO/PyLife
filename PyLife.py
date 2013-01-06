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
BACKGROUNDCOLOUR=(0,0,0)
TICKRATE=20

#SET size of cells in pixels

UNITSIZE=5

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
            #if in end of array, loop around and check index 0
                if x==self.sizex-1 and y==self.sizey-1:
                    if self.previous[x-1][y]:
                        besideCellsAlive+=1
                    if self.previous[x-1][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x-1][0]:   
                        besideCellsAlive+=1
                    if self.previous[x][y-1]:   
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
                    if self.previous[x-1][0]:   
                        besideCellsAlive+=1
                    if self.previous[x][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x][0]:   
                        besideCellsAlive+=1
                    if self.previous[x+1][y]:
                        besideCellsAlive+=1
                    if self.previous[x+1][y-1]:   
                        besideCellsAlive+=1
                    if self.previous[x+1][0]:   
                        besideCellsAlive+=1
                else:
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
                    if self.previous[x+1][y]:
                        besideCellsAlive+=1
                    if self.previous[x+1][y-1]:   
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
    game.nexttick()
    #draw the shit
    screen.fill(BACKGROUNDCOLOUR)
    for x in range (game.sizex):
        for y in range(game.sizey):
            if game.current[x][y]:
                pygame.draw.rect(screen,ALIVECOLOUR,pygame.Rect((x*UNITSIZE,y*UNITSIZE),(UNITSIZE,UNITSIZE)))
            elif not DEADCOLOUR==BACKGROUNDCOLOUR:
                pygame.draw.rect(screen,DEADCOLOUR,pygame.Rect((x*UNITSIZE,y*UNITSIZE),(UNITSIZE,UNITSIZE)))
    pygame.display.flip()
    tickingtime=clock.tick(TICKRATE)
#    if(int(game)>7000):               #debug 
#        game.generate(time.gmtime(),U.gridsize[0],U.gridsize[1])
#    print((1./tickingtime)*1000) #debug
#    print(int(game))              #debug
