#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, UMBEL, OWL
from utils.namespaces import rutaAnillo, rutaMaiz, rutaVueltaOriente, dbpedia, wikidata, eol, imgur, gbif, uniprot
from faunaAgricola import g

#g = Graph()

def flora(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3, linkURI):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang="es") ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang="la")) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang="es")) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Vegetal', lang="es")) )
    g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web
    
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF a DBpedia  
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF a UniProt
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Links externos
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) )
    
    g.add( ( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf'])) )

    
flora(
    rutaAnillo['Flora.rdf#passifloraTarminiana'],
    "CURUBO",
    "Passiflora tarminiana",
    """Planta enredadera de tallo cilíndrico pubescente, presenta flores color rosado pálido con blanco, corona de 
    filamentos vinotinto con blanco y estambres amarillos. El fruto, denominado curuba, es una baya oblonga de color 
    amarillo al madurar, rico en vitamina C.""",
    imgur['KvyxSz2.jpg'],
    dbpedia['Passiflora_tarminiana'],
    eol['5741930'],
	'https://es.wikipedia.org/wiki/Curuba',
	uniprot['483749'],
	gbif['3587792']
)

flora(
    rutaAnillo['Flora.rdf#solanumLycopersicum'],
    "TOMATERA",
    "Solanum lycopersicum",
    """Planta anual de tamaño muy variable tiene tallos ramificados con pelos cortos; el fruto (el tomate),  es una 
    baya de forma globosa y de unos 8 cms de diámetro, verde cuando es inmadura y que toma un color rojo intenso 
    con la maduración.""",
    imgur['pv31wH0.jpg'],
    dbpedia['Solanum_lycopersicum'],
    eol['392557'],
	'https://es.wikipedia.org/wiki/Solanum_lycopersicum',
	uniprot['4081'],
	gbif['2930137']
)
            
g.add( (rutaMaiz['Flora.rdf#citrusSinensis'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #naranjo
g.add( (rutaMaiz['Flora.rdf#capsicumAnnuum'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #aji
g.add( (rutaMaiz['Flora.rdf#cynodonPlectostachyus'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #pasto estrella
g.add( (rutaMaiz['Flora.rdf#caricaPapaya'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #papaya
g.add( (rutaMaiz['Flora.rdf#citrusNobilis'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #mandarina
g.add( (rutaMaiz['Flora.rdf#perseaAmericana'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #aguacate
g.add( (rutaMaiz['Flora.rdf#saccharumOfficinarum'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #caña
g.add( (rutaMaiz['Flora.rdf#passifloraEdulis'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #maracuya
g.add( (rutaMaiz['Flora.rdf#zeaMays'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #maiz
g.add( (rutaMaiz['Flora.rdf#mangiferaIndica'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #mango
g.add( (rutaMaiz['Flora.rdf#musaParadisiaca'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #platano
g.add( (rutaMaiz['Flora.rdf#citrusLimon'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #limon
g.add( (rutaMaiz['Flora.rdf#theobromaCacao'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #cacao
g.add( (rutaVueltaOriente['Flora.rdf#ingaEdulis'], UMBEL.isRelatedTo, URIRef(rutaAnillo['Flora.rdf']) )) #guama
    
    
#print(g.serialize(format='pretty-xml'))
