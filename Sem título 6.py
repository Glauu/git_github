import os

pasta_raiz = '//nas.prodam/smg_cgpatri/CGPATRI_DEAPI_ACERVO_PLANTAS/GEORREFERENCIAMENTO/PLANTAS DGPI GEOREFERENCIADAS/'
lista_arquivos = []
def entrar_pasta():
    try:
        os.chdir(pasta_raiz)
        print(f"Entrou na pasta: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Pasta não encontrada")
    except Exception as e:
        print(f"Erro ao entra na pasta: {e}")
entrar_pasta()

for i in os.listdir(pasta_raiz)[:30]:
    #   entrar na pasta e listar arquivos contidos em i
    entrar_pasta()
    arquivos_na_pasta = os.listdir(i)
    print(arquivos_na_pasta)
#Até aqui código ok 

#    if shapefile.endswith('.shp')
#        print(shapefile)