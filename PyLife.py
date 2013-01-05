#!/usr/bin/python3
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

#SET size of cells in pixels

UNITSIZE=10

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
	def __init__ (self):
        self.current[][]=0
        self.previous[][]=0
    def __str__ (self):
        alive=0
        #if we try to print this, give number of alive cells
        for x in range(len(self.current):
            for y in self.current[x]:
                if y==1:
                    alive+=1
        return str(alive)
    def generate(seed, sixex,sixey):
        random.seed(seed)
        self.sixex=sixex
        self.sizey=sizey
        for x in range(sixex):
            for y in range(sixey):
                self.current[x][y]=random.randint(0,1)
    def nexttick:
        #run with go-through borders
        self.previous=self.current
        for x in range(self.sixex):
            for y in range(self.sixey):
            besideCellsAlive=0
            #if in end of array, loop around and check index 0
                if x==self.sixex-1 && y==self.sixey-1:
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
                elif x==self.sixex-1:
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
                elif y==self.sixey-1:
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
                elif besideCellsAlive==2 && self.current[x][y]==1:
                    self.current[x][y]=1
    
