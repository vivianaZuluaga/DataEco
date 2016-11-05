#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rutaVueltaOriente.restaurantesVueltaOriente import g
#from utils.metadatos import g

print (g.serialize(format="pretty-xml"))
#print rutaJardin
