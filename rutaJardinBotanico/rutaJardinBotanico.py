#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import UMBEL, CRUZAR, GEOES, OWL
from utils.namespaces import rutaJardin, geonames, dbpedia 
from rutaAnilloAgricola.restaurantesAgricola import g


g.add( (URIRef(rutaJardin), GEOES.formaParteDe, dbpedia.Tulua))
g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Alojamientos ) )
#g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Empresas) )
#g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Eventos) )
#g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Fauna) )
g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Flora) )
g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Lugares) )
#g.add( (URIRef(rutaJardin), UMBEL.hasCharacteristic, rutaJardin.Restaurantes) )
g.add( (URIRef(rutaJardin), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rutaJardin), RDFS.label, Literal("RUTA HACIA EL JARDÍN BOTÁNICO O MATEGUADUA DESTINO ECOTURÍSTICO", lang='es')) )
g.add( (URIRef(rutaJardin), RDFS.comment, Literal("""Se inicia en el corregimiento de Cienegueta, entrando por la doble 
calzada. La Vía destapada limita con el río Tuluá y conduce a Mateguadua y Puente Zinc. En el recorrido el turista disfrutará de 
un encuentro con la naturaleza, hermosos paisajes, vista panorámica de la zona urbana de Tuluá, además de ganaderías.""", lang='es')) )
g.add( (URIRef(rutaJardin), FOAF.depiction, URIRef("http://i.imgur.com/xRi00pT.jpg")) )


#print(g.serialize(format='pretty-xml'))
