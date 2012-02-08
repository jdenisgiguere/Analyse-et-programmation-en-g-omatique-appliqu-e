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


---------
Exercices
---------


