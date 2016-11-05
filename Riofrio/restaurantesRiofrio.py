#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import maps, imgur, rioFrio
from empresasRiofrio import g

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
    g.add( (URIRef(uriatencion), GR.closes, Literal(cierra, datatype=XSD.time)) )#hh:mm:ss
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Monday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Tuesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Wednesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Thursday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Friday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Saturday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Sunday) )

    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rioFrio.Restaurantes)))

restaurantes(
     'http://www.livevalledelcauca.com/tulua/restaurante-ecoparque-vayju.html',
     'RESTAURANTE VAYJÚ',
     """Ofrece delicias típicas de la comida Colombiana con las que seguro te deleitarás. En Vayjú encontrarás un 
     delicioso Sancocho de Gallina para que vengas y disfrutes acompañado de tu familia y amigos. Además no podía 
     faltar una buena Bandeja Paisa con chicharrón.""",
     '3146977558, 3176699094',
     'Km 6 Vía Riofrío - Salónica, Riofrío, Valle Del Cauca',
     'http://www.vayju.com/',
     imgur['X4X8uQh.jpg'],
     maps['nJPYDitXkRP2'],
     'http://www.eltiempo.com/archivo/documento/CMS-13708315',
     '09:00:00',
     '18:00:00'
)

#print (g.serialize(format="pretty-xml"))    
