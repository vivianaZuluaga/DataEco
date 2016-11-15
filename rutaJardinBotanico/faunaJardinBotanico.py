#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, CRUZAR, UMBEL, OWL
from utils.namespaces import rutaJardin, rutaMaiz, rutaVueltaOriente, dbpedia, wikidata, imgur, eol, gbif, uniprot
from floraJardinBotanico import g

#g = Graph()

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3, linkURI):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang='es') ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang='la')) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang='es')) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Animal', lang='es')) )  
    g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web
    
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF a DBpedia  
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF a UniProt
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Links externos
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) )
    
    g.add( ( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaJardin['Fauna.rdf'])) )
 
 
fauna(
	rutaJardin['Fauna.rdf#attaCephalotes'],
	'HORMIGAS CORTADORAS DE HOJAS',
	'Atta cephalotes',
	"""Cultivan hongos alimentándolos con material de las plantas recién cortadas; los hongos son utilizados
	 para alimentar a las larvas y a los adultos. Sus colonias se dividen en castas, basadas mayormente 
	por su tamaño, realizando funciones variadas. Son endémicas de centro y sur América.""",
	imgur['4h2ENLK.jpg'],
	dbpedia['Atta_cephalotes'],
	eol['452188'],
	'https://es.wikipedia.org/wiki/Hormigas_cortadoras_de_hojas',
	uniprot['12957'],
	gbif['5035748']
)

fauna(
	rutaJardin['Fauna.rdf#apterostigmaDentigerum'],
	'HORMIGA',
	'Apterostigma dentigerum',
	"""Pertenece al género de hormigas del Nuevo Mundo de la subfamilia Myrmicinae. Se encuentra en una variedad de 
	hábitats, incluyendo bosque húmedo, bosque seco y bosque montano.""",
	imgur['7AKWq7p.jpg'],
	wikidata['Q9626579'],
	eol['397229'],
	'https://en.wikipedia.org/wiki/Apterostigma',
	uniprot['257670'],
	gbif['1316978']
)

fauna(
	rutaJardin['Fauna.rdf#aztecaInstabilis'],
	'HORMIGA',
	'Azteca instabilis',
	"""Forma nidos en los troncos huecos de los árboles que tienen una gran grieta o fisura en la base. Las colonias 
	pueden vivir durante largos periodos de tiempo.""",
	imgur['tw0dYMW.jpg'],
	wikidata['Q13432862'],
	eol['473991'],
	'http://www.antwiki.org/wiki/Azteca_instabilis',
	uniprot['602870'],
	gbif['5035731']
)

fauna(
	rutaJardin['Fauna.rdf#brachymyrmexHeeri'],
	'HORMIGA',
	'Brachymyrmex heeri',
	"""Pequeñas trabajadoras (1.2 - 2mms) con nueve antenas segmentadas. El color varía de amarillo a marrón. Anida 
	bajo piedras y otros objetos, a menudo en áreas perturbadas.""",
	imgur['tQlvBcx.jpg'],
	wikidata['Q9663061'],
	eol['472945'],
	'http://www.antwiki.org/wiki/Brachymyrmex_heeri',
	uniprot['604545'],
	gbif['1317348']
)

fauna(
	rutaJardin['Fauna.rdf#camponotusNovogranadensis'],
	'HORMIGA',
	'Camponotus novogranadensis',
	"""Esta especie se ha encontrado recientemente, es de color oscuro, no brillante y 
	pequeña (las mayores tienen aproximadamente 5 mms de largo). Forma sus nidos en madera muerta o tallos huecos.""",
	imgur['FSHri6w.jpg'],
	wikidata['Q13452133'],
	eol['467057'],
	'http://www.antwiki.org/wiki/Camponotus_novogranadensis',
	uniprot['605724'],
	gbif['5034665']
)

fauna(
	rutaJardin['Fauna.rdf#camponotusSenex'],
	'HORMIGA',
	'Camponotus senex',
	"""Es muy común en hábitats de bosques húmedos. Forma sus nidos en la vegetación abierta de matorral, 
	carreteras, ramas muertas que van desde tallos estrechos de vid a ramas relativamente grandes.""",
	imgur['eoWYXMB.jpg'],
	wikidata['Q13452348'],
	eol['398450'],
	'http://www.antwiki.org/wiki/Camponotus_senex',
	uniprot['606022'],
	gbif['5033118']
)

fauna(
	rutaJardin['Fauna.rdf#crematogasterCarinata'],
	'HORMIGA',
	'Crematogaster carinata',
	"""Pequeña e inofensiva que a menudo coloniza ramas de árboles. Parece ser capaz de mantener las colonias sin salir de 
	su árbol de origen.""",
	imgur['fewSAes.jpg'],
	dbpedia['Crematogaster_carinata'],
	eol['407090'],
	'http://www.antwiki.org/wiki/Crematogaster_carinata',
	uniprot['1720225'],
	gbif['1324354']
)
   
g.add( (rutaVueltaOriente['Fauna.rdf#carolliaPerspicillata'], UMBEL.isRelatedTo, URIRef(rutaJardin['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#glossophagaSoricina'], UMBEL.isRelatedTo, URIRef(rutaJardin['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#bosTaurus'], UMBEL.isRelatedTo, URIRef(rutaJardin['Fauna.rdf'])) )
