#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, DC, FOAF
from utils.ontologias import VCARD, EVENT, UMBEL, TIME
from utils.namespaces import rutaVueltaOriente, facebook, twitter, imgur, maps, youtube
from empresasVueltaOriente import g
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
	g.add( ( URIRef(uri), EVENT.place, URIRef(mapa)) )#http://www.maps.org/3666646	
	g.add( ( URIRef(mapa), RDFS.label, Literal(lugar, lang='es')) ) # datatype=XSD.string
	
	g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaVueltaOriente['Eventos.rdf'])) )
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo

eventos(
	rutaVueltaOriente['Eventos.rdf#fiestasReyes'],#uri
	'FIESTAS DE REYES Y FERIA GANADERA',#nombre
	'2017-01-07T00:00:00Z',#fecha CCYY-MM-DDThh:mm:ss
	"""La programación de las festividades incluye Cabalgata, feria ganadera y equina, venta de gastronomía típica, juegos 
	tradicionales de la cultura campesina como "subir un tronco engrasado", carrera de encostalados, entre otros. Se dispone 
	todo el tiempo de una tarima para presentación de grupos artísticos.""",#descripcion
	'La Marina, Valle del Cauca',#lugar
	youtube['TswybiVKASo'],#video
	imgur['438LfFg.jpg'],#imagen
	twitter['767897508722991104'],
	maps['qFaNLL7zQ2C2'],
	"P2D",#PnYn MnDTnH nMnS
	'http://www.tulua.gov.co/sitio.shtml?apc=m1v1--&x=1480713'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#fiestasCampesino'],#uri
	'FIESTAS DEL CAMPESINO',#nombre
	'2016-09-18T00:00:00Z',#fecha
	"""Es la fiesta anual donde se reúnen todos los habitantes de la vereda, familias y amigos; se realizan actividades típicas 
	como cabalgatas, presentación de espectáculos, marrano engrasado, competencias infantiles y muestras de los campesinos.""",#descripcion
	'La Iberia, Valle del Cauca',#lugar
	'No disponible',#video
	imgur['52ldlxo.jpg'],#imagen
	twitter['767898777864794113'],
	maps['qqkBHrAmJa12'],
	'P2D',#PnYn MnDTnH nMnS
	'http://elperiodicowebregion.blogspot.com.co/2010/09/fiestas-del-campesino-y-la-alegria.html'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#baileDiciembre'],#uri
	'BAILE DEL 31 DE DICIEMBRE',#nombre
	'2016-12-31T00:00:00Z',#fecha
	"""Se reúnen las familias de la vereda y hacen un baile con cena, concursos y una actividad muy llamativa, que consiste en 
	leer un pergamino con refranes de los personajes típicos de la región, también bebidas típicas, buñuelos, natilla y dulce manjar 
	blanco. Cada una de las familias lleva un muñeco “Año viejo”, y los queman simultáneamente a media noche.""",#descripcion
	'La Iberia, Valle del Cauca',#lugar
	'No disponible',#video
	imgur['7heSlcY.jpg'],#imagen
	twitter['767900391610650625'],
	maps['WHPFE1ukYHK2'],
	'P1D',#PnYn MnDTnH nMnS
	'http://turismotulua.blogspot.com.co/2014/07/caracterizacion-del-inventario.html'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#diaVictimas'],#uri
	'DÍA DE LAS VÍCTIMAS',#nombre
	'2017-08-04T00:00:00Z',#fecha
	"""Homenaje a las víctimas del paramilitarismo.""",#descripcion
	'La Moralia, Valle del Cauca',#lugar
	youtube['3KL8SgdMwyM'],#video
	imgur['4VEPRb1.jpg'],#imagen
	twitter['767903221813772288'],
	maps['Xsj8ugEpHXv'],
	'P1D',#PnYn MnDTnH nMnS
	'http://www.eltabloide.com.co/memoria-y-dignidad-campesina-en-la-moralia/'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#ganeX5'],#uri
	'DESAFÍO GUERREROS GANE X5',#nombre
	'2017-07-03T00:00:00Z',#fecha
	"""Evento en el que se busca fomentar la practica del deporte para tener una vida saludable. Es un recorrido en el que se 
	pondrá a prueba la fortaleza mental, resistencia física, agilidad y trabajo en equipo. Realizado en el Rancho Las Palmas.""",#descripcion
	'La Rivera, Tuluá, Valle del Cauca',#lugar
	youtube['UwspEG-Bu6A'],#video cambiar
	imgur['yRKmOVw.jpg'],#imagen
	'http://ganecentro.com/noticias/revive-la-emocion-de-desafio-guerreros-ganex5/',
	maps['nPXddjXKX2n'],
	'P1D',#PnYn MnDTnH nMnS
	'http://ganecentro.com/noticias/desafio-guerreros-gane-x5/'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#parapente'],#uri
	'VUELOS EN PARAPENTE',#nombre
	'2016-01-01T00:00:00Z',#fecha
	"""Vuelos en parapente desde $100.000 hasta $120.000, incluyen fotos, video, subida al lugar de encuentro. Disfruta 
	una gran sensación al volar de 20-30 minutos. Punto de encuentro Parador la Iberia. Para más informacion llamar al 3165440241""",#descripcion
	'La Iberia, Valle del Cauca',#lugar
	youtube['zVAgYrfPCY0'],#video
	imgur['1Z0meja.jpg'],#imagen
	twitter['767913157444657152'],
	maps['iSLVDv8eTWC2'],
	'P365D',#PnYn MnDTnH nMnS
	facebook['Club-de-parapente-tulua-528121404021970']
)

eventos(
	rutaVueltaOriente['Eventos.rdf#nacionalVaqueria'],#uri
	'NACIONAL DE VAQUERÍA',#nombre
	'2017-05-30T00:00:00Z',#fecha
	"""Evento del carnaval de apertura de la Feria de Tuluá. Participan vaqueros de varias regiones del país. Realizado en el 
	Rancho Las Palmas.""",#descripcion
	'La Rivera, Tuluá, Valle del Cauca',#lugar
	youtube['bPDpDWeVzEs'],#video
	imgur['lzsE2Ig.jpg'],#imagen
	'http://elperiodicowebtulua.blogspot.com.co/2015/06/nacional-de-vaqueria-en-tulua.html',
	maps['rchRKxTBmF62'],
	'P2D',#PnYn MnDTnH nMnS
	'http://elperiodicowebregion.blogspot.com.co/2015/06/desde-el-llano-llegaron-familias.html'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#nacionalCiclomontanismo'],#uri
	'VÁLIDA NACIONAL DE CICLOMONTAÑISMO',#nombre
	'2017-05-06T00:00:00Z',#fecha
	"""Evento en donde los ciclomontañistas (categorias infantil, prejuvenil, master) compiten por los puntos que entrega la 
	válida. Una pista seca de mucha habilidad, manejo, técnica y fuerza. Realizada en el Rancho Las Palmas.""",#descripcion
	'La Rivera, Tuluá, Valle del Cauca',#lugar
	youtube['a3-x_tlZYNE'],#video
	imgur['Umldzk8.jpg'],#imagen
	'http://www.coc.org.co/all-news/tulua-sera-sede-de-la-ii-valida-nacional-de-mtb/',
	maps['wYtUHVgpVTP2'],
	'P1D',#PnYn MnDTnH nMnS
	'http://www.mtbcolombia.com/noticias/item/el-valle-se-prepara-para-la-valida-nacional'
)

eventos(
	rutaVueltaOriente['Eventos.rdf#fiestasPicacho'],#uri
	'FIESTAS DEL RETORNO AL MORRO DEL PICACHO',#nombre
	'2016-10-14T00:00:00Z',#fecha
	"""Cabalgata, reinado de la vaca, ciclopaseo, exhibición de parapentes, festival gastronómico, artistas y competencias 
	de ciclomontañismo.""",#descripcion
	'El Picacho, Tuluá, Valle del Cauca',#lugar
	'No disponible',#video
	imgur['tt8Nwkr.jpg'],#imagen
	'http://www.eltabloide.com.co/category/picacho/',
	maps['5y7xQPvYVNL2'],
	'P3D',#PnYn MnDTnH nMnS
	'http://www.eltabloide.com.co/vibra-el-morro-de-el-picacho/'
)

#print (g.serialize(format="pretty-xml"))
