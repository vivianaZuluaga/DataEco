#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace
from rdflib import URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import OWL, VoID, dcterms, OWL
from utils.namespaces import dbpedia, geonames, uniprot, rutaMaiz, rioFrio

g = Graph()

DBpedia = URIRef('http://dbpedia.org/resource/')
UniProt = URIRef('http://www.uniprot.org/taxonomy/')
GeoNames = URIRef('http://www.geonames.org/')

DataEco = URIRef('http://www.dataeco.org/dataseteco/void.rdf')
DataEcouniprot = URIRef('http://www.dataeco.org/dataseteco/void.rdf#dataEcouniprot')
DataEcodbpedia = URIRef('http://www.dataeco.org/dataseteco/void.rdf#dataEcodbpedia')
DataEcoGeonames = URIRef('http://www.dataeco.org/dataseteco/void.rdf#dataEcoGeonames')

creatorCarlos = URIRef('http://www.dataeco.org/dataseteco/autores.rdf#camorenov')
creatorViviana = URIRef('http://www.dataeco.org/dataseteco/autores.rdf#vzuluagab')
contribuitorAlbeiro = URIRef('http://www.dataeco.org/dataseteco/autores.rdf#alaponte')
contribuitorOscar = URIRef('http://www.dataeco.org/dataseteco/autores.rdf#oceballos')
contribuitorYuri = URIRef('http://www.dataeco.org/dataseteco/autores.rdf#ybermudez')

##Información Básica
g.add( (DataEco, RDF.type, VoID.Dataset) )
g.add( (DataEco, FOAF.homepage, URIRef('http://www.dataeco.org/dataseteco/EcolodApp/')) )
g.add( (DataEco, dcterms.title, Literal('DataEco')) )
g.add( (DataEco, dcterms.description, Literal("""Dataset con información ecoturística de los
municipios de Riofrío y Tuluá pertenecientes a la subregión Centro del Valle del Cauca""")))
g.add( (DataEco, dcterms.creator, creatorCarlos) ) #responsables creacion dataset
g.add( (DataEco, dcterms.creator, creatorViviana) )
g.add( (DataEco, dcterms.publisher, dbpedia['Universidad_del_Valle_(Colombia)']) ) #responsable de hacer que el dataset este disponible
g.add( (DataEco, dcterms.contributor, contribuitorAlbeiro) ) # responsables de hacer contribuciones al dataset
g.add( (DataEco, dcterms.contributor, contribuitorOscar) )
g.add( (DataEco, dcterms.contributor, contribuitorYuri) )
g.add( (DataEco, dcterms.created, Literal('2016-09-17', datatype=XSD.date)) )

#licencia
g.add( (DataEco, dcterms.license, URIRef('https://creativecommons.org/licenses/by-sa/4.0/')))

#temas - se usan uris de dbpedia para categorizarlo
g.add( (DataEco, dcterms.subject, dbpedia['Ecotourism']) )
g.add( (DataEco, dcterms.subject, dbpedia['Tulua']) )
g.add( (DataEco, dcterms.subject, dbpedia['Riofrio,_Valle_del_Cauca']) )
g.add( (DataEco, dcterms.subject, dbpedia['Valle_del_Cauca_Department']) )
g.add( (DataEco, dcterms.subject, dbpedia['Location']) )

#Detalles tecnicos
g.add( (DataEco, VoID.feature, URIRef('http://www.w3.org/ns/formats/RDF_XML')) ) #formato

##Datos de Acceso
g.add( (DataEco, VoID.sparqlEndpoint, URIRef('http://190.14.254.238:3030/')) ) #endpoint

##Datos estructurales
g.add( (DataEco, VoID.exampleResource, URIRef(rioFrio['descripcion.rdf'])) ) 
g.add( (DataEco, VoID.exampleResource, URIRef(rutaMaiz['descripcion.rdf'])) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://idi.fundacionctic.org/cruzar/turismo')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://purl.org/acco/ns')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://purl.org/ontology/wo/')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://www.w3.org/2003/01/geo/wgs84_pos')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://geo.linkeddata.es/ontology/')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://purl.org/goodrelations/v1')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://www.w3.org/2006/vcard/ns')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://purl.org/NET/c4dm/event.owl')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://umbel.org/umbel')) )
g.add( (DataEco, VoID.vocabulary, URIRef('http://purl.org/dc/terms/')) )

g.add( (DataEco, VoID.triples, Literal('8934', datatype=XSD.int)) )

####Links - LinkSet colección de tripletas donde sujeto y objeto están en diferentes datasets
#Note: There are two different notions of “directionality” for RDF links:

    #Which dataset provides the subjects of the triples, and which the objects?
    #Which dataset contains the links? (Who published them?)
 
#links a dbpedia    
g.add( (DBpedia, RDF.type, VoID.Dataset) )
g.add( (DBpedia, FOAF.homepage, URIRef('http://dbpedia.org/fct/')) )
g.add( (DBpedia, dcterms.title, Literal('dbpedia')) )
g.add( (DBpedia, dcterms.description, Literal("""Hacia una Infraestructura de Datos Pública para un Gráfico de 
conocimiento semántico""")))

#DataEco - dbpedia
g.add( (DataEcodbpedia, RDF.type, VoID.Linkset) )
g.add( (DataEcodbpedia, VoID.linkPredicate, OWL.sameAs) )
g.add( (DataEcodbpedia, VoID.target, DataEco) )
g.add( (DataEcodbpedia, VoID.target, DBpedia) )
g.add( (DataEcodbpedia, VoID.subset, DataEco) ) #quien publica los links
g.add( (DataEcodbpedia, VoID.triples, Literal('393', datatype=XSD.int)) )

#links a uniprot Taxonomy  
g.add( (UniProt, RDF.type, VoID.Dataset) )
g.add( (UniProt, FOAF.homepage, URIRef('http://www.uniprot.org/')) )
g.add( (UniProt, dcterms.title, Literal('uniprot')) )
g.add( (UniProt, dcterms.description, Literal("""Los organismos se clasifican en una estructura de 
árbol jerárquica. La base de datos 'taxonomy' contiene todos los nodos (taxones) del árbol.""")))

#DataEco - uniprot
g.add( (DataEcouniprot, RDF.type, VoID.Linkset) )
g.add( (DataEcouniprot, VoID.linkPredicate, OWL.sameAs) )
g.add( (DataEcouniprot, VoID.target, DataEco) )
g.add( (DataEcouniprot, VoID.target, UniProt) )
g.add( (DataEcouniprot, VoID.subset, DataEco) ) #quien publica los links
g.add( (DataEcouniprot, VoID.triples, Literal('396', datatype=XSD.int)) )

#links a Geonames Taxonomy  
g.add( (GeoNames, RDF.type, VoID.Dataset) )
g.add( (GeoNames, FOAF.homepage, URIRef('http://www.geonames.org/ontology/documentation.html')) )
g.add( (GeoNames, dcterms.title, Literal('GeoNames')) )
g.add( (GeoNames, dcterms.description, Literal("""La base de datos geográfica 'GeoNames' cubre todos los países 
y contiene más de once millones de nombres de lugares que están disponibles para descargar de forma gratuita.""")))

#DataEco - Geonames
g.add( (DataEcoGeonames, RDF.type, VoID.Linkset) )
g.add( (DataEcoGeonames, VoID.linkPredicate, OWL.sameAs) )
g.add( (DataEcoGeonames, VoID.target, DataEco) )
g.add( (DataEcoGeonames, VoID.target, GeoNames) )
g.add( (DataEcoGeonames, VoID.subset, DataEco) ) #quien publica los links
g.add( (DataEcoGeonames, VoID.triples, Literal('13', datatype=XSD.int)) )
 
print (g.serialize(format='pretty-xml'))
