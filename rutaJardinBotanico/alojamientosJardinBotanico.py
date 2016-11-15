#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, ACCO, UMBEL
from utils.namespaces import rutaJardin, facebook, ciudadGuru, maps, imgur
from rutaJardinBotanico import g


def alojamientos(uri, nombre, webpage, telefono, email, direcc, mapa, descripcion, uriRoom, uriValue, 
	uriBed, numHabitaciones, numCamas, imagen, linkURI):
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

	#g.add( (URIRef(uri), VCARD.cateogry, Literal("Alojamientos de la Ruta del Maíz")))
	g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaJardin['Alojamientos.rdf'])))
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo


alojamientos(
	 rutaJardin['Alojamientos.rdf#jardinBotanico'],
	'JARDÍN BOTÁNICO JUAN MARÍA CÉSPEDES',
	'http://inciva.gov.co/patrimonios-turisticos/jardin-botanico-juan-maria-cespedes-tulua/',
	'3206888271, 3156361319',
	'jardinbotanico@inciva.gov.co',
	'Mateguada, Valle del Cauca', #direccion
	maps['7SWSXJa77pQ2'],
	"""El Jardín Botánico Juan María Céspedes es un centro de investigaciones del Instituto para
	la Investigación y la Preservación del Patrimonio Cultural y Natural del Valle del Cauca - INCIVA. Ubicado en el 
	corregimiento de Mateguadua.""",
	'http://www.livevalledelcauca.com/tulua/jardin-botanico-juan-maria-cespedes.html',
	ciudadGuru['jardin-botanico-juan-maria-cespedes-tulua/tulua/15952821'],
	facebook['pages/Jardin-Botanico-Juan-Maria-Cespedes/193724564145315'],
	'2',#NumHabitaciones
	'8',#NumCamas
	imgur['QCAEQ1y.jpg'],
	facebook['jbjuanmariacespedes']
)

alojamientos(
	 rutaJardin['Alojamientos.rdf#casaCampestre'],
	'CASA CAMPESTRE MATEGUADUA',
	'No disponible',
	'3016070060',
	'No disponible',
	'Mateguada, Valle del Cauca', #direccion
	maps['HwUEQxtVVWu'],
	"""Cuenta con cocina, estufa de gas, nevera, asador, fogón de leña. Ubicada en el corregimiento de Mateguadua a 
	700 ms del Jardín Botánico Juan María Céspedes, a orillas de la carretera y cerca del río Tuluá.""",
	facebook['QueHayPaHacerTulua/photos/a.1051206711587508.1073741826.315617475146439/1051206934920819/?type=3'],
	facebook['QueHayPaHacerTulua'],
	facebook['QueHayPaHacerTulua/photos/a.1051206711587508.1073741826.315617475146439/1051206901587489/?type=3'],
	'3',#NumHabitaciones
	'5',#NumCamas
	imgur['EVYhBtm.jpg'],
	facebook['media/set/?set=a.1051206711587508.1073741826.315617475146439&type=3']
)

#print(g.serialize(format='pretty-xml'))
