#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.namespaces import facebook, geonames


g = Graph()

def autores(uri, nombreCompleto, nombre, apellido, nick, titulo, email, homepage, interes, ubicacion, linkURI): 
	if homepage != 'No disponible':
		g.add( (URIRef(uri), FOAF.homepage, URIRef(homepage)) )
	if linkURI != 'No disponible':
		g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) )
		
	g.add( (URIRef(uri), RDF.type, FOAF.Person) )
	g.add( (URIRef(uri), FOAF.name, Literal(nombreCompleto)) )
	g.add( (URIRef(uri), FOAF.givenname, Literal(nombre)) )
	g.add( (URIRef(uri), FOAF.family_name, Literal(apellido)) )
	g.add( (URIRef(uri), FOAF.nick, Literal(nick)) )
	g.add( (URIRef(uri), FOAF.title, Literal(titulo)) )
	g.add( (URIRef(uri), FOAF.mbox, Literal(email)) )  
	g.add( (URIRef(uri), FOAF.based_near, URIRef(ubicacion)) )
	g.add( (URIRef(uri), FOAF.interest, URIRef(interes)) )
    
    
autores(
	'http://190.14.254.237/dataseteco/autores.rdf#vzuluagab',
	'Viviana Andrea Zuluaga',
	'Viviana Andrea',
	'Zuluaga',
	'vzuluagab',
	'Estudiante',
	'viviana.zuluaga@correounivalle.edu.co',
	'https://github.com/vivianaZuluaga',
	geonames['3666646'],
	'http://linkeddata.org/',
	facebook['vzuluagabolanos']
)

autores(
	'http://190.14.254.237/dataseteco/autores.rdf#camorenov',
	'Carlos Andrés Moreno',
	'Carlos Andrés',
	'Moreno',
	'camorenov',
	'Estudiante',
	'carlos.a.moreno.v@correounivalle.edu.co',
	'http://carmoreno.github.io/',
	geonames['3666646'],
	'http://linkeddata.org/',
	'https://co.linkedin.com/in/carmoreno1'
)

autores(
	'http://190.14.254.237/dataseteco/autores.rdf#ybermudez',
	'Yuri Mercedes Bermúdez Mazuera',
	'Yuri Mercedes',
	'Bermúdez Mazuera',
	'ybermudez',
	'Profesora',
	'yuri.bermudez@correounivalle.edu.co',
	'http://independent.academia.edu/YuriMercedesBermudezMazuera',
	geonames['3666646'],
	'http://linkeddata.org/',
	'https://plus.google.com/112830835883823056733'
)

autores(
	'http://190.14.254.237/dataseteco/autores.rdf#oceballos',
	'Oscar Orlando Ceballos Argote',
	'Oscar Orlando',
	'Ceballos Argote',
	'oceballos',
	'Profesor',
	'oscar.ceballos@correounivalle.edu.co',
	'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001378665',
	geonames['3687925'],
	'http://linkeddata.org/',
	'https://plus.google.com/107843414783163417790'
)

autores(
	'http://190.14.254.237/dataseteco/autores.rdf#alaponte',
	'Albeiro Aponte Vargas',
	'Albeiro',
	'Aponte Vargas',
	'alaponte',
	'Profesor',
	'albeiro.aponte@correounivalle.edu.co',
	'No disponible',
	geonames['3673164'],
	'http://linkeddata.org/',
	'No disponible'
)
    
print (g.serialize(format='pretty-xml'))  
