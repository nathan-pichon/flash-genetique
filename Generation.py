#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import random
from enum import Enum
from operator import attrgetter
import math

from CleverBot import CleverBot
from Map import Map


class Generation:
    generationNumber = 1
    populationNumber = 100
    nbrOfParents = 5
    mutatingRate = 1
    defaultHealth = 30

    def __init__(self):
        self.id = Generation.generationNumber
        Generation.generationNumber += 1
        # self.mapFile = "map" + str(random.randrange(1, 3)) + ".json"
        self.mapFile = "map-test.json"
        self.map = Map(self.mapFile)
        self.population = []
        self.rounds = []

    def generateFirstPopulation(self):
        while len(self.population) != self.populationNumber:
            bot = CleverBot(self.defaultHealth)
            self.map.addBot(bot)
            bot.setupRandGenes()
            self.population.append(bot)
    
    def setPopulation(self, population):
        self.population = population[:self.populationNumber]
        for bot in self.population:
            self.map.addBot(bot)

# Démarre l'évaluation des bots
    def start(self):
        print('Generation ' + str(self.id) + ' started')
        self.rounds.append(self.getStats())
        while self.isABotAlive():
            for bot in self.population:
                if bot.isAlive():
                    bot.doSomething()
            self.rounds.append(self.getStats())
        print('Max round', len(self.rounds))
        print('Generation ' + str(self.id) + ' finished')

# Est-ce que le bot est encore vivant ?
    def isABotAlive(self):
        return next((x for x in self.population if x.isAlive()), False)

# Génère une population à partir de la population de l'actuel génération
    def getNextGeneration(self):
        population = self.crossover()
        for bot in population:
            if random.randrange(100) <= self.mutatingRate:
                bot.mutate()
        rest = self.populationNumber - len(population)
        while rest > 0:
            bot = CleverBot(self.defaultHealth)
            bot.setupRandGenes()
            population.append(bot)
            rest -= 1
        return population

# Croisement entre les parents de la génération actuelle
    def crossover(self):
        population = []
        parents = self.selectParents(self.nbrOfParents)
        parentsLeftToCross = parents.copy()
        for parent1 in parents:
            parentsLeftToCross.pop(0)
            for parent2 in parentsLeftToCross:
                population.append(self.onePointCrossover(parent1, parent2))
                population.append(self.multiPointCrossover(parent1, parent2))
        return population + parents

# Croisement des gènes des deux parent sur un seul axe
    def onePointCrossover(self, parent1, parent2):
        point = random.randrange(1, len(parent1.genes) - 1)
        child = CleverBot(self.defaultHealth)
        child.copyGenes(parent1.genes[:point] + parent2.genes[point:])
        return child

# Croisement des gènes des deux parent sur deux axes
    def multiPointCrossover(self, parent1, parent2):
        pointMaxLength = math.floor((len(parent1.genes) - 1) / 2)
        child = CleverBot(self.defaultHealth)
        point1 = random.randrange(1, pointMaxLength)
        point2 = point1 + random.randrange(1, pointMaxLength)
        if random.randrange(1,2) == 1:
            child.copyGenes(parent1.genes[:point1] + parent2.genes[point1:point2] + parent1.genes[point2:])
        else:
            child.copyGenes(parent2.genes[:point1] + parent1.genes[point1:point2] + parent2.genes[point2:])
        return child


# Sélection des parents pour les croisements et génération de la nouvelle population
    def selectParents(self, nbr):
        selector = Selector(random.randrange(1, 4))
        print(selector)
        if selector == Selector.RANDOM:
            return self.randomSelector(nbr)
        if selector == Selector.RANK:
            return self.rankSelector(nbr)
        if selector == Selector.ROULETTE_WHEEL:
            return self.rouletteSelector(nbr)
        if selector == Selector.STOCHASTIC:
            return self.stochasticSelector(nbr)
        if selector == Selector.TOURNAMENT:
            return self.tournamentSelector(nbr)

# Sélectionne aléatoirement des parents
    def randomSelector(self, nbr):
        return random.sample(self.population, nbr)
    
# Sélectionne l'élite des parents
    def rankSelector(self, nbr):
        sort = sorted(self.population, key=lambda bot: bot.age)
        return sort[:nbr]

# Sélectionne des parents grâce à la méthode de la roulette
    def rouletteSelector(self, nbr):
        result = []

        for i in range(nbr):
            sum = 1
            for bot in self.population:
                sum += bot.age - self.defaultHealth
            fixedPoint = random.randrange(0, sum) - 1
            sum = 0
            for bot in self.population:
                sum += bot.age - self.defaultHealth
                if sum > fixedPoint:
                    result.append(bot)
                    break

        return result

# Sélectionne les parents comme la méthode de la roulette mais avec une sélection de tous les parents en un tour de roue
    def stochasticSelector(self, nbr):
        result = []
        fixedPoints = []

        max = 0
        for bot in self.population:
            max += bot.age - self.defaultHealth
        for i in range(nbr):
            fixedPoints.append(0 if max == 0  else random.randrange(max))
        fixedPoints.sort()
        sum = 0
        currentPoint = 0
        for bot in self.population:
            sum += bot.age - self.defaultHealth
            while currentPoint < nbr and sum >= fixedPoints[currentPoint]:
                result.append(bot)
                currentPoint += 1
            if currentPoint >= nbr:
                break
        return result

# Sélection des parents par tournoi
    def tournamentSelector(self, nbr):
        result = []
        for i in range(nbr):
            sample = random.sample(self.population, random.randrange(2, self.populationNumber))
            result.append(sorted(sample, key=lambda bot: bot.age)[0])
        return result

    def getStats(self):
        return {
            "map": self.map.getDict(),
            "bots": list(map(lambda bot: bot.getDict(), filter(lambda bot: bot.isAlive(), self.population))),
            "leaderboard": sorted(map(lambda bot : bot.getScore(), self.population), key=lambda bot : bot['age'])
        }


    def getDict(self):
        return {
            'id': self.id,
            'rounds': self.rounds
        }

class Selector(Enum):
    ROULETTE_WHEEL = 1
    STOCHASTIC = 2
    TOURNAMENT = 3
    RANK = 4
    RANDOM = 5