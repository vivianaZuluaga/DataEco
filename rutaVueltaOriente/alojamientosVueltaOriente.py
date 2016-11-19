#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, ACCO, UMBEL
from utils.namespaces import rutaVueltaOriente, facebook, twitter, alcaldiaTulua, imgur, maps, youtube, valleCompras
from rutaVueltaOriente import g

#g = Graph()

def alojamientos(uri, nombre, webpage, telefono, email, direcc, mapa, descripcion, uriRoom, uriValue, 
    uriBed, numHabitaciones, numCamas, imagen, linkURI):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)))   
            
    g.add( (URIRef(uri), RDF.type, ACCO.Hotel))#Cambiar por casa
    g.add( (URIRef(uri), RDF.type, GR.Individual) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), GR.description, Literal(descripcion, lang='es')) )
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono)))
    g.add( (URIRef(uri), VCARD.email, Literal(email)))
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

    #Horario de Atención
    g.add( (URIRef(uri), ACCO.feature, ACCO.AccommodationFeature) )
    g.add( (ACCO.AccommodationFeature, ACCO.availabilityTimes, Literal("24 Horas")) )

    #Habitaciones
    g.add( (URIRef(uriRoom), RDF.type, ACCO.HotelRoom))
    g.add( (URIRef(uriRoom), RDF.type, GR.SomeItems) )
    g.add( (URIRef(uriRoom), ACCO.partOf, URIRef(uri)) )

    #Value
    g.add( (URIRef(uriValue), RDF.type, GR.QuantitativeValue))
    g.add( (URIRef(uriRoom), ACCO.numberOfRooms, URIRef(uriValue)) )
    g.add( (URIRef(uriValue), GR.hasUnitOfMeasurement, Literal("C62"))) #No hay unidades
    g.add( (URIRef(uriValue), GR.hasValue, Literal(numHabitaciones, datatype=XSD.int)))

    #Camas
    g.add( (URIRef(uriBed), RDF.type, ACCO.BedDetails))
    g.add( (URIRef(uriRoom), ACCO.bed, URIRef(uriBed)))
    g.add( (URIRef(uriBed), ACCO.quantity, Literal(numCamas, datatype=XSD.int)))
    
    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaVueltaOriente['Alojamientos.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("ALOJAMIENTOS", lang='es')))
    

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#laLinda'],#uri
    "FINCA LA LINDA",#nombre
    "http://www.turismoboga.com/fincalin.html",#webpage
    "3176369765, 2242759, 2257332",#telefono
    "mivalledecompras.com@gmail.com",#email
    "La Marina, Valle del Cauca",#direccion
    maps['HnkCTRqcw482'],#mapa
    """Piscina para adultos e infantil, sauna, cancha de fútbol, tejo, ping pong, sapo, salón de villar, zonas verdes, 
    juegos infantiles, juegos de mesa, horno, fogón de leña, estufa a gas, parqueadero con 
    capacidad para 20 vehículos.""",#descripcion
    facebook['finca.lalinda.1'],#uriroom
    valleCompras['villalinda tulua valle/index.html'],#urivalue
    imgur['ajLSDOw.jpg'],#uriBed
    "6",#numHab
    "16",#numCamas
    imgur['0MEtcXS.jpg'],#imagen
    youtube['ZXgZCMzGCog']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#laCantera'],#uri
    "LA CANTERA",#nombre
    "No disponible",#webpage
    "3113242282, 3174892540",#telefono
    "No disponible",#email
    "Vía al Picacho, Tuluá, Valle del Cauca",#direccion
    maps['Ck73WX3L5Tu'],#mapa
    """Cómodas habitaciones, cabañas, zona de camping, lago, kiosko para conferencias, seminarios y eventos, pista de baile, 
    zona de BBQ, fogon de leña. Ofrece al turista senderos ecológicos para caminatas al aire libre, también rutas de 
    ciclomontañismo para el viajero intrépido, visita al alto de La Cruz y el Jardín Botánico. Ubicada en el Km 1 Doble Calzada""",#descripcion
    imgur['ZRdVYRs.jpg'],#uriroom
    facebook['pages/Finca-La-Cantera-Tulua/212484658901980'],#urivalue
    imgur['JZIBlhm.jpg'],#uriBed
    "",#numHab
    "",#numCamas
    imgur['FwIvEpW.jpg'],#imagen
    facebook['fincahotellacantera/']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#villaLina'],#uri
    "VILLA LINA",#nombre
    "No disponible",#webpage
    "3152630133, 2242946",#telefono
    "mivalledecompras.com@gmail.com",#email
    "La Iberia, Valle del Cauca",#direccion
    maps['t7DczPasTxK2'],#mapa
    """Sitio campestre para recrearse y descansar, tiene una amplia zona verde, pasesos ecológicos a caballo, fogón de leña, 
    sitio de juegos y más. Ideal para sus eventos empresariales o familiares, los fines de semana o retiros espirituales. Ubicada
    a 15 minutos de Tuluá.""",#descripcion
    imgur['d690JRu.jpg'],#uriroom
    valleCompras['finca villa lina en la iveria/index.html'],#urivalue
    imgur['NwTwTCv.jpg'],#uriBed
    "3",#numHab
    "6",#numCamas
    imgur['KwJhf9j.jpg'],#imagen
    twitter['763489482062561282']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#bellaVista'],#uri
    "FINCA BELLA VISTA",#nombre
    "No disponible",#webpage
    "3163211199, 3182262773, 2242590",#telefono
    "No disponible",#email
    "La Marina, Valle del Cauca",#direccion
    maps['rzFdYDP41v72'],#mapa
    """Cuenta con capacidad para ubicar en la vivienda a 10 personas, una amplia zona de camping que cobija a 
    más de 30 campistas, salón para 50 personas. En este espacio puedes disfrutar de la interacción directa con la naturaleza 
    mediante un recorrido por un agradable sendero ecológico acompañado por una encantadora quebrada.""",#descripcion
    alcaldiaTulua['1515736'],#uriroom
    imgur['6ZNSZmA.jpg'],#urivalue
    "http://n4.sdlcdn.com/imgs/b/u/r/bed-de330.jpg",#uriBed
    "5",#numHab
    "10",#numCamas
    imgur['vPufIKq.jpg'],#imagen
    twitter['763493126220775424']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#laIsabela'],#uri
    "LA ISABELA",#nombre
    "No disponible",#webpage
    "3185935231",#telefono
    "No disponible",#email
    "Vía La Marina, Valle del Cauca",#direccion
    maps['7zjBQ9xerZ82'],#mapa
    """Capacidad de alojamiento para 30 personas, cuenta con un sendero que va acompañado del río Morales, amplias zonas verdes, 
    tiene a disposición de sus visitantes diversos juegos para compartir en familia. Ubicada a 5 minutos del balneario las Marías.""",#descripcion
    alcaldiaTulua['1515737'],#uriroom
    "https://www.datos.gov.co/Cultura/Fincas-y-casas-campestres-Municipio-de-Tulu-/x5f2-nrzc/data",#urivalue
    "https://famsa_imagenes2.storage.googleapis.com/155711024TITANIO_perfil.jpg",#uriBed
    "",#numHab
    "30",#numCamas
    imgur['tx2q1oE.jpg'],#imagen
    twitter['763526953987080192']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#villaAgaton'],#uri
    "FINCA CAMPESTRE VILLA AGATÓN",#nombre
    "No disponible",#webpage
    "3188218334, 3166245893, 2243191",#telefono
    "No disponible",#email
    "Vía La Marina, Valle del Cauca",#direccion
    maps['y6hmmAMyizD2'],#mapa
    """Cuenta con una cabaña para 20 personas, jacuzzi, turco, voley playa, asador, kiosco tipo discoteca, fogón de leña, mini 
    fútbol, TV satelital, está totalmente amoblada. Ubicada a 10 minutos de Tuluá.""",#descripcion
    facebook['pages/En-Villa-Agaton-La-Iberia/483913585039109'],#uriroom
    "http://www.livevalledelcauca.com/tulua/finca-campestre-villa-agaton.html",#urivalue
    "http://corona.vteximg.com.br/arquivos/ids/161827-1000-1000/637207502000_F1.jpg",#uriBed
    "1",#numHab
    "20",#numCamas
    imgur['5d3r7ge.jpg'],#imagen
    facebook['villaagaton/']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#laUmbria'],#uri
    "LA UMBRIA CASA DE RETIROS Y CONVIVENCIAS",#nombre
    "No disponible",#webpage
    "2243075, 2255606",#telefono
    "diocebuga@hotmail.com",#email
    "La Rivera, Tuluá, Valle del Cauca",#direccion
    maps['pQ1K5DD1U642'],#mapa
    """En ambiente campestre y natural que permite el silencio y el recogimiento. La Diócesis de Buga ofrece a sus visitantes 
    este lugar con sencillas, pero confortables habitaciones, áreas de zonas verdes, amplios corredores, salón de conferencias 
    o reuniones, baños sociales, servicio de comedor, entre otros.""",#descripcion
    facebook['pages/La-Umbria/207406979406042'],#uriroom
    "http://www.diocesisdebuga.org/index.shtml?apc=f---;1;-;-;&x=8968",#urivalue
    imgur['mDUSPGF.jpg'],#uriBed
    "",#numHab
    "",#numCamas
    imgur['Mcr7R3w.jpg'],#imagen
    facebook['pages/Casa-De-Retiro-La-Umbria-Tulua/854376261242075']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#codecot'],#uri
    "ANTIGUO CODECOT",#nombre
    "No disponible",#webpage
    "2260752",#telefono
    "No disponible",#email
    "Vía La Marina, La Moralia, Valle del Cauca",#direccion
    maps['Y6B3L5Msdzv'],#mapa
    """Ofrece pasadías y hospedaje. Capacidad para 14 personas, zona de camping, río y charcos, kiosco, senderos ecológicos, 
    huerta casera, juegos infantiles, zona para asados, interacción con animales de granja.""",#descripcion
    "http://www.tc.columbia.edu/housing/guest-and-conference-housing/guest-housing/rooms/ghRoom.jpg",#uriroom
    alcaldiaTulua['1475499'],#urivalue
    "http://www.flatdogscamp.com/wp-content/uploads/2011/08/Chalet-room.jpg",#uriBed
    "6",#numHab
    "8",#numCamas
    imgur['KpLCwSW.jpg'],#imagen
    twitter['763574753894498304']
)

alojamientos(
    rutaVueltaOriente['Alojamientos.rdf#santSebastian'],#uri
    "CHALET SANT SEBASTIAN",#nombre
    "No disponible",#webpage
    "3154924598",#telefono
    "No disponible",#email
    "La Marina, Valle del Cauca",#direccion
    maps['iz6Ti1YCmQx'],#mapa
    """Ofrece la oportunidad de disfrutar con su familia, amigos de un ambiente sano, pleno contacto con la naturaleza. Lago 
    para pesca, a 10 minutos encuentras balnearios con piscinas de agua natural, paseo ecológico. Ubicado vía El Diamante.""",#descripcion
    imgur['DjzCERq.jpg'],#uriroom
    facebook['SebastianHernandezCastrillon/'],#urivalue
    imgur['qn7NgA2.jpg'],#uriBed
    "4",#numHab
    "4",#numCamas
    imgur['QUd4xJd.jpg'],#imagen
    facebook['Hostal-Santsebastian-995216180540544']
)

#print (g.serialize(format="pretty-xml")) 
