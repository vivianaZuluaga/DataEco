# -*- coding: utf-8 -*-

from rdflib import Namespace
from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS
from ontologias import GEOES, GEOPOS

dbr = Namespace('http://dbpedia.org/resource/')
wikidata = Namespace('http://www.wikidata.org/entity/')

g = Graph()

g.add( (dbr['Riofrio,_Valle_del_Cauca'], GEOES.formaParteDe, wikidata.Q5762107) )
g.add( (dbr.Tulua, GEOES.formaParteDe, wikidata.Q5762107) )

#Datos geograficos generales de cada municipio
g.add( (dbr.Tulua, RDF.type, GEOES.Municipio) )
g.add( (dbr.Tulua, GEOPOS.geometry, GEOPOS.lat) )
g.add( (dbr.Tulua, GEOPOS.geometry, GEOPOS.long) )
g.add( (dbr.Tulua, RDFS.label, Literal('Corazón del Valle', lang='es')) )
g.add( (GEOPOS.lat, GEOPOS.SpatialThing, Literal('4.083333')) )
g.add( (GEOPOS.long, GEOPOS.SpatialThing, Literal('-76.199997')) )
g.add( (GEOPOS.lat, RDF.type, GEOPOS.point) )
g.add( (GEOPOS.long,  RDF.type, GEOPOS.point) )

g.add( (dbr['Riofrio,_Valle_del_Cauca'], RDF.type, GEOES.Municipio) )
g.add( (dbr['Riofrio,_Valle_del_Cauca'], GEOPOS.geometry, GEOPOS.lat) )
g.add( (dbr['Riofrio,_Valle_del_Cauca'], GEOPOS.geometry, GEOPOS.long) )
g.add( (GEOPOS.lat, GEOPOS.SpatialThing, Literal('4.156111')) )
g.add( (GEOPOS.long, GEOPOS.SpatialThing, Literal('76.287781')) )
g.add( (GEOPOS.lat, RDF.type, GEOPOS.point) )
g.add( (GEOPOS.long,  RDF.type, GEOPOS.point) )

#print (g.serialize(format='pretty-xml'))


