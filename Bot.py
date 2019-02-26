#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import uuid

class Bot:
    def __init__(self, health):
        self.age = 0
        self.botAround = 0
        self.foodAround = 0
        self.health = health
        self.id = uuid.uuid4()

    def setMap(self, map):
        self.__map = map

    def move(self, x, y):
        if self.isAlive() and self.__map:
            self.__x += x
            self.__y += y
            # Le bot ne doit pas sortir de la map
            if self.__x < 0:
                self.__x = 0
            elif self.__x >= self.__map.width:
                self.__x = self.__map.width - 1
            if self.__y < 0:
                self.__y = 0
            elif self.__y >= self.__map.height:
                self.__y = self.__map.height - 1
            self.endTurn()

    def goNorth(self):
        self.move(0,-1)

    def goSouth(self):
        self.move(0,1)

    def goEast(self):
        self.move(1,0)

    def goWest(self):
        self.move(-1,0)

    def eat(self):
        if self.__map and self.isAlive():
            food = self.__map.getFood(self.getPosition())
            if food > 0:
                self.health += food
            self.endTurn()

    def endTurn(self):
        if self.isAlive():
            self.age += 1
            self.health -= 1
            self.getInformationsAround()
        return self.age

    def isAlive(self):
        return self.health > 0

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getPosition(self):
        return (self.__x, self.__y)

    def countNorthFood(self):
        zone = self.__map.getNorthZone(self.__x, self.__y)
        return self.__map.countFoodBetween(*zone)

    def countEastFood(self):
        zone = self.__map.getEastZone(self.__x, self.__y)
        return self.__map.countFoodBetween(*zone)

    def countSouthFood(self):
        zone = self.__map.getSouthZone(self.__x, self.__y)
        return self.__map.countFoodBetween(*zone)

    def countWestFood(self):
        zone = self.__map.getWestZone(self.__x, self.__y)
        return self.__map.countFoodBetween(*zone)

    def countNorthBot(self):
        zone = self.__map.getNorthZone(self.__x, self.__y)
        return self.__map.countBotBetween(*zone)

    def countEastBot(self):
        zone = self.__map.getEastZone(self.__x, self.__y)
        return self.__map.countBotBetween(*zone)

    def countSouthBot(self):
        zone = self.__map.getSouthZone(self.__x, self.__y)
        return self.__map.countBotBetween(*zone)

    def countWestBot(self):
        zone = self.__map.getWestZone(self.__x, self.__y)
        return self.__map.countBotBetween(*zone)

    def getInformationsAround(self):
        x1 = self.__x - 1
        if x1 < 0:
            x1 = self.__x
        y1 = self.__y - 1
        if y1 < 0:
            y1 = self.__y
        x2 = self.__x + 1
        if x2 >= self.__map.width:
            x2 = self.__x
        y2 = self.__y + 1
        if y2 >= self.__map.height:
            y2 = self.__y
        
        bot = self.__map.countBotBetween(x1, y1, x2, y2) - 1
        food = self.__map.countFoodBetween(x1, y1, x2, y2)
        
        self.botAround = bot
        self.foodAround = food

    def canEatFood(self):
        pos = self.getPosition()
        food = self.__map.countFoodBetween(*pos, *pos)
        return 1 if food else 0

    def getDict(self):
        return {
            "age": self.age,
            "health": self.health,
            "x": self.__x,
            "y": self.__y,
            "id": str(self.id)
        }

    def getScore(self):
        return {
            "age": self.age,
            "id": str(self.id)
        }