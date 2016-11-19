#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, DC, FOAF
from utils.ontologias import GR, VCARD, EVENT, UMBEL, TIME, GEONAMES
from utils.namespaces import facebook, twitter, youtube, imgur, maps, rutaAnillo
from floraAgricola import g

#g = Graph()

def eventos(uri, nombre, fecha, descripcion, lugar, media, image, uriTime, mapa, duracion, linkURI):
	if media != "No disponible":
		g.add(( URIRef(uri), EVENT.illustrate, URIRef(media)) )

	g.add(( URIRef(uri), RDF.type, EVENT.Event ) )
	g.add( (URIRef(uri), FOAF.depiction, URIRef(image)) )
	g.add(( URIRef(uri), RDFS.label, Literal(nombre, lang='es')) )
	g.add(( URIRef(uri), RDFS.comment, Literal(descripcion, lang='es')) )
	
	#Fecha y duracion
	g.add( ( URIRef(uri), EVENT.time, URIRef(uriTime) ) )
	g.add( ( URIRef(uriTime), RDF.type, TIME.Interval) )
	g.add( ( URIRef(uriTime), TIME.at, Literal(fecha, datatype=XSD.dateTime) ))
	g.add( ( URIRef(uriTime), TIME.duration, Literal(duracion, datatype=XSD.duration) ))
	
	#Lugar	
	g.add( ( URIRef(uri), EVENT.place, URIRef(mapa)) )	
	g.add( ( URIRef(mapa), RDFS.label, Literal(lugar, lang='es')) ) 
	
	g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaAnillo['Eventos.rdf'])) )
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) )
	g.add( (URIRef(uri), VCARD.category, Literal("EVENTOS", lang='es')))

	
eventos(
	rutaAnillo['Eventos.rdf#fiestasPatronales'],
	'FIESTAS PATRONALES DEL SEÑOR SANTO APARECIDO',
	'2016-08-04T17:00:00Z',
	"""Actividad celebrada cada año en la capilla del Santo Aparecido, ubicada en la vereda El Cairo de 
	Tuluá, como parte del cordón de turismo religioso de la región.""",
	'Vía a Tres Esquinas, Tuluá, Valle del Cauca',
	youtube['-40bgzzZoC4'],
	imgur['XyS55bz.png'],
	twitter['797966359980285958'],
	maps['MBaH4hDPBT82'],
	"P3D",#PnYn MnDTnH nMnS
	facebook['photo.php?fbid=10208577568495272&set=a.1035541447382.2007789.1190834860&type=3']
)

eventos(
	rutaAnillo['Eventos.rdf#fiestasRetorno'],
	'FIESTAS DEL RETORNO',
	'2016-11-04T00:00:00Z',
	"""Cabalgata, presentaciones artísticas, actividades deportivas, espacio para compartir en familia.""",
	'Tres Esquinas, Tuluá, Valle del Cauca',
	'No disponible',
	imgur['lmbAVVW.jpg'],
	twitter['797991285592379392'],
	maps['Y6TB7N9hxHw'],
	"P3D",#PnYn MnDTnH nMnS
	facebook['events/355103938162580']
)
		
#print(g.serialize(format='pretty-xml'))
