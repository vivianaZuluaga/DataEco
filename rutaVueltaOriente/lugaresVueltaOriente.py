#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import CRUZAR, VCARD, UMBEL
from utils.namespaces import rutaVueltaOriente, facebook, youtube, maps, twitter, imgur
from floraVueltaOriente import g


def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa, linkURI): 
    if video != "No disponible":
        g.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia 
                  
    g.add( (URIRef(uri), RDF.type, VCARD.Location) )
    g.add( (URIRef(uri), FOAF.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), RDFS.comment, Literal(descripcion, lang='es')) )
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) #agente
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) #revisar
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )
    
    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaVueltaOriente['Lugares.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    
lugares(
    rutaVueltaOriente['Lugares.rdf#chagualos'],#uri
    'LA RESERVA NATURAL DE LA SOCIEDAD CIVIL LOS CHAGUALOS',#nombre
    """Es un área natural protegida dedicada a la conservación, investigación, educación ambiental, ecoturismo, y agroecología, 
    su ecosistema principal hace parte del bosque subandino. Ubicada a 15.5 kilómetros de la ciudad de Tuluá y a 3 Kilómetros 
    del casco urbano del corregimiento de La Marina.""",#descripcion
    'La Marina, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'reservachagualos@gmail.com',#email
    imgur['Auduk3K.jpg'],#imagen
    youtube['8hUawerN5Ek'],#video
    maps['DXSZCo17J432'],#mapa
    facebook['reserva.chagualos']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#laRochela'],#uri
    'LA ROCHELA',#nombre
    """Ofrece servicio de camping, piscina de aguas naturales alimentadas por una de las quebradas de la zona, es ideal para 
    familias y grupos, cuenta con sala de juegos de mesa, cancha de vóley playa, alquiler de caballos y zonas verdes. Ubicada en el 
    Km 8 de la vía.""",#descripcion
    'Vía La Marina - Tuluá, Valle del Cauca',#direccion
    '3152253329, 3185344484, 3155079632',#telefono
    'balneariolarochela@gmail.com',#email
    imgur['unia8WG.jpg'],#imagen
    'No disponible',#video
    maps['mRy7QrqNvqx'],#mapa
    facebook['La-Rochela-612135438799528']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#tresPiedras'],#uri
    'BALNEARIO TRES PIEDRAS',#nombre
    """Ofrece servicios de alimentos y bebidas, recreación, espacios de práctica de motocross, canchas de voley playa, alquiler 
    de caballos, todo esto se disfruta con el río que pasa por este establecimiento deleitando con sus naturales y puras aguas a 
    sus visitantes.""",#descripcion
    'La Marina, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'No disponible',#email
    imgur['nyr3AXR.jpg'],#imagen
    'No disponible',#video
    maps['4VpMavgHgTx'],#mapa
    facebook['pages/Tres-Piedras-La-Marina/1401175110175669']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#moralito'],#uri
    'MORALITO',#nombre
    """Cuenta con espacios para la integración familiar y de grupos, ofrece recreación, piscinas naturales, servicio de alimentos 
    y bebidas, juegos infantiles, kioscos, parqueadero.""",#descripcion
    'La Marina, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'No disponible',#email
    imgur['nyC1cgz.jpg'],#imagen
    'No disponible',#video
    maps['e3qMhtrL66o'],#mapa
    facebook['pages/La-Marina-Moralito/596105267145768']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#parquePrincipal'],#uri
    'PARQUE PRINCIPAL',#nombre
    """Cuenta con polideportivo cubierto, juegos infantiles, establecimiento de alimentos y bebidas, plaza de mercado, donde 
    los domingos los agricultores y campesinos ponen en venta la producción de carnes, provenientes de las fincas cercanas, 
    además es el punto de encuentro de los habitantes y un ambiente esparcimiento para sus visitantes. Ubicado frente a la iglesia 
    y la estación de policía.""",#descripcion
    'La Marina, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'No disponible',#email
    imgur['GErJR9N.jpg'],#imagen
    'No disponible',#video
    maps['5S6Po9VY1tC2'],#mapa
    facebook['La-Marina-Tulua-Valle-Ecoturismo-y-Diversion-102570483183016/']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#elPicacho'],#uri
    'CERRO EL PICACHO',#nombre
    """Sitio de peregrinación, cada año por la misma fecha de mayo, cientos de Tulueños suben. Se puede observar un lindo amanecer 
    o un hermoso atardecer. Se practican parapente, paracaidismo, ciclismo.""",#descripcion
    'El Picacho, Tuluá, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'No disponible',#email
    imgur['RNN9f6T.jpg'],#imagen
    youtube['BYkSVIzh5CY'],#video
    maps['Y7rJbfcAxcy'],#mapa
    "http://www.eltabloide.com.co/un-picacho-lleno-de-mitos-y-leyendas/"
)

lugares(
    rutaVueltaOriente['Lugares.rdf#parqueLaMoralia'],#uri
    'PARQUE PRINCIPAL LA MORALIA',#nombre
    """Cuenta con polideportivo cubierto, juegos infantiles, monumento a las víctimas.""",#descripcion
    'La Moralia, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'No disponible',#email
    imgur['kkgKuhQ.jpg'],#imagen
    youtube['KCifoTh--d0'],#video
    maps['k9zJoVNP4L82'],#mapa
    twitter['764645876329512961']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#coodeco'],#uri
    'COODECO O BRISAS DEL RÍO MORALES',#nombre
    """Balneario con aguas naturales.""",#descripcion
    'La Marina, Valle del Cauca',#direccion
    '0',#telefono No disponible
    'No disponible',#email
    imgur['hp4KyVh.jpg'],#imagen
    'No disponible',#video
    maps['MFTuskB4DXN2'],#mapa
    facebook['pages/Coodeco-La-Marina-Tulua-Valle/330765627124567']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#ranchoLasPalmas'],#uri
    'RANCHO LAS PALMAS',#nombre
    """Lugar de encuentro en donde se llevan a cabo diversos eventos, cuenta con pista de ciclomontañismo. Ubicado 
    en el Km 1 detrás del Centro Comercial Tuluá La 14.""",#descripcion
    'La Rivera, Tuluá Valle del Cauca',#direccion
    '2243939, 3155693615',#telefono
    'No disponible',#email
    imgur['DKmsfRt.jpg'],#imagen
    youtube['sVlkViwdHHA'],#video
    maps['eMjWbhVFiPw'],#mapa
    facebook['pages/Rancho-Las-Palmas/246671912037940']
)

lugares(
    rutaVueltaOriente['Lugares.rdf#lasMarias'],#uri
    'CENTRO RECREACIONAL LAS MARÍAS',#nombre
    """Ofrece servicios de alojamiento en cabañas, zona de camping, restaurante, piscina, sauna, parqueadero gratis, 
    zona WIFI. Excelente lugar para compartir en familia por su tranquilidad y espectacular relación con la naturaleza. 
    Espacios aptos para eventos empresariales. Ubicado a 15 minutos de Tuluá.""",#descripcion
    'La Moralia, Valle del Cauca',#direccion
    '3167796220, 3188001754',#telefono
    'visitalasmarias@gmail.com',#email www.visitalasmarias.com
    imgur['wttl4ey.jpg'],#imagen
    'No disponible',#video
    maps['vyuRs9SLc4G2'],#mapa
    facebook['LasMariasValle/']
)

#print(g.serialize(format='pretty-xml'))
