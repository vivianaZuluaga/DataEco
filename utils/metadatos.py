#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, BNode
from rdflib import URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import OWL, VoID, dcterms, OWL
from rutaVueltaOriente.restaurantesVueltaOriente import g

#g = Graph()

DataEco = BNode()
DataEcoUniProt = BNode()
DataEcoDBpedia = BNode()
DataEcoGeonames = BNode()
creatorCarlos = URIRef('https://www.facebook.com/carmoreno11')
creatorViviana = URIRef('https://www.facebook.com/vzuluagabolanos')
contribuitorAlbeiro = URIRef('https://www.facebook.com/yurimercedes.bermudezmazuera')
contribuitorOscar = URIRef('https://www.facebook.com/oscar.orlando.ceballos.argote')
contribuitorYuri = URIRef('https://www.facebook.com/yurimercedes.bermudezmazuera')
univalle = URIRef('http://www.univalle.edu.co/')
DBpedia = URIRef('http://www.dbpedia.org/')
UniProt = URIRef('http://www.uniprot.org/taxonomy/')
geonames = URIRef('http://www.geonames.org/')

##Información Básica
g.add( (DataEco, RDF.type, VoID.Dataset) )
g.add( (DataEco, FOAF.homepage, URIRef('190.14.254.237/dataseteco/EcolodApp/')) )
g.add( (DataEco, dcterms.title, Literal('DataEco')) )
g.add( (DataEco, dcterms.description, Literal("""Dataset con información ecoturística de los
municipios de Riofrío y Tuluá pertenecientes a la subregión Centro del Valle del Cauca""")))
g.add( (DataEco, dcterms.creator, creatorCarlos) ) #responsables creacion dataset
g.add( (DataEco, dcterms.creator, creatorViviana) )
g.add( (DataEco, dcterms.publisher, univalle) ) #responsable de hacer que el dataset este disponible
g.add( (DataEco, dcterms.contributor, contribuitorAlbeiro) ) # responsables de hacer contribuciones al dataset
g.add( (DataEco, dcterms.contributor, contribuitorOscar) )
g.add( (DataEco, dcterms.contributor, contribuitorYuri) )
g.add( (DataEco, dcterms.created, Literal('2016-09-17', datatype=XSD.date)) )

#creadores
g.add( (creatorCarlos, RDF.type, FOAF.Person) )
g.add( (creatorCarlos, RDFS.label, Literal('Carlos Andres Moreno Vélez')) )
g.add( (creatorCarlos, FOAF.mbox, Literal('carlos.a.moreno.v@correounivalle.edu.co')) )

g.add( (creatorViviana, RDF.type, FOAF.Person) )
g.add( (creatorViviana, RDFS.label, Literal('Viviana Andrea Zuluaga Bolaños')) )
g.add( (creatorViviana, FOAF.mbox, Literal('viviana.zuluaga@correounivalle.edu.co')) )

#publicacion
g.add( (univalle, RDF.type, FOAF.Organization) )
g.add( (univalle, RDFS.label, Literal('Universidad del Valle Sede Tuluá')) )
g.add( (univalle, FOAF.homepage, URIRef('http://tulua.univalle.edu.co/')) )

#contribuidores
g.add( (contribuitorYuri, RDF.type, FOAF.Person) )
g.add( (contribuitorYuri, RDFS.label, Literal('Yuri Mercerdes Bermúdez')) )
g.add( (contribuitorYuri, FOAF.mbox, Literal('yuri.bermudez@correounivalle.edu.co')) )

g.add( (contribuitorOscar, RDF.type, FOAF.Person) )
g.add( (contribuitorOscar, RDFS.label, Literal('Oscar Orlando Ceballos Argote')) )
g.add( (contribuitorOscar, FOAF.mbox, Literal('oscar.ceballos@correounivalle.edu.co')) )

g.add( (contribuitorAlbeiro, RDF.type, FOAF.Person) )
g.add( (contribuitorAlbeiro, RDFS.label, Literal('Albeiro Aponte')) )
g.add( (contribuitorAlbeiro, FOAF.mbox, Literal('alaponte@gmail.com')) )

#licencia
g.add( (DataEco, dcterms.license, URIRef('https://creativecommons.org/licenses/by-sa/4.0/')))

#temas - se usan uris de dbpedia para categorizarlo
g.add( (DataEco, dcterms.subject, URIRef('http://dbpedia.org/resource/Ecotourism')) )
g.add( (DataEco, dcterms.subject, URIRef('http://dbpedia.org/resource/Tulua')) )
g.add( (DataEco, dcterms.subject, URIRef('http://dbpedia.org/resource/Riofri­o,_Valle_del_Cauca')) )
g.add( (DataEco, dcterms.subject, URIRef('http://dbpedia.org/resource/Valle_del_Cauca_Department')) )
g.add( (DataEco, dcterms.subject, URIRef('http://dbpedia.org/resource/Location')) )

#Detalles tecnicos
g.add( (DataEco, VoID.feature, URIRef('http://www.w3.org/ns/formats/RDF_XML')) ) #formato

##Datos de Acceso
g.add( (DataEco, VoID.sparqlEndpoint, URIRef('http://190.14.254.238:3030/')) ) #endpoint

##Datos estructurales
g.add( (DataEco, VoID.exampleResource, URIRef('http://190.14.254.237/dataseteco/Riofrio/')) )
g.add( (DataEco, VoID.exampleResource, URIRef('http://190.14.254.237/dataseteco/RutaDelMaiz/')) )
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

g.add( (DataEco, VoID.triples, Literal('7147', datatype=XSD.int)) )

####Links - LinkSet colección de tripletas donde sujeto y objeto están en diferentes datasets
#Note: There are two different notions of “directionality” for RDF links:

    #Which dataset provides the subjects of the triples, and which the objects?
    #Which dataset contains the links? (Who published them?)
 
#links a DBpedia    
g.add( (DBpedia, RDF.type, VoID.Dataset) )
#g.add( (DBpedia, FOAF.homepage, URIRef('')) )
g.add( (DBpedia, dcterms.title, Literal('DBpedia')) )
g.add( (DBpedia, dcterms.description, Literal("""Hacia una Infraestructura de Datos Pública para un Gráfico de 
conocimiento semántico""")))

#DataEco - DBpedia
g.add( (DataEcoDBpedia, RDF.type, VoID.Linkset) )
g.add( (DataEcoDBpedia, VoID.linkPredicate, OWL.sameAs) )
g.add( (DataEcoDBpedia, VoID.target, DataEco) )
g.add( (DataEcoDBpedia, VoID.target, DBpedia) )
g.add( (DataEcoDBpedia, VoID.subset, DataEco) ) #quien publica los links
g.add( (DataEcoDBpedia, VoID.triples, Literal('', datatype=XSD.int)) )

#links a Uniprot Taxonomy  
g.add( (UniProt, RDF.type, VoID.Dataset) )
#g.add( (UniProt, FOAF.homepage, URIRef('')) )
g.add( (UniProt, dcterms.title, Literal('UniProt')) )
g.add( (UniProt, dcterms.description, Literal("""""")))

#DataEco - UniProt
g.add( (DataEcoUniProt, RDF.type, VoID.Linkset) )
g.add( (DataEcoUniProt, VoID.linkPredicate, OWL.sameAs) )
g.add( (DataEcoUniProt, VoID.target, DataEco) )
g.add( (DataEcoUniProt, VoID.target, UniProt) )
g.add( (DataEcoUniProt, VoID.subset, DataEco) ) #quien publica los links
g.add( (DataEcoUniProt, VoID.triples, Literal('', datatype=XSD.int)) )

#links a Geonames Taxonomy  
g.add( (geonames, RDF.type, VoID.Dataset) )
#g.add( (UniProt, FOAF.homepage, URIRef('')) )
g.add( (geonames, dcterms.title, Literal('GeoNames')) )
g.add( (geonames, dcterms.description, Literal("""""")))

#DataEco - Geonames
g.add( (DataEcoGeonames, RDF.type, VoID.Linkset) )
g.add( (DataEcoGeonames, VoID.linkPredicate, OWL.sameAs) )
g.add( (DataEcoGeonames, VoID.target, DataEco) )
g.add( (DataEcoGeonames, VoID.target, geonames) )
g.add( (DataEcoGeonames, VoID.subset, DataEco) ) #quien publica los links
g.add( (DataEcoGeonames, VoID.triples, Literal('', datatype=XSD.int)) )
 
#print (g.serialize(format='pretty-xml'))
