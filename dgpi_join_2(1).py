import os
import qgis

project = QgsProject.instance()
#camada_dgpi_1 = qgis.core.QgsProject()- cria um novo projeto qgis
pasta_raiz = '//nas.prodam/smg_cgpatri/CGPATRI_DEAPI_ACERVO_PLANTAS/GEORREFERENCIAMENTO/PLANTAS DGPI GEOREFERENCIADAS'
for nome_pasta_1 in os.listdir(pasta_raiz):
    nome_pasta_2 = os.path.join(nome_pasta_1 + '.shp')
    print(nome_pasta_2)
    pasta_dgpi = os.path.join(pasta_raiz, nome_pasta)
    print(pasta_dgpi)
    if os.path.isdir(pasta_dgpi):
        dgpi_shapefile = os.path.join(pasta_raiz, nome_pasta_1 + nome_pasta_2)
        print(dgpi_shapefile)
        layer = qgis.core.QgsVectorLayer(dgpi_shapefile, nome_pasta, 'ogr')
        project.addMapLayer(layer)
qgis.utils.iface.mapCanvas().refreshAllLayers()
