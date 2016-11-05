# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from utils.ontologias import UMBEL, CRUZAR, GEOES, OWL
from rdflib.namespace import RDF, RDFS, FOAF
from utils.namespaces import rioFrio, geonames, dbpedia
from rutaMaiz.restaurantes import g

g.add( (URIRef(rioFrio), GEOES.formaParteDe, dbpedia['Riofrio,_Valle_del_Cauca']))
g.add( (URIRef(rioFrio), UMBEL.hasCharacteristic, rioFrio.Alojamientos ) )
g.add( (URIRef(rioFrio), UMBEL.hasCharacteristic, rioFrio.Eventos) )
g.add( (URIRef(rioFrio), UMBEL.hasCharacteristic, rioFrio.Fauna) )
g.add( (URIRef(rioFrio), UMBEL.hasCharacteristic, rioFrio.Flora) )
g.add( (URIRef(rioFrio), UMBEL.hasCharacteristic, rioFrio.Lugares) )
g.add( (URIRef(rioFrio), UMBEL.hasCharacteristic, rioFrio.Restaurantes) )
g.add( (URIRef(rioFrio), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rioFrio), RDFS.label, Literal("RIOFRÍO", lang="es")) )
g.add( (URIRef(rioFrio), RDFS.comment, Literal("""Por la carretera panorama se encuentra el municipio de Riofrío, 
su diversidad de pisos térmicos va de la mano con su topografía y orografía. Es conocido como una autentica reserva turística, por 
poseer los parajes más típicos del valle, riqueza ecológica y abundante fauna.""", lang="es")) )
g.add( (URIRef(rioFrio), FOAF.depiction, URIRef("http://i.imgur.com/2XEPrR1.jpg")) )

##Links de la ruta
g.add( (URIRef(rioFrio), OWL.sameAs, URIRef(geonames['3670754'])) ) #riofrio
g.add( (URIRef(rioFrio), OWL.sameAs, URIRef(geonames['3783081'])) ) #vda La Vigorosa

#print (g.serialize(format='pretty-xml'))

