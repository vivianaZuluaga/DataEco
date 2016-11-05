# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, ACCO, UMBEL
from utils.namespaces import rioFrio, maps, imgur, alcaldiaRiofrio
from RutaRiofrio import g


def alojamientos(uri, nombre, webpage, telefono, email, direcc, mapa, descripcion, uriRoom, uriValue, 
	uriBed, numHabitaciones, numCamas, imagen):
	if webpage != "No disponible":
		g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)))	
			
	g.add( (URIRef(uri), RDF.type, ACCO.Hotel))
	g.add( (URIRef(uri), RDF.type, GR.Individual) )
	g.add( (URIRef(uri), GR.name, Literal(nombre, lang='es')) )
	g.add( (URIRef(uri), GR.description, Literal(descripcion, lang='es')) )
	g.add( (URIRef(uri), VCARD.tel, Literal(telefono)))
	g.add( (URIRef(uri), VCARD.email, Literal(email)))
	g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
	g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

	#Dirección según vCard 2006
	g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
	g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
	g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
	g.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

	#Horario de Atención
	g.add( (URIRef(uri), ACCO.feature, ACCO.AccommodationFeature) )
	g.add( (ACCO.AccommodationFeature, ACCO.availabilityTimes, Literal("24 Horas")) )

	#Habitaciones
	g.add( (URIRef(uriRoom), RDF.type, ACCO.HotelRoom))
	g.add( (URIRef(uriRoom), RDF.type, GR.SomeItems) )
	g.add( (URIRef(uriRoom), ACCO.partOf, URIRef(uri)) )

	#Value
	g.add( (URIRef(uriValue), RDF.type, GR.QuantitativeValue))
	g.add( (URIRef(uriRoom), ACCO.numberOfRooms, URIRef(uriValue)) )
	g.add( (URIRef(uriValue), GR.hasUnitOfMeasurement, Literal("C62"))) #No hay unidades
	g.add( (URIRef(uriValue), GR.hasValue, Literal(numHabitaciones, datatype=XSD.int)))

	#Camas

	g.add( (URIRef(uriBed), RDF.type, ACCO.BedDetails))
	g.add( (URIRef(uriRoom), ACCO.bed, URIRef(uriBed)))
	g.add( (URIRef(uriBed), ACCO.quantity, Literal(numCamas, datatype=XSD.int)))

	#g.add( (URIRef(uri), VCARD.cateogry, Literal("Alojamientos Riofrío")))
	g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rioFrio.Alojamientos)))

alojamientos(
	alcaldiaRiofrio['2720854'],
	'FINCA-HOTEL SANTA TERESITA',
	'http://www.fincasantateresita.8m.com/',
	'2244447, 2259381, 3104580461, 3004738684',
	'fincasantateresita@hotmail.com',
	'Vía Riofrío - Salónica, Riofrío, Valle del Cauca',
	maps['2uMdPYJkN1n'],
	"""Alojamiento en habitaciones multiples con baño privado, servicio de restaurante criollo, 
	piscina de agua natural, kiosco para eventos con capacidad para 50 personas, caminatas y cabalgatas ecológicas, 
	zona de camping. Ubicada en la Vereda el Crucero.""",
	alcaldiaRiofrio['index.shtml?apc=bjxx-1-&x=2720854'],
	alcaldiaRiofrio['sitios_visitar.shtml'],
	'http://www.fincasantateresita.8m.com/tarifas.html',
	'4',
	'12',
	imgur['lUSf4vV.jpg']
)

#print(g.serialize(format='pretty-xml'))	
