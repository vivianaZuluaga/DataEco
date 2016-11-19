# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from utils.ontologias import UMBEL, CRUZAR, GEOES, OWL, skos
from rdflib.namespace import RDF, RDFS, FOAF
from utils.namespaces import rioFrio, geonames, dbpedia
from rutaMaiz.restaurantes import g

#g = Graph()

g.add( (URIRef(rioFrio['descripcion.rdf']), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rioFrio['descripcion.rdf']), GEOES.formaParteDe, dbpedia['Riofrio,_Valle_del_Cauca']))
g.add( (URIRef(rioFrio['descripcion.rdf']), skos.related, rioFrio['Alojamientos.rdf']) )
g.add( (URIRef(rioFrio['descripcion.rdf']), skos.related, rioFrio['Eventos.rdf']) )
g.add( (URIRef(rioFrio['descripcion.rdf']), skos.related, rioFrio['Fauna.rdf']) )
g.add( (URIRef(rioFrio['descripcion.rdf']), skos.related, rioFrio['Flora.rdf']) )
g.add( (URIRef(rioFrio['descripcion.rdf']), skos.related, rioFrio['Lugares.rdf']) )
g.add( (URIRef(rioFrio['descripcion.rdf']), skos.related, rioFrio['Restaurantes.rdf']) )


g.add( (URIRef(rioFrio['descripcion.rdf']), RDFS.label, Literal("RIOFRÍO", lang="es")) )
g.add( (URIRef(rioFrio['descripcion.rdf']), RDFS.comment, Literal("""Por la carretera panorama se encuentra el municipio de Riofrío, 
su diversidad de pisos térmicos va de la mano con su topografía y orografía. Es conocido como una autentica reserva turística, por 
poseer los parajes más típicos del valle, riqueza ecológica y abundante fauna.""", lang="es")) )
g.add( (URIRef(rioFrio['descripcion.rdf']), FOAF.depiction, URIRef("http://i.imgur.com/2XEPrR1.jpg")) )

##Links de la ruta
g.add( (URIRef(rioFrio['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3670754'])) ) #riofrio
g.add( (URIRef(rioFrio['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3783081'])) ) #vda La Vigorosa

#print (g.serialize(format='pretty-xml'))

