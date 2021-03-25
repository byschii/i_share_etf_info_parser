
import doc_cutter
import doc_cutter
# import os
#print(list(os.walk('.'))[0])



# https://code.visualstudio.com/docs/containers/debug-python





ishare_info_places = {
    "esposizione_geografica":{
        "pagina": 1,
        "bbox_w": (0.50,  0.95), # rispetto a img.size[0] w
        "bbox_h": (0.05,  0.18) # rispetto a img.size[1] h
    },
    "settori":{
        "pagina": 1,
        "bbox_w": (0.05, 0.51),
        "bbox_h": (0.07, 0.22) # rispetto a img.size[1] h
    },
    "caratteristiche_di_sostenibilita":{
        "pagina": 2,
        "bbox_w": (0.52, 0.96),
        "bbox_h": (0.29, 0.33)
    },
    "performance_annualizzata":{
        "pagina": 0,
        "bbox_w": (0.01, 0.66),
        "bbox_h": (0.76, 0.82)
    },
    "10_principali_posizioni":{
        "pagina":0,
        "bbox_w": (0.65, 0.96),
        "bbox_h": (0.63, 0.75)        
    },
    "informazioni_sul_fondo_1":{
        "pagina": 0,
        "bbox_w": (0.65, 0.96),
        "bbox_h": (0.25, 0.48)
    },
    "informazioni_sul_fondo_2":{
        "pagina": 0,
        "bbox_w": (0.65, 0.96),
        "bbox_h": (0.49, 0.59)
    }
}



isin = 'IE0005042456'

doc_cutter.cut_ishare_etf_document(isin, ishare_info_places)
#doc_downloader.download_ishare_etf_document(isin)


print("fatto")

