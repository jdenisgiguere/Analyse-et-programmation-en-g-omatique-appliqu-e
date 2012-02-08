Les fonctions
=============


Les fonctions constituent un élément fondamental pour
l'organisation interne du code source.

----------
Fondements
----------

La syntaxe générale est: ::

    def nom_de_fonction( parametre1, ..., parametreN ):
        bloc d'instructions
        
        ...
        
        return(valeur)

La fonction ne possède pas obligatoirement de paramètres.

.. code-block:: python

    def bonjour():
        print "Bonjour!"


Elle devient toutefois bien plus utile lorsque
des paramètres sont utilisés et qu'une valeur est retournée.


.. code-block:: python

    def aire_rectangle(largeur, hauteur):
        aire = largeur * hauteur
        return aire


--------------
Espace de noms
--------------

En programmation, une variable peut prendre différentes
valeurs dans des contextes différents.
L'*espace de noms* décrit un environnement de ces environnements.::

    >>> base = 20.0
    >>> profondeur = 30.0
    >>> superficie = aire_rectangle(base, profondeur)
    >>> print superfie
    600.0
    >>> print aire
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    
    <python console> in <module>()

    NameError: name 'aire' is not defined

Ici, ``aire`` est définie uniquement dans l'espace de noms de
la fonction  ``aire_rectangle``.


-----------------------------------------
Utilisation d'une fonction dans un script
-----------------------------------------

.. literalinclude:: exemples/aire_sphere.py

---------------------
Paramètres par défaut
---------------------

Il arrive à l'occasion qu'une fonction possède un paramètre
dont la valeur est régulièrement la même. 

.. code-block:: python

    def point(x, y, z=0.0):
        return {'x':x, 'y':y, 'z':z}

De cette façon, on pourra créer un dictionnaire de coordonnées
sans spécifier explicitement l'altitude si elle n'est pas
considérée. ::

    >>> point1 = point(2.0, 3.2, 12.0)
    >>> point2 = point(4.0, -3.0)
    >>> print point1
    {'y': 3.2, 'x': 2.0, 'z': 12.0}
    >>> print point2
    {'y': -3.0, 'x': 4.0, 'z': 0.0}


---------
Exercices
---------

NDVI
####

#. Créez la fonction ``ndvi``. Celle-ci reçoit deux
   compte numérique en paramètre.



