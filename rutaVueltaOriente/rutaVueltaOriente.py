#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import UMBEL, CRUZAR, GEOES, OWL, skos
from utils.namespaces import rutaVueltaOriente, geonames, dbpedia
from rutaJardinBotanico.lugaresJardinBotanico import g

#g = Graph()

g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), GEOES.formaParteDe, dbpedia.Tulua))
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Alojamientos.rdf'] ) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Empresas.rdf']) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Eventos.rdf']) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Fauna.rdf']) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Flora.rdf']) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Lugares.rdf']) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), skos.related, rutaVueltaOriente['Restaurantes.rdf']) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), RDFS.label, Literal("RUTA VUELTA A ORIENTE", lang='es')) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), RDFS.comment, Literal("""Al llegar al hipermercado La 14 y enrutarse hacia la Escuela de Policía 
Simón Bolívar de Tuluá (Esbol) inicia la Vuelta a Oriente.  Senderos entre plantaciones de especies nativas en 150 hectáreas, a 
1.100 metros sobre el nivel del mar y 24 grados de temperatura, en promedio, esperan al visitante.""", lang='es')) )
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), FOAF.depiction, URIRef("http://i.imgur.com/xbaeiIt.jpg")) )

##Links de la ruta - Corregimientos
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3768950'])) ) #la rivera
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3683480'])) ) #el Picacho
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3782975'])) ) #la Moralia
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3678726'])) ) #la Iberia
g.add( (URIRef(rutaVueltaOriente['descripcion.rdf']), OWL.sameAs, URIRef(geonames['3678442'])) ) #la Marina

#print(g.serialize(format='pretty-xml'))

