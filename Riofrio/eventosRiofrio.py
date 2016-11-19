#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, DC, FOAF
from utils.ontologias import VCARD, EVENT, UMBEL, TIME
from utils.namespaces import rioFrio, maps, imgur, geonames, youtube, twitter, facebook, alcaldiaRiofrio
from alojamientosRiofrio import g, rioFrio

#g = Graph()

def eventos(uri, nombre, fecha, descripcion, lugar, media, image, uriTime, mapa, duracion, linkURI):
	if media != "No disponible":
		g.add(( URIRef(uri), FOAF.depiction, URIRef(media)) )
		
	g.add( ( URIRef(uri), RDF.type, EVENT.Event ) )
	g.add( ( URIRef(uri), FOAF.depiction, URIRef(image)) )
	g.add( ( URIRef(uri), RDFS.label, Literal(nombre, lang='es')) )# forma lexica e idioma
	g.add( ( URIRef(uri), RDFS.comment, Literal(descripcion, lang='es')) )
	
	#Fecha y duracion
	g.add( ( URIRef(uri), EVENT.time, URIRef(uriTime) ) )
	g.add( ( URIRef(uriTime), RDF.type, TIME.Interval) )
	g.add( ( URIRef(uriTime), TIME.at, Literal(fecha, datatype=XSD.dateTime) ))
	g.add( ( URIRef(uriTime), TIME.duration, Literal(duracion, datatype=XSD.duration) ))
	
	#Lugar	
	g.add( ( URIRef(uri), EVENT.place, URIRef(mapa)) )#http://www.geonames.org/3666646	
	g.add( ( URIRef(mapa), RDFS.label, Literal(lugar, lang='es')) ) # datatype=XSD.string
	
	g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rioFrio['Eventos.rdf'])) )
	
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
	g.add( (URIRef(uri), VCARD.category, Literal("EVENTOS", lang='es')))

eventos(
	rioFrio['Eventos.rdf#fiestasEcoturisticas'],
	'FIESTAS ECOTURÍSTICAS Y DEL RETORNO',
	'2017-05-27T00:00:00Z',
	"""Se realizan presentaciones artísticas, actividades recreativas como el concurso Raja Leña, en el cual se dan tres troncos 
	a cada participante y debe astillarlos en media hora.""",
	'Fenicia, Riofrío, Valle del Cauca',
	youtube['BG9VJyksD0U'],
	imgur['xGBq9Yf.jpg'],
	twitter['769954296548974593'],
	geonames['3671462'],
	'P4D',
	alcaldiaRiofrio['eventos.shtml?apc=cdxx-1-&x=2722611']
)

eventos(
 	rioFrio['Eventos.rdf#feriaRiofrio'],
 	'FERIA DE RIOFRÍO',
 	'2017-10-10T00:00:00Z',
 	"""Se realizan conciertos de diferentes artistas y en horas de la tarde se ubican lugares para la venta de productos 
 	comercializados por los habitantes del municipio.""",
 	'Riofrío, Valle del Cauca',
 	youtube['7T1FAjEcWa0'],
 	imgur['0gc6Uce.png'],
 	twitter['769992497317707781'],
 	geonames['3670755'],
 	'P3D',
 	'http://www.valledelcauca.gov.co/turismo/publicaciones.php?id=28443'
)

eventos(
 	rioFrio['Eventos.rdf#fiestasSalonica'],
 	'FIESTAS DE SALÓNICA',
 	'2017-01-09T00:00:00Z',
 	"""Se realizan actividades recreativas y conciertos de diferentes artistas.""",
 	'Salónica, Riofrío, Valle del Cauca',
 	youtube['4ObHOKolrRY'],
 	imgur['rEh73KD.jpg'],
 	twitter['769996208295346177'],
 	maps['pXZPmiHenbQ2'],
 	'P3D',
 	'http://mobile.pueblosdecolombia.com/Departamento%20del%20Valle%20del%20Cauca/fiestas/26459/Salonica.html'
)

eventos(
 	rioFrio['Eventos.rdf#carnavalDuende'],
 	'CARNAVAL DEL DUENDE',
 	'2016-11-01T00:00:00Z',
 	"""Se realiza cada año para fomentar el ecoturismo, la conservación del ecosistema y difundir las creencias, las danzas, 
 	la música, así como los mitos, las leyendas, historias y ritos tradicionales.""",
 	'Fenicia, Riofrío, Valle del Cauca',
 	'No disponible',
 	imgur['b292tQI.png'],
 	twitter['797112613721214976'],
 	maps['Cof1SHSbEQs'],
 	'P4D',
 	facebook['groups/262819420499376']
)

#print (g.serialize(format="pretty-xml"))    	
