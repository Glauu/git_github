import os

pasta_raiz = '//nas.prodam/smg_cgpatri/CGPATRI_DEAPI_ACERVO_PLANTAS/GEORREFERENCIAMENTO/PLANTAS DGPI GEOREFERENCIADAS/'
for root, dirs, files in os.walk(pasta_raiz, 'limit=50'):
    for i in files:
        if i.endswith('.shp'):
            poligonos = os.path.join(root, i)
            print(poligonos)
#    if arquivo.shp exixts
#      var = os.path.join(root, arquivo.shp)
#print(var)