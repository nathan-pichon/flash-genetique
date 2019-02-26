#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import random
import json
import math

class Map:
    foodValue = 50
# Initilisation de la map avec une largeur et une hauteur (en case de jeu)
    def __init__(self, file):
        self.__listBot = []
        self.loadMap(file)

# Ajouter un bot à la map
    def addBot(self, bot):
        self.__listBot.append(bot)
        rand = random.randint(1, self.width * self.height - 1)
        bot.setX(rand % self.width)
        bot.setY(math.floor(rand / self.width))
        bot.setMap(self)

# Chargement d'une map JSON à partir d'un chemin fichier
    def loadMap(self, file):
        data = open(file, "r")
        self.__mapData = json.loads(data.read())
        self.map = self.__mapData['data'].copy()
        self.width = self.__mapData['width']
        self.height = self.__mapData['height']

# Permet de remettre à zéro la map
    def resetMap(self):
        if self.__mapData:
            self.map = self.__mapData.copy()
        del self.__listBot[:]

# Récupération de la nourriture sur la case donnée par pos
    def getFood(self, pos):
        lines = pos[1] * self.width
        index = pos[0] + lines
        food = 0
        if self.map[index] == 1:
            food = self.foodValue
            self.map[index] = 0
        return food

# Compte le nombre de Bot présents dans la zone donnée
    def countBotBetween(self, x1, y1, x2, y2):
        counter = 0
        for bot in self.__listBot:
            pos = bot.getPosition()
            if pos[0] >= x1 and pos[0] <= x2 and pos[1] >= y1 and pos[1] <= y2:
                counter += 1
        return counter

# Compte le nombre de nourriture dans la zone donnée
    def countFoodBetween(self, x1, y1, x2, y2):
        if x1 > x2 :
            tmp = x1
            x1 = x2
            x2 = tmp
        if y1 > y2 :
            tmp = y1
            y1 = y2
            y2 = tmp

        if x2 >= self.width or y2 >= self.height:
            raise MapError("Out of range", "X must be between lower than " + str(self.width) + ", Y must be lower than " + str(self.height) + ".")

        counter = 0
        currPos = [x1, y1]
        while currPos[0] <= x2 and currPos[1] <= y2:
            lines = currPos[1] * self.width
            counter += self.map[currPos[0] + lines]
            currPos[0] += 1
            if currPos[0] > x2 and currPos[1] < y2:
                currPos[0] = x1
                currPos[1] += 1
        return counter

# Récupération de la zone au nord d'une coordonnée x/y
    def getNorthZone(self, x, y):
        return (0, 0, self.width-1, y)

# Récupération de la zone au sud d'une coordonnée x/y
    def getSouthZone(self, x, y):
        return (0, y, self.width-1, self.height-1)

# Récupération de la zone à l'est d'une coordonnée x/y
    def getEastZone(self, x, y):
        return (x, 0, self.width-1, self.height-1)

# Récupération de la zone à l'ouest d'une coordonnée x/y
    def getWestZone(self, x, y):
        return (0, 0, x, self.height-1)
    
    def getDict(self):
        return {
            "data": self.map,
            "width": self.width,
            "height": self.height
        }

class MapError(Exception): 
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message