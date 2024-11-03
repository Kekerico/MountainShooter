#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from src.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from src.EnemyShot import EnemyShot
from src.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.speed_multiplier = 1    
        self.moving_up = True          

    def move(self):
        if self.name == 'Enemy3':
          
            if self.moving_up:
                self.rect.centery -= ENTITY_SPEED[self.name] * self.speed_multiplier
            else:
                self.rect.centery += ENTITY_SPEED[self.name] * self.speed_multiplier

        
            self.rect.centerx -= ENTITY_SPEED[self.name]

           
            if self.rect.top <= 0:  
                self.rect.top = 0  
                self.speed_multiplier = 2  
                self.moving_up = False     

            elif self.rect.bottom >= WIN_HEIGHT: 
                self.rect.bottom = WIN_HEIGHT  
                self.speed_multiplier = 1  
                self.moving_up = True      

        
        if self.name != 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
