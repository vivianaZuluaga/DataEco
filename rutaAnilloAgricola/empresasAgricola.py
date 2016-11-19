#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import rutaAnillo, facebook, twitter, imgur, maps, youtube
from alojamientosAgricola import g

#g = Graph()

def empresas(uri, nombre, tel, imagen, descripcion, direcc, email, webpage, mapa, uriatencion, abre, cierra, linkURI):
    if webpage != 'No disponible':
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
    
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )      
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang="es")) )
    g.add( (URIRef(uri), GR.description, Literal(descripcion, lang="es")))
    g.add( (URIRef(uri), VCARD.tel, Literal(tel)) )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) 
    
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)) )
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang="es")) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang="es")) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

    g.add( (URIRef(uri), GR.hasOpeningHoursSpecification, URIRef(uriatencion)))
    g.add( (URIRef(uriatencion), RDF.type, GR.OpeningHoursSpecification) )
    g.add( (URIRef(uriatencion), GR.opens, Literal(abre, datatype=XSD.time)) )#Se especifica el tipo de dato
    g.add( (URIRef(uriatencion), GR.closes, Literal(cierra, datatype=XSD.time)) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Monday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Tuesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Wednesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Thursday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Friday) )
    
    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaAnillo['Empresas.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("EMPRESAS", lang='es')))

empresas(
    rutaAnillo['Empresas.rdf#avicolaChica'],#uri
    'AVICOLA LA CHICA',#nombre
    '2303387',#tel
    imgur['iwFz4zG.jpg'],#imagen
    """Comercialización de huevos""",#descrip
    'Avícola - La Chica Vía a Tres Esquinas, Tuluá, Valle del Cauca',#direccion
    'No disponible',#email
    'No disponible',#webpage
    maps['dp6m5j9xDo62'],#mapa
    "http://directoriotelefonico.info/directorio/de/tulua/a/150",#uriatencion
    "08:00:00",#abre
    "18:00:00",#cierra
    facebook['pages/Avicola-La-Chica/375601145975612']
)

empresas(
    rutaAnillo['Empresas.rdf#comfandi'],#uri
    'SUPERMERCADO COMFANDI',#nombre
    '2310819',#tel
    imgur['ImKLnVA.png'],#imagen
    """Variedad de productos, calidad, promociones permanentes, atención amable y oportuna.""",#descrip
    'Calle 23 No. 7 - 11, Tuluá, Valle del Cauca',#direccion
    'No disponible',#email
    'http://www.comfandi.com.co',#webpage
    maps['pkTqvXMsgrj'],#mapa
    "http://www.bigpass.com.co/buscador/details.php?ide=125896",#uriatencion
    "08:00:00",#abre
    "18:00:00",#cierra
    facebook['supermercadosydrogueriascomfandi']
)

empresas(
    rutaAnillo['Empresas.rdf#ieOccidente'],#uri 
    'INSTITUCIÓN EDUCATIVA TÉCNICA OCCIDENTE',#nombre
    '0',#tel
    imgur['eC5RRwe.jpg'],#imagen
    """Espacio de socialización, en donde se amplían, ratifican o construyen nuevos conocimientos, comportamientos, 
    modos de relación y aceptación del otro. Ubicada frente a la capilla del Santo Aparecido.""",#descrip
    'Vía a Tres Esquinas, Tuluá, Valle del Cauca',#direccion
    'No disponible',#email
    'http://ietecnicaoccidente.tripod.com/',#webpage 
    maps['BUTrUuSDjCK2'],#mapa
    "www.occiportal.jimdo.com",#uriatencion
    "06:00:00",#abre
    "18:00:00",#cierra
    facebook['Institucion-Educativa-Tecnica-Occidente-134974479939448/']
)

empresas(
    rutaAnillo['Empresas.rdf#zoocriaderoSirena'],#uri 
    'ZOOCRIADERO DE AVESTRUCES LA SIRENA',#nombre
    '2257083',#tel
    imgur['SGXyLbc.png'],#imagen
    """Criadero de avestruces, comercialización de huevos y plumas. Ubicado en la Hacienda La Sirena.""",#descrip
    'La Palmera, Tuluá, Valle del Cauca',#direccion
    'No disponible',#email
    'http://www.cvc.gov.co',#webpage 
    maps['A3tVoWjpmMQ2'],#mapa
    rutaAnillo['Empresas/licenciaAvestruces.pdf'],#uriatencion
    "07:00:00",#abre
    "18:00:00",#cierra
    youtube['_kQesussw3k']
)

empresas(
    rutaAnillo['Empresas.rdf#cubatas'],#uri 
    'MAMÁ CUBATAS',#nombre
    '3165131438',#tel
    imgur['RBt0z5d.jpg'],#imagen
    """Un lugar diferente con espacios sofisticados.""",#descrip
    'Bocas de Tuluá, Tuluá, Valle del Cauca',#direccion Carrera 26A 40 - 43
    'No disponible',#email
    'No disponible',#webpage 
    maps['eEKb1nRc4Fz'],#mapa
    "http://eventerbee.com/event/el-caribefunk-en-tulua-18-de-junio,961838740604403",#uriatencion
    "18:00:00",#abre
    "01:00:00",#cierra
    facebook['Mama-Cubatas-1684533791806093/']
)

#print (g.serialize(format='pretty-xml'))
