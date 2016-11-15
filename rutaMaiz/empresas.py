#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import facebook, twitter, ciudadGuru, imgur, maps, camaraTulua, dbpedia, rutaMaiz
from alojamientos import g

#g = Graph()

# Esquema del grafo para empresas de la ruta del maíz.
def empresas(uri, nombre, tel, imagen, descripcion, direcc, email, webpage, mapa, uriatencion, abre, cierra, linkURI):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
                 
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )
    g.add( (URIRef(uri), GR.name, Literal(nombre)) )
    g.add( (URIRef(uri), GR.description, Literal(descripcion)))
    g.add( (URIRef(uri), VCARD.tel, Literal(tel)) )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) 
    
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)) )
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
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
    
    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz['Empresas.rdf'])))
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo

empresas(
    rutaMaiz['Empresas.rdf#agrocorvalle'],
    'AGROINDUSTRIA OLEAGINOSA CORAZÓN DEL VALLE',
    '3148541375, 3162742948, 3176247417',
    #'http://i.imgur.com/iVHRK2g.jpg',
    imgur['iVHRK2g.jpg'],
    """Dedicada al cultivo y transformación de 
    frutos de plantas oleaginosas principalmente la SACHA INCHI.""",
    'Campoalegre, Tuluá, Valle del Cauca',
    'sicorazondelvalle@gmail.com',
    'https://www.agrocorvalle.com',
    maps['5bcFmGU8gpx'],
    "http://www.eltabloide.com.co/el-aceite-de-los-incas/",
    "08:00:00",
    "18:00:00",
    facebook['AGROCORVALLE']
)

empresas(
    rutaMaiz['Empresas.rdf#ingenioSanCarlos'],
    'INGENIO SAN CARLOS',
    '2311515',
    #'http://i.imgur.com/IwXka7i.png',
    imgur['IwXka7i.png'],
    """Empresa agroindustrial dedicada al cultivo de caña
    y su transformación en azúcares, mieles, energía limpia y otros derivados.""",
    #'Vía Riofrio Km. 7 Palomestizo',
    'Ingenio Sancarlos, Al Ingenio San Carlos #Vía Río Frío Km 3, Palomestizo, Tuluá, Valle del Cauca',
    'https://mail1.ingeniosancarlos.com.co/owa/',
    'http://www.ingeniosancarlos.com.co/',
    maps['z12DarMykcr'],
    camaraTulua['ingenio-sancarlos-s-a/'],
    "05:00:00",
    "16:00:00" ,
    facebook['pages/Ingenio-Sancarlos-SA/624707384217059']
)

empresas(
    rutaMaiz['Empresas.rdf#viveroElRosal'],
    'VIVERO EL ROSAL',
    '2257151, 2313440, 2319719, 3165542035',
    #'http://i.imgur.com/OicbmG7.jpg',
    imgur['OicbmG7.jpg'],
    'Empresa dedicada a la producción, comercialización y distribución de plantas ornamentales.',
    'Calle 27 No. 3 Oeste 52, Tuluá, Valle del Cauca',
    'No disponible',
    'http://www.viveroelrosal.com/',
    maps['ZWqu9cCVnqy'],
    ciudadGuru['vivero-el-rosal/tulua/15406229'],
    "07:00:00",
    "18:00:00",
    facebook['ViveroElRosaltulua']
)

empresas(
    rutaMaiz['Empresas.rdf#laHerradura'],
    'CENTRO COMERCIAL LA HERRADURA',
    '2249507',
    #'http://i.imgur.com/yXlawlm.png',
    imgur['yXlawlm.png'],
    """Centro comercial del Corazón de Valle del Cauca donde encuentras plazoleta de comidas,
    bares, tiendas, cine, eventos y más.""",
    'Carrera 19 No. 28 - 76, Tuluá, Valle del Cauca',
    'No disponible',
    'http://www.laherradura.com.co/',
    maps['eWUvQ3seeqs'],
    ciudadGuru['centro-comercial-la-herradura/tulua/15722833'],
    "09:00:00",
    "23:00:00",
    facebook['pages/La-Herradura/10401777341']
)

empresas(
    rutaMaiz['Empresas.rdf#la14'],
    'CENTRO COMERCIAL TULUÁ LA 14',
    '2308640',
    #'http://i.imgur.com/d6zxnQe.jpg',
    imgur['d6zxnQe.jpg'],
    """Centro empresarial, comercial y de negocios, epicentro de una permanente actividad social
    y el lugar de encuentro favorito de las familias centro vallecaucanas.""",
    'Carrera. 40 No. 37 - 51, Tuluá, Valle del Cauca',
    'No disponible',
    'http://centrocomercialtulua.com/',
    maps['khz8XnXuAHQ2'],
    ciudadGuru['centro-comercial-tulua-la-14/tulua/16750145'],
    "09:30:00",
    "23:30:00",
    facebook['centrocomercialtuluala14']
)

empresas(
    rutaMaiz['Empresas.rdf#projugos'],
    'PRODUCTORA DE JUGOS S.A.S',
    '2356100, 2253153',
    #'http://i.imgur.com/68cCsff.jpg',
    imgur['68cCsff.jpg'],
    """Empresa especializada en el procesamiento de pulpas, jugos de frutas naturales
    y concentrados.""",
    'Calle 48 No. 21 - 100, Tuluá, Valle del Cauca',
    'info@projugos.com',
    'http://www.projugos.com/',
    maps['Lb5DsP437dP2'],
    camaraTulua['productora-de-jugos-s-a-s/'],
    "07:00:00",
    "18:00:00",
    facebook['pages/Projugos-Tulua/403454439767813']
)

empresas(
    rutaMaiz['Empresas.rdf#levapan'],
    'LEVAPAN S.A',
    '2241688',
    #'http://i.imgur.com/x9N7Moc.jpg',
    imgur['x9N7Moc.jpg'],
    """Moderna y tecnificada planta de producción de levadura.""",
    'Carrera 27 A No. 40 - 470, Tuluá, Valle del Cauca',
    'impuesto@levapan.com',
    'http://www.levapan.com/',
    maps['f3S8nRTWMdC2'],
    camaraTulua['compania-nacional-de-levaduras-levapan-s-a/'],
    "07:30:00",
    "18:00:00",
    facebook['pages/Levapan-Tulua/481467405286461']
)

empresas(
    rutaMaiz['Empresas.rdf#centroaguas'],
    'CENTROAGUAS S.A. E.S.P',
    '2317070',
    #'http://i.imgur.com/Dqh8Z8Y.jpg',
    imgur['Dqh8Z8Y.jpg'],
    """Purificación y distribución de agua, para uso doméstico y comercial.""",
    'Calle 25 No. 32A - 31, Tuluá, Valle del Cauca',
    'info@centroaguas.com',
    'http://www.centroaguas.com/',
    maps['maps/xhhhcTiNAK12'],
    camaraTulua['centroaguas-s-a-e-s-p/'],
    "07:00:00",
    "16:00:00",
    facebook['Agregar-centro-aguas-tulua/446894565390492']
)

empresas(
    rutaMaiz['Empresas.rdf#cetsa'],
    'COMPAÑÍA DE ELECTRICIDAD DE TULUÁ S.A. E.S.P.',
    '2339000',
    #'http://i.imgur.com/4KSaIUz.jpg',
    imgur['4KSaIUz.jpg'],
    """Comercialización de energía eléctrica.""",
    'Calle 29 No. 23 - 45, Tuluá, Valle del Cauca',
    'mlasso@cetsa.com.co',
    'http://www.cetsa.com.co',
    maps['CwfJVDVaH1m'],
    camaraTulua['compania-de-electricidad-de-tulua-s-a-e-s-p/'],
    "08:00:00",
    "16:00:00",
    facebook['pages/Compa%C3%B1ia-de-Electricidad-de-Tulua-CETSA/109217362434941']
)

empresas(
    rutaMaiz['Empresas.rdf#transtobar'],
    'EMPRESA DE TRANSPORTES TOBAR LIMITADA "TRANSTOBAR"',
    '2242199',
    #'http://i.imgur.com/HbJ0Oh2.jpg',
    imgur['HbJ0Oh2.jpg'],
    """Transporte metropolitano colectivo regular de pasajeros.""",
    'Carrera 18 No. 26 B - 01, Tuluá, Valle del Cauca',
    'transtobartulua@gmail.com',
    'No disponible',
    maps['zkRFEQ2E2W72'],
    camaraTulua['empresa-de-transportes-tobar-limitada-transtobar/'],
    "05:00:00",
    "19:00:00",
    facebook['pages/trans-tobar-tulua/127752540643366']
)

empresas(
    rutaMaiz['Empresas.rdf#centralTransportes'],
    'CENTRAL DE TRANSPORTES DE TULUÁ S.A.',
    '2245779, 2251477',
    #'http://i.imgur.com/aKdj3Oq.jpg',
    imgur['aKdj3Oq.jpg'],
    """Transporte intermunicipal.""",
    'Carrera 20 No. 26 - 32, Tuluá, Valle del Cauca',
    'contabilidad@terminaltulua.com',
    'http://www.terminaltulua.com/',
    maps['SBfKsSqoAx52'],
    camaraTulua['central-de-transportes-de-tulua-s-a/'],
    "04:30:00",
    "20:00:00",
    facebook['pages/Terminal-de-transportes-Tulu%C3%A1/413459778666424']
)

empresas(
    rutaMaiz['Empresas.rdf#harinasTulua'],
    'INDUSTRIA DE HARINAS TULUÁ LIMITADA',
    '2245815, 2251477',
    #'http://i.imgur.com/0k8bTdA.jpg',
    imgur['0k8bTdA.jpg'],
    """Industria dedicada a la elaboración de harina de trigo fortificada
    y sus derivados como la sémola, semolatto, salvado, mogolla, harina de
    tercera y harina integral.""",
    'Carrera 28 No 32 - 54, Tuluá, Valle del Cauca',
    'contabilidad@harinastulua.com',
    'http://harinastulua.com/',
    maps['3yvUxvApjC32'],
    camaraTulua['industria-de-harinas-de-tulua-ltda/'],
    "08:00:00",
    "16:00:00",
    facebook['Industria-de-Harinas-Tulua-limitada-133301366750011/']
)

empresas(
    rutaMaiz['Empresas.rdf#bancoPopular'],
    'BANCO POPULAR AGENCIA TULUÁ',
    '2243997',
    #'http://i.imgur.com/lmJk2Wx.jpg',
    imgur['lmJk2Wx.jpg'],
    """Sede del Banco Popular de la ciudad de Tuluá.""",
    'Carrera 25 No. 27 - 92, Tuluá, Valle del Cauca',
    'tulua@bancopopular.com.co',
    'http://www.bancopopular.com.co/',
    maps['eRwDwfodkFM2'],
    camaraTulua['banco-popular/'],
    "08:00:00",
    "16:00:00",
    dbpedia['Banco_Popular_(Colombia)']
)

empresas(
    rutaMaiz['Empresas.rdf#bancoBogota'],
    'BANCO DE BOGOTÁ AGENCIA TULUÁ',
    '2244222',
    #'http://i.imgur.com/byJtPab.jpg',
    imgur['byJtPab.jpg'],
    """Sede del Banco de Bogotá de la ciudad de Tuluá.""",
    'Carrera 26  No. 27 - 32, Tuluá, Valle del Cauca',
    'jds612@bancodebogota.com',
    'http://www.bancodebogota.com/',
    maps['C3uT9unrXJG2'],
    camaraTulua['banco-de-bogota-agencia-tulua/'],
    "08:00:00",
    "16:00:00",
    dbpedia['Banco_de_Bogota']
)

empresas(
    rutaMaiz['Empresas.rdf#bancoOccidente'],
    'BANCO DE OCCIDENTE AGENCIA TULUÁ',
    '2243086',
    #'http://i.imgur.com/bBw3z7f.png',
    imgur['bBw3z7f.png'],
    """Sede del Banco de Occidente de la ciudad de Tuluá.""",
    'Calle 27 No. 25 - 37, Tuluá, Valle del Cauca',
    'of.tulua@bancodeoccidente.com.co',
    'http://www.bancodeoccidente.com.co',
    maps['do7YXobsy6w'],
    camaraTulua['banco-de-occidente-agencia-tulua/'],
    "08:00:00",
    "16:00:00",
    dbpedia['Banco_de_Occidente_Credencial']
)

empresas(
    rutaMaiz['Empresas.rdf#bancolombia'],
    'BANCOLOMBIA TULUÁ',
    '2319905',
    #'http://i.imgur.com/TOTbhR5.jpg',
    imgur['TOTbhR5.jpg'],
    """Sede de Bancolombia de la ciudad de Tuluá.""",
    'Carrera 26 No. 26 - 20, Tuluá, Valle del Cauca',
    'No disponible',
    'http://www.grupobancolombia.com/',
    maps['maB4rWdiNLU2'],
    camaraTulua['bancolombia-tulua/'],
    "08:00:00",
    "16:30:00",
    dbpedia['Bancolombia']
)

empresas(
    rutaMaiz['Empresas.rdf#viveroJazmin'],
    'ARTESANÍAS Y VIVERO EL JAZMÍN',
    '2321193',
    #'http://i.imgur.com/9OiB5aZ.png',
    imgur['9OiB5aZ.png'],
    """Comercialización de plantas y artesanías.""",
    'Calle 31 Nro. 38 - 45, Tuluá, Valle del Cauca',
    'viverojazmin@gmail.com',
    'http://www.viveroeljazmin.com/',
    maps['iSaQ88pygck'],
    ciudadGuru['artesanias-y-vivero-el-jazmin/tulua/15724710'],
    "07:00:00",
    "18:00:00",
    twitter['Ecodataset/status/707056997326311424']
)

empresas(
    rutaMaiz['Empresas.rdf#bioverti'],
    'BIOVERTI',
    '3133000914',
    #'http://i.imgur.com/IMbLvj6.jpg',
    imgur['IMbLvj6.jpg'],
    """Cultivo de hortalizas, raíces y tubérculos.""",
    #'Calle 26 No. 36-32 Apto 201',
    'Calle 26 No. 36 - 32, Tuluá, Valle del Cauca',
    'anyel176@hotmail.com',
    'http://www.bioverti.com',
    maps['aE9d6FjHjUD2'],
    camaraTulua['bioverti/'],
    "09:00:00",
    "16:00:00",
    twitter['Ecodataset/status/707060058031595520'] 
)

#print (g.serialize(format="pretty-xml"))
