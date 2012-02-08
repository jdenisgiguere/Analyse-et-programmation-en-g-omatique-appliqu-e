===========
Les classes
===========

Lorsque la complexité d'un logiciel augmente, il devient
nécessaire d'identifier de stratégie pour gérer cette complexité.
Les classes constituent un outil privilégiées pour cela.

------------
Introduction
------------

La classe représente un gabarit qui pourra être utilisée pour
décrire des entités similaires. Les caractéristiques de ces entités
seront stockées dans des variables qu'on appelle attributs et
des fonctions qu'on appelle méthodes.

.. code-block:: python

    class Point:
        "point 2D"


Le mot réservé ``class`` débute la déclaration d'une fonction.
La classe est délimitée par un bloc.

--------------
Initialisation 
--------------

Un point possède deux attributs élémentaire:
un abscisse et une ordonnée.
On peut les créer assez simplement ::

    >>> p = Point()
    >>> p.x = 1.0
    >>> p.y = 2.0

Cette approche nous placera rapidement devant certaines limitations.
On préférera donc créer une fonction d'initialisation.

.. code-block:: python

    class Point:
        "point 2D"

        def __init__(self, x, y):
            """
            Arguments:
            x -- abscisse
            y -- ordonnée
            """
            self.x = x
            self.y = y
    

La classe ``Point`` possède maintenant une fonction particulière pour
son initialisation : ``__init__``. Comme la fonction
fait partie d'une classe, on l'appelle méthode.
Par convention, le premier argument d'une méthode est ``self``.
Cette argument représente l'entité de la classe qui est
considérée. La méthode d'initialisation permet, entre autres,
de donner les attributs par défaut d'une classe. ::

    >>> point1 = Point(1.0,2.0)
    >>> print point1.x
    1.0
    >>> print point1.y
    2.0

----------------------------------
Représentation simple d'une entité
----------------------------------

Une autre méthode particulière est la méthode ``__str__``.
Cette méthode permet de spécifier une chaîne de caractères
qui représente une entité de la classe.

.. code-block:: python

    class Point:
        "point 2D"

        def __init__(self, x, y):
            """
            Arguments:
            x -- abscisse
            y -- ordonnée
            """
            self.x = x
            self.y = y

        def __str__(self):
            return "(%f, %f)" % (self.x, self.y)


Ce qui permet d'obtenir un affichage de cette nature ::

    >>> p = Point(1.1, 2.0)
    >>> print p
    (1.100000, 2.000000)


-------------------
Des méthodes utiles
-------------------



.. code-block:: python

    import math

    class Point:
        "point 2D"

        def __init__(self, x, y):
            """
            Arguments:
            x -- abscisse
            y -- ordonnée
            """
            self.x = x
            self.y = y

        def __str__(self):
            return "(%f, %f)" % (self.x, self.y)

        def distance(self, point):
            """
            Distance entre deux points
            """
            distance_carree = (self.x - point.x)**2 + (self.y - point.y)**2
            distance = math.sqrt(distance_carree)
            return distance

Cette méthode s'utilise ainsi ::

    >>> p1 = Point(0, 0)
    >>> p2 = Point(10, 0)
    >>> distance = p1.distance(p2)
    >>> print distance
    10.0

---------
Exercices
---------

La classe ligne
################

#. Proposez une classe ligne décrivant une ligne passant par
   deux points.
#. Créez une méthode qui calcule la distance entre cette ligne
   et un point.


