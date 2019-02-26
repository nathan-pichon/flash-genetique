#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import logging

from Map import Map
from CleverBot import CleverBot

MAX_GEN = 2000

print('start')

"""for gene in bot.genes:
    print('Gene:')
    print('- Input', gene.input)
    print('- Weight', gene.weight)
    print('- Output', gene.output)
    print('Activated', gene.active)"""

from Generation import Generation

oldGen = None
i = 0

while i < MAX_GEN:
    i += 1
    gen = Generation()
    if oldGen:
        gen.setPopulation(oldGen.getNextGeneration())
    else:
        gen.generateFirstPopulation()
    gen.start()
    oldGen = gen
f = open( 'generation'+ str(gen.id) +'.json', 'w' )
f.write( repr(gen.getDict()) )
f.close()

# gen = Generation()

# gen.generateFirstPopulation()

# print('crossover', len(gen.crossover()))
# print('nextGen', len(gen.getNextGeneration()))

# gen.start()
# print(gen.tournamentSelector(5))

"""
f = open( 'generation.json', 'w' )
f.write( repr(gen.getDict()) )
f.close()
# """

