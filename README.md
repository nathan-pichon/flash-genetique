# flash-genetique

## Démonstration
Le but de cette démonstration est de montrer une application visible de ce qu'est le principe d'un algorithme génétique.

### Détail
#### Définition d'un individu

##### Règles
- Un individu est un bot capable de survivre n tours.
- Il peut récupérer des points de nourriture sur la carte dans laquelle il évolue.
- Un point de nourriture augmente sa durée de vie de x tours (constante à définir)
- Bonus si le temps: Il peut ingérer un bot adverse (système d'xp grâce à la nourriture, un bot de niveau égal ou supérieur ne peut être ingéré)

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




