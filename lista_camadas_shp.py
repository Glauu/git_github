import os
import qgis.core

pasta ='S:/CGPATRI_DIPI/cadastro_croquis/Glaucy/analise_vetorial/Plantas'
list_arq = os.listdir(pasta)
for i in list_arq:
    if i.endswith('.shp'):
        layer = qgis.core.QgsVectorLayer(pasta, i, 'ogr')
        print(layer.name())
    else:
        print("Não é um arquivo shp")
        
    