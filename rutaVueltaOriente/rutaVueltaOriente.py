#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import UMBEL, CRUZAR, GEOES, OWL
from utils.namespaces import rutaVueltaOriente, geonames, dbpedia
from rutaJardinBotanico.lugaresJardinBotanico import g


g.add( (URIRef(rutaVueltaOriente), GEOES.formaParteDe, dbpedia.Tulua))
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Alojamientos ) )
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Empresas) )
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Eventos) )
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Fauna) )
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Flora) )
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Lugares) )
g.add( (URIRef(rutaVueltaOriente), UMBEL.hasCharacteristic, rutaVueltaOriente.Restaurantes) )
g.add( (URIRef(rutaVueltaOriente), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rutaVueltaOriente), RDFS.label, Literal("RUTA VUELTA A ORIENTE", lang='es')) )
g.add( (URIRef(rutaVueltaOriente), RDFS.comment, Literal("""Al llegar al hipermercado La 14 y enrutarse hacia la Escuela de Policía 
Simón Bolívar de Tuluá (Esbol) inicia la Vuelta a Oriente.  Senderos entre plantaciones de especies nativas en 150 hectáreas, a 
1.100 metros sobre el nivel del mar y 24 grados de temperatura, en promedio, esperan al visitante.""", lang='es')) )
g.add( (URIRef(rutaVueltaOriente), FOAF.depiction, URIRef("http://i.imgur.com/xbaeiIt.jpg")) )

##Links de la ruta - Corregimientos
g.add( (URIRef(rutaVueltaOriente), OWL.sameAs, URIRef(geonames['3768950'])) ) #la rivera
g.add( (URIRef(rutaVueltaOriente), OWL.sameAs, URIRef(geonames['3683480'])) ) #el Picacho
g.add( (URIRef(rutaVueltaOriente), OWL.sameAs, URIRef(geonames['3782975'])) ) #la Moralia
g.add( (URIRef(rutaVueltaOriente), OWL.sameAs, URIRef(geonames['3678726'])) ) #la Iberia
g.add( (URIRef(rutaVueltaOriente), OWL.sameAs, URIRef(geonames['3678442'])) ) #la Marina

#print(g.serialize(format='pretty-xml'))

