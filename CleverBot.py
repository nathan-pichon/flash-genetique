#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import random
import operator
from enum import Enum

from Bot import Bot
class CleverBot(Bot):
    minGenes = 35
    def __init__(self, health):
        super().__init__(health)
        self.genes = []
    
# Génère aléatoirement les gènes
    def setupRandGenes(self):
        del self.genes[:]
        for input in Input:
            for output in Output:
                self.genes.append(Genes(input, output))
        self.activateRandGenes(self.minGenes)
    
    def copyGenes(self, genes):
        for gene in genes:
            newOne = Genes(gene.input, gene.output, weight=gene.weight)
            newOne.active = gene.active
            self.genes.append(newOne)

# Lance une mutation aléatoire
    def mutate(self):
        method = Mutation(random.randrange(1,5))
        print(method)
        if method == Mutation.FLIP:
            self.flipMutation()
        elif method == Mutation.INVERT:
            self.invertMutation()
        elif method == Mutation.RESET:
            self.resetMutation()
        elif method == Mutation.SWAP:
            self.swapMutation()
        elif method == Mutation.SCRAMBLE:
            self.scrambleMutation()

# Echange aléatoirement plusieurs gènes
    def scrambleMutation(self):
        nbrOfScramble = random.randrange(1, len(self.genes))
        genes = random.sample(self.genes, nbrOfScramble)
        random.shuffle(genes)
        weights = list(map(lambda gene: gene.weight, genes))
        for i in range(nbrOfScramble):
            genes[i].weight = weights[i]

# Inversion de plusieurs gènes
    def invertMutation(self):
        nbrOfInvert = random.randrange(1, len(self.genes))
        genes = random.sample(self.genes, nbrOfInvert)
        weights = list(map(lambda gene: gene.weight, genes))
        weights.reverse()
        for i in range(nbrOfInvert):
            genes[i].weight = weights[i]

# Remet à zéro un gène (random sur le poid)
    def resetMutation(self):
        gene = random.choice(self.genes)
        gene.randomWeight()

# Echange les poids entre deux gènes
    def swapMutation(self):
        genes = random.sample(self.genes, 2)
        weight = genes[0].weight
        genes[0].weight = genes[1].weight
        genes[1].weight = weight

# Active/Désactive un gène aléatoire
    def flipMutation(self):
        gene = random.choice(self.genes)
        if (gene.active):
            gene.deactivate()
        else:
            gene.activate()

# Active aléatoirement des gènes
    def activateRandGenes(self, nbr):
        genes = list(filter(lambda gene: not gene.active, self.genes))
        if len(genes):
            genes = random.sample(genes, nbr)
            for gene in genes:
                gene.activate()

# Désactive aléatoirement des gènes
    def deactivateRandGenes(self, nbr):
        genes = list(filter(lambda gene: gene.active, self.genes))
        if len(genes):
            genes = random.sample(genes, nbr)
            for gene in genes:
                gene.deactivate()

# Remplace un gène par celui donné
    def replaceGene(self, gene): 
        for currentGene in self.genes:
            if currentGene.input == gene.input and currentGene.output == gene.output:
                currentGene.copy(gene)
                break

# Effectue une action en fonction des gènes
    def doSomething(self):
        score = {
            Output.EAT: 0,
            Output.NORTH: 0,
            Output.EAST: 0,
            Output.SOUTH: 0,
            Output.WEST: 0,
            Output.STAY: 0
        }
        for gene in filter(lambda x: x.active, self.genes):
            score[gene.output] += self.getValueOfInput(gene.input) * gene.weight
        action = max(score.items(), key=operator.itemgetter(1))[0]
        self.doAction(action)
    
# Execute l'action donnée en paramètre
    def doAction(self, action):
        if action == Output.EAT:
            return self.eat()
        elif action == Output.NORTH:
            return self.goNorth()
        elif action == Output.EAST:
            return self.goEast()
        elif action == Output.SOUTH:
            return self.goSouth()
        elif action == Output.WEST:
            return self.goWest()
        elif action == Output.STAY:
            return self.endTurn()
        
# Récupération de la valeur correspondant à l'input donné en paramètre
    def getValueOfInput(self, input):
        if input == Input.HEALTH:
            return self.health
        if input == Input.NORTHFOODS:
            return self.countNorthFood()
        if input == Input.EASTFOODS:
            return self.countEastFood()
        if input == Input.SOUTHFOODS:
            return self.countSouthFood()
        if input == Input.WESTFOODS:
            return self.countWestFood()
        if input == Input.FOODAROUND or input == Input.BOTAROUND:
            self.getInformationsAround()
            if input == input == Input.BOTAROUND:
                return self.botAround
            if input == Input.FOODAROUND:
                return self.foodAround
        if input == Input.FOODHERE:
            return self.canEatFood()

class Mutation(Enum):
    SCRAMBLE = 1
    FLIP = 2
    INVERT = 3
    RESET = 4
    SWAP = 5

class Input(Enum):
    HEALTH = 1
    BOTAROUND = 2
    FOODAROUND = 3
    NORTHFOODS = 8
    EASTFOODS = 9
    SOUTHFOODS = 10
    WESTFOODS = 11
    FOODHERE = 12

class Output(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    EAT = 5
    STAY = 6

class Genes:
    minWeight = 1
    maxWeight = 1000
    def __init__(self, input, output, *pos, **args):
        self.input = input
        if 'weight' in args:
            self.weight = args['weight']
        else:
            self.randomWeight()
        self.output = output
        self.active = False

# active le gène
    def activate(self):
        self.active = True

# désactive le gène
    def deactivate(self):
        self.active = False

# défini un poids aléatoire pour le gen compris entre les MIN et MAX    
    def randomWeight(self):
        self.weight = random.randrange(self.minWeight, self.maxWeight) / 100

# copy le gène donné
    def copy(self, gene):
        self.weight = gene.weight
        self.active = gene.active