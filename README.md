# flash-genetique

## ENGLISH

## Demo
The purpose of this demo is to show with an visible application the principle of genetic algorithm.

### Detail
#### Definition of an individual

##### Rules
- An individual is a bot capable to survive x turns.
- He can gather points of food on the map where he grow.
- A point of food expand his lifespan by x turns(constant to be define)
- TODO : He can eat his opponents (Experiment Point system with food, he can only eat bots with less XP)

##### Caracteristics and possible actions
- age : nbr of turns that the bot survive
- position : x and y on the map
- movements (action) : north, east, south, west
- eat (action) : Eat the food available on his position
- do nothing (action)

##### Inputs
- Age
- Number of food in the North
- Number of food in the East
- Number of food in the South
- Number of food in the West
- Number of bots near him (+/- 1 range)
- Number of food available near him (+/- 1 range)
- Is there a food on his position ? (boolean)

#### Definition of a gene
A gene will be represented by those informations:
- An input
- A weight
- An action

#### Neural Network
Each gene will allow to calculate the total weight of the actions (Input x Weight)

The heavier action will be executed.



## FRENCH

## Démonstration
Le but de cette démonstration est de montrer une application visible de ce qu'est le principe d'un algorithme génétique.

### Détail
#### Définition d'un individu

##### Règles
- Un individu est un bot capable de survivre n tours.
- Il peut récupérer des points de nourriture sur la carte dans laquelle il évolue.
- Un point de nourriture augmente sa durée de vie de x tours (constante à définir)
- TODO: Il peut ingérer un bot adverse (système d'xp grâce à la nourriture, un bot de niveau égal ou supérieur ne peut être ingéré)

##### Caractéristiques et actions possibles
- age : nombre de tour où le bot a vécu
- position : x et y sur la map
- déplacement (action) : nord, est, sud, ouest
- manger (action) : Mange la nourriture disponible sur sa case
- ne rien faire (action) : passe son tour

##### Inputs
- Age
- Nombre de nourriture au Nord
- Nombre de nourriture à l'Est
- Nombre de nourriture au Sud
- Nombre de nourriture à l'Ouest
- Nombre de bot l'entourant (+/- 1 de distance)
- Nombre de nourriture l'entourant (+/- 1 de distance)
- Est-ce qu'une nourriture se trouve à son emplacement ? (boolean)

#### Définition d'un gène
Un gène représentera 3 informations:
- Un input
- Un poids
- Une action

#### Réseau neuronal
Chaque gène permettra de calculer le poid total des actions (Input x Poids)

L'action recevant le plus de points sera réalisée.




