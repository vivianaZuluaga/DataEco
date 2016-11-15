#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF
from utils.ontologias import OWL

g = Graph()
dbpedia = Namespace('http://dbpedia.org/resource/')
ecolod = Namespace('http://190.14.254.237/dataseteco/')

def links(uriDBpedia, uriDataEco):         
    g.add( (URIRef(uriDBpedia), OWL.sameAs, URIRef(uriDataEco)) )
    
links(dbpedia['Category:Colombia'], ecolod['RutaDelJardinBotanico/descripcion.rdf']) #categorias sobre Colombia
links(dbpedia['Category:Colombia'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Category:Colombia'], ecolod['Riofrio/descripcion.rdf'])
links(dbpedia['Category:Colombia'], ecolod['RutaVueltaAOriente/descripcion.rdf'])
links(dbpedia['Category:Colombia'], ecolod['RutaDelAnilloAgricola/descripcion.rdf'])

links(dbpedia['Colombia'], ecolod['RutaDelJardinBotanico/descripcion.rdf'])  
links(dbpedia['Colombia'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Colombia'], ecolod['Riofrio/descripcion.rdf'])
links(dbpedia['Colombia'], ecolod['RutaVueltaAOriente/descripcion.rdf'])
links(dbpedia['Colombia'], ecolod['RutaDelAnilloAgricola/descripcion.rdf'])

links(dbpedia['Tourism_in_Colombia'], ecolod['RutaDelJardinBotanico/descripcion.rdf'])
links(dbpedia['Tourism_in_Colombia'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Tourism_in_Colombia'], ecolod['Riofrio/descripcion.rdf'])
links(dbpedia['Tourism_in_Colombia'], ecolod['RutaVueltaAOriente/descripcion.rdf'])
links(dbpedia['Tourism_in_Colombia'], ecolod['RutaDelAnilloAgricola/descripcion.rdf'])
      
links(dbpedia['Category:Municipalities_of_Colombia'], ecolod['Riofrio/descripcion.rdf'])

links(dbpedia['Category:Flora_of_Colombia'], ecolod['RutaDelJardinBotanico/Flora/descripcion.rdf'])
links(dbpedia['Category:Flora_of_Colombia'], ecolod['RutaDelMaiz/Flora/descripcion.rdf'])
links(dbpedia['Category:Flora_of_Colombia'], ecolod['Riofrio/Flora/descripcion.rdf'])
links(dbpedia['Category:Flora_of_Colombia'], ecolod['RutaVueltaAOriente/Flora/descripcion.rdf'])

links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelJardinBotanico/Flora/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelMaiz/Flora/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['Riofrio/Flora/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaVueltaAOriente/Flora/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelAnilloAgricola/Fauna/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelMaiz/Fauna/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['Riofrio/Fauna/descripcion.rdf'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaVueltaAOriente/Fauna/descripcion.rdf'])

links(dbpedia['Category:Fauna_of_Colombia'], ecolod['RutaDelAnilloAgricola/Fauna/descripcion.rdf'])
links(dbpedia['Category:Fauna_of_Colombia'], ecolod['RutaDelMaiz/Fauna/descripcion.rdf'])
links(dbpedia['Category:Fauna_of_Colombia'], ecolod['Riofrio/Fauna/descripcion.rdf'])
links(dbpedia['Category:Fauna_of_Colombia'], ecolod['RutaVueltaAOriente/Fauna/'])

links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelJardinBotanico/Flora/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelMaiz/Flora/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['Riofrio/Flora/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaVueltaAOriente/Flora/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelAnilloAgricola/Fauna/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelMaiz/Fauna/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['Riofrio/Fauna/descripcion.rdf'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaVueltaAOriente/Fauna/descripcion.rdf'])

links(dbpedia['Category:Municipalities_of_Valle_del_Cauca_Department'], ecolod['Riofrio/descripcion.rdf'])

links(dbpedia['Riofrio,_Valle_del_Cauca'], ecolod['Riofrio/descripcion.rdf'])
links(dbpedia['Tulua'], ecolod['RutaDelMaiz/'])
links(dbpedia['Heriberto_Gil_Martinez_Airport'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Estadio_Doce_de_Octubre'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Cortulua'], ecolod['RutaDelMaiz/']) #equipo de futbol tulua
links(dbpedia['University_of_Valle'], ecolod['RutaVueltaAOriente/Empresas.rdf#univalle'])

links(dbpedia['Ecotourism'], ecolod['RutaDelJardinBotanico/descripcion.rdf'])
links(dbpedia['Ecotourism'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Ecotourism'], ecolod['Riofrio/descripcion.rdf'])
links(dbpedia['Ecotourism'], ecolod['RutaVueltaAOriente/descripcion.rdf'])
links(dbpedia['Ecotourism'], ecolod['RutaDelAnilloAgricola/descripcion.rdf'])

links(dbpedia['Location'], ecolod['RutaDelJardinBotanico/descripcion.rdf'])
links(dbpedia['Location'], ecolod['RutaDelMaiz/descripcion.rdf'])
links(dbpedia['Location'], ecolod['Riofrio/descripcion.rdf'])
links(dbpedia['Location'], ecolod['RutaVueltaAOriente/descripcion.rdf'])
links(dbpedia['Location'], ecolod['RutaDelAnilloAgricola/descripcion.rdf'])
    
    
print (g.serialize(format="nt"))

