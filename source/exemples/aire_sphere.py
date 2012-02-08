# -*- coding: utf-8 -*-
"""
Script retournant l'aire d'une sphère

Usage: aire_sphere.py <rayon>
"""

import sys
from math import pi

def aire_sphere(rayon):
    """
    aire d'une sphère

    .. math::
        aire = 4 * \pi * rayon ^ 2

    """
    aire = 4 * pi * rayon ** 2

    return aire

if __name__ == '__main__':
    rayon = float(sys.argv[1])

    aire_sphere = aire_sphere(rayon)

    print "L'aire de la sphère est", aire_sphere

    sys.exit(0)
