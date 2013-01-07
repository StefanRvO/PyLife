#!/usr/bin/python2
#Conway's game of Life written in python. For more info, see the README

import pygame
from pygame.locals import *
import time
import random
from sys import exit
import math
import inputbox

#Set screensize
SCREENSIZE=(1300,700)

#Set colour of the cells
ALIVECOLOUR=(255,255,255)
DEADCOLOUR=(0,0,0)
DEADCOLOUR=BACKGROUNDCOLOUR=(17,20,70)
TICKRATE=5
GOTHROUGH=1
PrevTICKRATE=0
Changed=0
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
    def __init__(self):
        self.generation=0
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
        self.generation=0
        self.current = [[0]*sizey for i in range(sizex)]
        #self.previous=self.current[:][:]
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
        self.generation+=1
        pygame.display.set_caption("Seed="+str(gameseed)+", Generation="+str(self.generation)+", Gridsize= ("+ str(U.gridsize[0])+" x "+str(U.gridsize[1])+")")


        self.bufferlist = [[0]*self.sizey for i in range(self.sizex)]
        for x in range(self.sizex):
            for y in range(self.sizey):
                #if not self.previous[x][y]==0:
                #    print (self.previous[x][y])
                if not GOTHROUGH:
                    #add to all neighbour cells if we are alive
                    if self.current[x][y]:
                        if not x==self.sizex-1:
                            self.bufferlist[x+1][y]+=1
                            if not y==self.sizey-1:
                                self.bufferlist[x+1][y+1]+=1
                            if not y==0:
                                self.bufferlist[x+1][y-1]+=1
                        if not x==0:
                            self.bufferlist[x-1][y]+=1
                            if not y==self.sizey-1:
                                self.bufferlist[x-1][y+1]+=1
                            if not y==0:
                                self.bufferlist[x-1][y-1]+=1
                        if not y==self.sizey-1:
                            self.bufferlist[x][y+1]+=1
                        if not y==0:
                            self.bufferlist[x][y-1]+=1
                else:
                    #if GOTHROUGH
                    if self.current[x][y]==1:
                        self.bufferlist[x][y-1]+=1  
                        self.bufferlist[x-1][y-1]+=1
                        self.bufferlist[x-1][y]+=1
                        if not y==self.sizey-1:
                            self.bufferlist[x-1][y+1]+=1
                            self.bufferlist[x][y+1]+=1
                            if not x==self.sizex-1:
                                self.bufferlist[x+1][y+1]+=1
                            else:
                                self.bufferlist[0][y+1]+=1
                        else:
                            self.bufferlist[x-1][0]+=1
                            self.bufferlist[x][0]+=1
                            if not x==self.sizex-1:
                                self.bufferlist[x+1][0]+=1
                            else:
                                self.bufferlist[0][0]+=1
                        if not x==self.sizex-1:
                            self.bufferlist[x+1][y]+=1
                            self.bufferlist[x+1][y-1]+=1
                        else:
                            self.bufferlist[0][y]+=1
                            self.bufferlist[0][y-1]+=1
                            
        for x in range(self.sizex):
            for y in range(self.sizey):
                if self.bufferlist[x][y]==3:
                    self.current[x][y]=1
                elif self.bufferlist[x][y]==2:
                    self.current[x][y]=self.current[x][y]
                elif self.bufferlist[x][y]<=1:
                    self.current[x][y]=0
                elif self.bufferlist[x][y]>=4:
                    self.current[x][y]=0

                
                
                        
    def changeCell(self,cords):
        #Get coordinates in grid by deviding with unit size and round down
        x=int(float(cords[0])/U.x)
        y=int(float(cords[1])/U.y)
        self.current[x][y] = not self.current[x][y]

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
gameseed=random.randint(0,time.mktime(time.gmtime()))   #this seed is hopefully suficiently random

game.generate(gameseed,U.gridsize[0],U.gridsize[1])

#Gameloop
while 1:
    #generate next generation
    if not TICKRATE==0:
        game.nexttick()
        DrawNext=1

     #event loop for controls
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        elif event.type==KEYDOWN:
            #Control speed on left and right
            if event.key==K_LEFT and TICKRATE>0:
                TICKRATE-=1
            if event.key==K_RIGHT and TICKRATE>-1:
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
            if event.key==K_w:
                GOTHROUGH=not GOTHROUGH
            if event.key==K_f:
                game.nexttick()
                DrawNext=1
            if event.key==K_UP:
                gameseed=random.randint(0,time.mktime(time.gmtime()))
                game.generate(gameseed,U.gridsize[0],U.gridsize[1])
                Changed=0
                DrawNext=1
            if event.key==K_DOWN:
                game.current = [[0]*game.sizey for i in range(game.sizex)]
                gameseed="BLANK"
                game.generation=0
                DrawNext=1
            if event.key==K_s:
                gameseed = inputbox.ask(screen, "Enter a seed to start from")
                game.generate(gameseed,U.gridsize[0],U.gridsize[1])
                DrawNext=1
                Changed=0

                
                
        #Mousecontrols
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                game.changeCell(event.pos)
                DrawNext=1
                if not Changed:
                    gameseed="Board Changed. Original seed was: "+str(gameseed)+" Changed at generation "+str(game.generation)
                    Changed=1


    #Do not draw if board is paused. Except if forced by some event
    if not TICKRATE==0 or DrawNext==1:
        DrawScreen()
        DrawNext=0
    if not TICKRATE==0:
        tickingtime=clock.tick(TICKRATE)
    else:
        tickingtime=clock.tick(10) #Only run with 10 loops per second if paused. Should be enough

#    if(int(game)>7000):               #debug
#        game.generate(time.gmtime(),U.gridsize[0],U.gridsize[1])
#    print((1./tickingtime)*1000) #debug
#    print(TICKRATE)
#    print(int(game))              #debug
