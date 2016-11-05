#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import rutaAnillo, facebook, maps, imgur
from faunaAgricola import g


def restaurantes(uri, nombre, menu, telefono, direccion, webpage, imagen, mapa, uriatencion, abre, cierra):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
            
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang="es")) )
    g.add( (URIRef(uri), GR.description, Literal(menu, lang="es")))
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono)) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))
    g.add( (URIRef(uri), GR.hasOpeningHoursSpecification, URIRef(uriatencion)) )
     
    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang="es")) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang="es")) )
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

    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaAnillo.Restaurantes)))


restaurantes(
    facebook['pages/Parador-Narino/1500318653527283'],#uri
    'RESTAURANTE Y PARADOR NARIÑO',#nombre
    """Sancocho de gallina, platos típicos a la carta, se atienden reuniones sociales.""",#descripcion
    '2315868',#telefono
    'Vía Nariño, Tuluá, Valle del Cauca',#direccion
    'No disponible',#webpage
    imgur['q1ovJTd.jpg'],#imagen
    maps['jXWsgvVddiE2'],#mapa
    "http://www.ciudadguru.com.co/empresas/restaurante-y-parador-narino/tulua/15724654",#uriatencion
    "00:00:00",#abre
    "17:00:00"#cierra
)

#print (g.serialize(format="pretty-xml"))
