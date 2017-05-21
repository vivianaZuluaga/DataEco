#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rutaVueltaOriente.restaurantesVueltaOriente import g
#from utils.metadatos import g

"""[summary]
[description] Genera el grafo que describe a las rutas ecoturísticas del 
municipio de Tuluá y al municipio de Riofrío
"""
print (g.serialize(format="pretty-xml"))
