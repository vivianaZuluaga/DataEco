#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import UMBEL, CRUZAR, GEOES, OWL
from utils.namespaces import rutaAnillo, geonames, dbpedia 
from Riofrio.restaurantesRiofrio import g


g.add( (URIRef(rutaAnillo['descripcion.rdf']), GEOES.formaParteDe, dbpedia.Tulua))
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Alojamientos.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Empresas.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Eventos.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Fauna.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Flora.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Lugares.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), UMBEL.hasCharacteristic, rutaAnillo['Restaurantes.rdf']) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rutaAnillo['descripcion.rdf']), RDFS.label, Literal("RUTA ANILLO AGRÍCOLA", lang="es")) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), RDFS.comment, Literal("""Se inicia en la capilla del Santo Aparecido, a tan solo 80 metros del 
supermercado Comfandi Chiminangos, por la vía que conduce al corregimiento de Tres Esquinas. El turista tendrá la oportunidad 
de conocer una escultura conservada hace más de 100 años, con una importante tradición oral relativa a los milagros que ha 
concedido a sus creyentes. Continuando por la vía se adentrará en el poblado de Tres Esquinas posteriormente llegará a La 
Palmera, Bocas de Tuluá, La Caballera y conectará con la vía que conduce finalmente al corregimiento de Nariño. Este último 
tramo es comúnmente denominado el Anillo Agroturístico.""", lang="es")) )
g.add( (URIRef(rutaAnillo['descripcion.rdf']), FOAF.depiction, URIRef("http://i.imgur.com/LHjqsqt.jpg")) )

##Links de la ruta
g.add( (URIRef(rutaAnillo['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3666759'])) ) #Tres esquinas
g.add( (URIRef(rutaAnillo['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3782980'])) ) #La Palmera
g.add( (URIRef(rutaAnillo['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3688714'])) ) #Bocas de Tulua
g.add( (URIRef(rutaAnillo['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3674030'])) ) #Nariño

#print (g.serialize(format='pretty-xml'))
