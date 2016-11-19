#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import maps, imgur, rioFrio, twitter, facebook, alcaldiaRiofrio
from empresasRiofrio import g

#g = Graph()

def restaurantes(uri, nombre, menu, telefono, direccion, webpage, imagen, mapa, uriatencion, abre, cierra, linkURI):
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

    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rioFrio['Restaurantes.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("RESTAURANTES", lang='es')))

restaurantes(
     rioFrio['Restaurantes.rdf#restauranteVayju'],#uri
     'RESTAURANTE VAYJÚ',#nombre
     """Ofrece delicias típicas de la comida colombiana, encontrarás delicioso sancocho de gallina para que 
     disfrutes acompañado de tu familia y amigos. Además buena bandeja paisa con chicharrón.""",#menu
     '3146977558, 3176699094',#tel
     'Km 6 Vía Riofrío - Salónica, Riofrío, Valle Del Cauca',#direccion
     'http://www.vayju.com/',#webpage
     imgur['X4X8uQh.jpg'],#imagen
     maps['nJPYDitXkRP2'],#mapa
     'http://www.eltiempo.com/archivo/documento/CMS-13708315',#uriAtencion
     '09:00:00',#abre
     '18:00:00',#cierra
     'http://www.livevalledelcauca.com/tulua/restaurante-ecoparque-vayju.html'#link
)

restaurantes(
     rioFrio['Restaurantes.rdf#juanValeja'],#uri
     'ECOCLUB JUAN VALEJA',#nombre
     """Restaurante, hospedaje, piscina natural, cabañas, salón de eventos, juegos de mesa e infantiles.
     Ubicado en la vereda La Cristalina del corregimiento de Salónica.""",#menu
     '3183602632, 3177495431',#tel
     'Salónica, Riofrío, Valle Del Cauca',#direccion
     'No disponible',#webpage
     imgur['TJ1BTbf.jpg'],#imagen
     maps['cWmFqvmx1JM2'],#mapa
     twitter['797161428318908416'],#uriAtencion
     '09:00:00',#abre
     '18:00:00',#cierra
     facebook['Ecoclubjuanvaleja']#link
)

restaurantes(
     rioFrio['Restaurantes.rdf#mexicana'],#uri
     'PAO A LA MEXICANA',#nombre
     """Comida mexicana""",#menu
     '3183786925',#tel
     'Calle 5B # 6 - 75 Riofrío, Valle Del Cauca',#direccion
     'No disponible',#webpage
     imgur['ZU9mtJD.jpg'],#imagen
     maps['3ZXre5FEb5k'],#mapa
     twitter['797164691705499648'],#uriAtencion
     '18:00:00',#abre
     '00:00:00',#cierra
     facebook['Paoalamexicana']#link
)

restaurantes(
     rioFrio['Restaurantes.rdf#todoADosqui'],#uri
     'TODO A DOSQUI',#nombre
     """Comida rápida""",#menu
     '3128666235',#tel
     'Calle 7 # 11 - 02 Riofrío, Valle Del Cauca',#direccion
     'No disponible',#webpage
     imgur['mxTbeTv.jpg'],#imagen
     maps['Cr6HvE8nFex'],#mapa
     twitter['797171210090070020'],#uriAtencion
     '18:00:00',#abre
     '00:00:00',#cierra
     facebook['Todo-A-Dosqui-852459148181204']#link
)

restaurantes(
     rioFrio['Restaurantes.rdf#fritanga'],#uri
     'PARQUE PRINCIPAL',#nombre
     """Puestos con comida típica colombiana: bofe ahumado, papas aborrajadas, empanadas, chorizos, 
     costillas de cerdo ahumadas y bebidas refrescantes.""",#menu
     '0',#tel
     'Riofrío, Valle Del Cauca',#direccion
     'No disponible',#webpage
     imgur['crBZG8Y.jpg'],#imagen
     maps['ivrQVkU8C2p'],#mapa
     alcaldiaRiofrio['index.shtml?apc=bjxx-3-&x=2720614'],#uriAtencion
     '10:00:00',#abre
     '',#cierra
     'https://www.elvalleestaenvos.com/el-parche-imperdible-de-rio-en-el-valle-del-cauca/'#link
)

#print (g.serialize(format="pretty-xml"))    
