#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import rutaVueltaOriente, facebook, maps, twitter, imgur
from lugaresVueltaOriente import g

#g = Graph()

def restaurantes(uri, nombre, menu, telefono, direccion, webpage, imagen, mapa, uriatencion, abre, cierra, linkURI):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
            
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), GR.description, Literal(menu, lang='es')))
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono)) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))
    g.add( (URIRef(uri), GR.hasOpeningHoursSpecification, URIRef(uriatencion)) )
     
    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )

    #Horario de atencion
    g.add( (URIRef(uriatencion), RDF.type, GR.OpeningHoursSpecification) )
    g.add( (URIRef(uriatencion), GR.opens, Literal(abre, datatype=XSD.time)) )#Se especifica el tipo de dato
    g.add( (URIRef(uriatencion), GR.closes, Literal(cierra, datatype=XSD.time)) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Monday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Tuesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Wednesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Thursday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Friday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Saturday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Sunday) )

    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaVueltaOriente['Restaurantes.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("RESTAURANTES", lang='es')))


restaurantes(
    rutaVueltaOriente['Restaurantes.rdf#elMirador'],#uri
    'EL MIRADOR',#nombre
    """Restaurante campestre""",#descripcion
    '0',#telefono No disponible
    'Vía La Marina, Valle del Cauca',#direccion
    'No disponible',#webpage
    imgur['oJ8gmA9.jpg'],#imagen
    maps['WZFtPETEM122'],#mapa
    twitter['797811224356519936'],#uriatencion
    "08:00:00",#abre
    "19:00:00",#cierra
    facebook['pages/Restaurante-El-Mirador-Via-La-Marina/600740703382784']
)

restaurantes(
    rutaVueltaOriente['Restaurantes.rdf#ranchoJ'],#uri
    'RANCHO J',#nombre
    """Piscina para niños y adultos, kiosco pequeño para eventos, senderos ecológicos, cancha de fútbol, alquiler de caballos, 
    interacción con animales de granja: patos, gallinas, ganzos, cabras y otros. Delicioso sancocho de gallina. Ubicado 
    sobre el Km 2 de la vía.""",#descripcion
    '3155793565, 3187122567',#telefono
    'El Picacho, Tuluá, Valle del Cauca',#direccion
    'No disponible',#webpage
    imgur['mvSK4Zm.jpg'],#imagen
    maps['go382c2uXfL2'],#mapa
    rutaVueltaOriente['Restaurantes/ranchoJ.mp4'],#uriatencion
    "10:00:00",#abre
    "18:00:00",#cierra
    facebook['rancho.jlarivera']
)

restaurantes(
    rutaVueltaOriente['Restaurantes.rdf#paradorLaIberia'],#uri
    'PARADOR LA IBERIA',#nombre
    """Eventos, recreación, platos a la carta, postres, café, bar. Ubicado en el km 7  de la vía.""",#descripcion
    '0',#telefono No disponible
    'La Marina, Valle del cauca',#direccion
    'No disponible',#webpage
    imgur['TyZ7QSv.jpg'],#imagen
    maps['UwPdvJvFAin'],#mapa
    rutaVueltaOriente['Restaurantes/paradorIberia.mp4'],#uriatencion
    "09:00:00",#abre
    "20:00:00",#cierra
    twitter['765348363785175040']
)

#print (g.serialize(format="pretty-xml"))
