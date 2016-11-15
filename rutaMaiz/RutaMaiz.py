#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from ontologias import UMBEL, CRUZAR, GEOES, OWL
from rdflib.namespace import RDF, RDFS, FOAF
from utils.namespaces import dbpedia, rutaMaiz, geonames
from utils.inicio import g

#g = Graph()

g.add( (URIRef(rutaMaiz['descripcion.rdf']), GEOES.formaParteDe, dbpedia.Tulua))
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Alojamientos.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Empresas.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Eventos.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Fauna.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Flora.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Lugares.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), UMBEL.hasCharacteristic, rutaMaiz['Restaurantes.rdf']) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rutaMaiz['descripcion.rdf']), RDFS.label, Literal("RUTA DEL MAÍZ", lang='es')) )
g.add( (URIRef(rutaMaiz['descripcion.rdf']), RDFS.comment, Literal("""Es una ruta de alto valor paisajístico, donde 
    el turista podrá deleitarse con la variedad de cultivos de cítricos, cultivos de maíz, cultivos de flores 
    exóticas. Comprende las gastronomía en torno de los productos a base de maíz, tales como trasnochados, 
    cuaresmeros, pandebonos, tortas, envueltos, masato, champús, chancarina y otros. El recorrido comienza desde 
    el Parque Carlos Sarmiento Lora, atravesando toda la ciudad de Tuluá hasta llegar al corregimiento de Campoalegre.""", lang='es')))
g.add( (URIRef(rutaMaiz), FOAF.depiction, URIRef("http://i.imgur.com/RQpb9ok.jpg")) )

##Links de la ruta
g.add( (URIRef(rutaMaiz['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3666646'])) ) #tulua
g.add( (URIRef(rutaMaiz['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3666644'])) ) #rio tulua

#print (g.serialize(format='pretty-xml'))	
