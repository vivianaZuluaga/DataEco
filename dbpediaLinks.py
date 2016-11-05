#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF
from ontologias import OWL

g = Graph()
dbpedia = Namespace('http://dbpedia.org/resource/')
ecolod = Namespace('http://190.14.254.237/dataseteco/')

def links(uriDBpedia, uriDataEco):         
    g.add( (URIRef(uriDBpedia), OWL.sameAs, URIRef(uriDataEco)) )
    
links(dbpedia['Category:Colombia'], ecolod['RutaDelJardinBotanico/']) #categorias sobre Colombia
links(dbpedia['Category:Colombia'], ecolod['RutaDelMaiz/'])
links(dbpedia['Category:Colombia'], ecolod['Riofrio/'])
links(dbpedia['Category:Colombia'], ecolod['RutaVueltaAOriente/'])
links(dbpedia['Category:Colombia'], ecolod['RutaDelAnilloAgricola/'])

links(dbpedia['Colombia'], ecolod['RutaDelJardinBotanico/'])  
links(dbpedia['Colombia'], ecolod['RutaDelMaiz/'])
links(dbpedia['Colombia'], ecolod['Riofrio/'])
links(dbpedia['Colombia'], ecolod['RutaVueltaAOriente/'])
links(dbpedia['Colombia'], ecolod['RutaDelAnilloAgricola/'])

links(dbpedia['Tourism_in_Colombia'], ecolod['RutaDelJardinBotanico/'])
links(dbpedia['Tourism_in_Colombia'], ecolod['RutaDelMaiz/'])
links(dbpedia['Tourism_in_Colombia'], ecolod['Riofrio/'])
links(dbpedia['Tourism_in_Colombia'], ecolod['RutaVueltaAOriente/'])
links(dbpedia['Tourism_in_Colombia'], ecolod['RutaDelAnilloAgricola/'])
      
links(dbpedia['Category:Municipalities_of_Colombia'], ecolod['Riofrio/'])

links(dbpedia['Category:Flora_of_Colombia'], ecolod['RutaDelJardinBotanico/Flora/'])
links(dbpedia['Category:Flora_of_Colombia'], ecolod['RutaDelMaiz/Flora/'])
links(dbpedia['Category:Flora_of_Colombia'], ecolod['Riofrio/Flora/'])
links(dbpedia['Category:Flora_of_Colombia'], ecolod['RutaVueltaAOriente/Flora/'])

links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelJardinBotanico/Flora/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelMaiz/Flora/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['Riofrio/Flora/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaVueltaAOriente/Flora/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelAnilloAgricola/Fauna/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaDelMaiz/Fauna/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['Riofrio/Fauna/'])
links(dbpedia['Category:Biota_of_Colombia'], ecolod['RutaVueltaAOriente/Fauna/'])

links(dbpedia['Category:Fauna_of_Colombia'], ecolod['RutaDelAnilloAgricola/Fauna/'])
links(dbpedia['Category:Fauna_of_Colombia'], ecolod['RutaDelMaiz/Fauna/'])
links(dbpedia['Category:Fauna_of_Colombia'], ecolod['Riofrio/Fauna/'])
links(dbpedia['Category:Fauna_of_Colombia'], ecolod['RutaVueltaAOriente/Fauna/'])

links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelJardinBotanico/Flora/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelMaiz/Flora/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['Riofrio/Flora/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaVueltaAOriente/Flora/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelAnilloAgricola/Fauna/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaDelMaiz/Fauna/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['Riofrio/Fauna/'])
links(dbpedia['Category:Environment_of_Colombia'], ecolod['RutaVueltaAOriente/Fauna/'])

links(dbpedia['Category:Municipalities_of_Valle_del_Cauca_Department'], ecolod['Riofrio/'])

links(dbpedia['Riofrio,_Valle_del_Cauca'], ecolod['Riofrio/'])
links(dbpedia['Tulua'], ecolod['RutaDelMaiz/'])
links(dbpedia['Heriberto_Gil_Martinez_Airport'], ecolod['RutaDelMaiz/'])
links(dbpedia['Estadio_Doce_de_Octubre'], ecolod['RutaDelMaiz/'])
links(dbpedia['Cortulua'], ecolod['RutaDelMaiz/']) #equipo de futbol tulua
links(dbpedia['University_of_Valle'], ecolod['RutaVueltaAOriente/Empresas'])

links(dbpedia['Ecotourism'], ecolod['RutaDelJardinBotanico/'])
links(dbpedia['Ecotourism'], ecolod['RutaDelMaiz/'])
links(dbpedia['Ecotourism'], ecolod['Riofrio/'])
links(dbpedia['Ecotourism'], ecolod['RutaVueltaAOriente/'])
links(dbpedia['Ecotourism'], ecolod['RutaDelAnilloAgricola/'])

links(dbpedia['Location'], ecolod['RutaDelJardinBotanico/'])
links(dbpedia['Location'], ecolod['RutaDelMaiz/'])
links(dbpedia['Location'], ecolod['Riofrio/'])
links(dbpedia['Location'], ecolod['RutaVueltaAOriente/'])
links(dbpedia['Location'], ecolod['RutaDelAnilloAgricola/'])
    
    
print (g.serialize(format="nt"))

