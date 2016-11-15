#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import rutaVueltaOriente, facebook, twitter, imgur, maps, youtube
from alojamientosVueltaOriente import g


def empresas(uri, nombre, tel, imagen, descripcion, direcc, email, webpage, mapa, uriatencion, abre, cierra, linkURI):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
    
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )      
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), GR.description, Literal(descripcion, lang='es')))
    g.add( (URIRef(uri), VCARD.tel, Literal(tel)) )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) 
    
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)) )
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
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
    
    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaVueltaOriente['Empresas.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo

empresas(
    rutaVueltaOriente['Empresas.rdf#escuelaPolicia'],#uri
    'ESCUELA DE POLICÍA SIMÓN BOLÍVAR',#nombre
    '2257192 ext. 130',#tel
    imgur['PCNkCT0.jpg'],#imagen
    """Centro de formación policial del suroccidente colombiano, tiene como objetivo principal, capacitar a los futuros policías, 
    a través de un proyecto educativo institucional, dirigido a satisfacer las necesidades de seguridad y convivencia 
    ciudadana. Ubicada en el Km 1 vía al corregimiento de La Rivera""",#descrip
    'Tuluá, Valle del Cauca',#direccion
    'esbol.oac@policia.gov.co',#email
    'http://policia.seedlabs.co/escuelas/simon-bolivar',#webpage
    maps['GgVE6MRkP5z'],#mapa
    youtube['iSA4bUzyzFs'],#uriatencion
    "07:00:00",#abre
    "18:00:00",#cierra
    facebook['pages/Escuela-de-Policia-Simon-Bolivar/334490836608164']
)

empresas(
    rutaVueltaOriente['Empresas.rdf#univalle'],#uri
    'UNIVERSIDAD DEL VALLE SEDE TULUÁ',#nombre
    '2241816',#tel
    imgur['my7qVD9.jpg'],#imagen
    """Universidad pública considerada la principal institución de educación superior del suroccidente del país.""",#descrip
    'Calle 43 No 43 - 33, Tuluá, Valle del Cauca',#direccion
    'academica.tulua@correounivalle.edu.co',#email
    'http://tulua.univalle.edu.co/',#webpage
    maps['V8JRNVrhLus'],#mapa
    youtube['3o_g3l1iC_4'],#uriatencion
    "08:00:00",#abre
    "17:00:00",#cierra
    facebook['UnivalleSedeTulua06/']
)

empresas(
    rutaVueltaOriente['Empresas.rdf#casaAbuelos'],#uri
    'CASA DE LOS ABUELOS ALONSO LOZANO GUERRERO',#nombre
    '2242194, 2255093, 3155560047',#tel
    imgur['tT2IN04.jpg'],#imagen
    """Entidad sin ánimo de lucro que atiende en la actualidad adultos mayores en condición de vulnerabilidad familiar, social y 
    económica, siendo la institución encargada de satisfacer sus necesidades básicas. Ubicada en el Km 2 vía al corregimiento de 
    La Rivera.""",#descrip
    'Tuluá, Valle del Cauca',#direccion
    'No disponible',#email
    'No disponible',#webpage
    maps['x6F3d8PftmR2'],#mapa
    youtube['6tMqqSnkDxQ'],#uriatencion
    "08:00:00",#abre
    "16:00:00",#cierra
    facebook['centrodebienestardelanciano.casadelosabuelos']
)

empresas(
    rutaVueltaOriente['Empresas.rdf#viveroElJardin'],#uri
    'VIVERO EL JARDÍN DE MI CASA',#nombre
    '3154924598, 3177365775',#tel
    imgur['XYu6NOk.jpg'],#imagen
    """Para toda ocasión regala un recuerdo que perdure. Plantas ornamentales, arboles frutales, orquídeas, palmas y
    bromelias.""",#descrip
    'La Marina, Valle del Cauca',#direccion
    'No disponible',#email
    'No disponible',#webpage
    maps['V6bajHY3FTs'],#mapa
    facebook['Vivero-el-jardin-de-mi-casa-644309525690362/'],#uriatencion
    "08:00:00",#abre
    "16:00:00",#cierra
    "https://www.youtube.com/watch?v=OhTiILsaCrw"
)

#print (g.serialize(format="pretty-xml"))
