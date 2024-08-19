import os

pasta_raiz = '//nas.prodam/smg_cgpatri/CGPATRI_DEAPI_ACERVO_PLANTAS/GEORREFERENCIAMENTO/PLANTAS DGPI GEOREFERENCIADAS/'

for i in os.listdir(pasta_raiz):
    #se i for uma pasta entrar na pasta e listar outras pastas
    nome_pasta = os.path.join(pasta_raiz, i)
    for j in os.listdir(nome_pasta):
        arquivos_pasta_dgpi = os.path.join(nome_pasta, j)
        
        if os.path.isdir(arquivos_pasta_dgpi):
            subpasta_revisão = os.path.join(arquivos_pasta_dgpi, j)
            print(f"{j} é uma subpasta")
            pass
        else:
            print(f'Pasta Planta {i} " " " " Arquivos: {j}', sep=" ")
#Até aqui código retorna qual é uma subpasta

#senão copiar basename do arquivo com extensão .shp
#caminho_2 = 'DGPI 00.001_00/DGPI 00.001_00.shp'
#nomes_sem_ext = os.path.splitext(caminho_2)
#nomes_sem_ext_2 = nomes_sem_ext[0].split("/")
#print(nomes_sem_ext)
#print(nomes_sem_ext_2)

#if (nomes_sem_ext_2[0] == nomes_sem_ext_2[1]):
#    print('Os nomes são iguais')
#else:
#    print('os nomes são diferentes')