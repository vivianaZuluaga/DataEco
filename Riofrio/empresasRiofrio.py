#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import maps, imgur, rioFrio, alcaldiaRiofrio
from lugaresRiofrio import g

# Esquema del grafo para empresas de la ruta del maíz.
def empresas(uri, nombre, tel, imagen, descripcion, direcc, email, webpage, mapa, uriatencion, abre, cierra):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
    
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )      
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), GR.name, Literal(nombre)) )
    g.add( (URIRef(uri), GR.description, Literal(descripcion)))
    g.add( (URIRef(uri), VCARD.tel, Literal(tel)) )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) 
    
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)) )
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Riofrio')) )
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
    
    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rioFrio.Empresas)))

empresas(
    'http://www.paginasamarillas.com.co/empresas/empresa-de-transporte-salonica-sa/riofrio-15722768',#uri
    'EMPRESA DE TRANSPORTE SALÓNICA S.A',#nombre
    '2008028',#tel
    imgur['JzqdDqD.jpg'],#img
    """Dedicada al transporte de pasajeros por vía terrestre, con sede en la ciudad de Tuluá.""",#desc
    'Cll 10 # 2 - 02, Salónica, Valle del Cauca',#dir
    'No disponible',#email
    'http://empresite.eleconomistaamerica.co/TRANSPORTES-SALONICA-SA.html',#pagina
    maps['shQcqeb18Kq'],#mapa
    'http://www.planetacolombia.com/empresa-de-transporte-salonica-sa-F150AC1041BD5',#uriatencion
    '05:00:00',#abre
    '20:00:00' #cierra
)

empresas(
    'http://www.indizze.co/hospital-kennedy-ese',
    'HOSPITAL KENEDY',
    '2268100, 2268101',
    imgur['wFLVGaW.png'],
    """Empresa social del estado que brinda servicios de baja complejidad, enfatizados en la promoción de la salud, la 
    prevención de la enfermedad y la calidad en la atención. Urgencias 24 horas.""",
    'Calle 7 # 10 - 65, Riofrío, Valle del Cauca',
    'kennedyese@hkriofrio.com',
    'http://www.hkriofrio.gov.co/',
    maps['AWe5VBCpMzB2'],
    alcaldiaRiofrio['tramites.shtml?apc=t-l1--&x=2719612'],
    '07:00:00',
    '17:00:00'
)

empresas(
    'http://www.informacion-empresas.co/Empresa_HACIENDA-NORMANDIA-SAS.html',
    'HACIENDA NORMANDIA SAS',
    '3162421352',
    imgur['zOeUtAu.png'],
    """Empresa privada fundada en el 1999 que cuenta actualmente con 60 empleados.""",
    'Km 14 Vía Tulua-Riofrío, Riofrío, Valle del Cauca',
    'No disponible',#Email
    'http://fichas.findthecompany.com.mx/l/130857814/Hacienda-Normandia-SAS-en-Riofrio',
    maps['ES2j7t5JST32'],
    'http://empresite.eleconomistaamerica.co/HACIENDA-NORMANDIA-SAS.html',
    '06:00:00',
    '19:00:00'
)

#print (g.serialize(format="pretty-xml"))

