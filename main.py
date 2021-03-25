import pdf2image
import os

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

def parse_downloaded_isin(isin)
    for info_name, info_data in ishare_info_places.items():
        print('parsing', info_name)
        images = pdf2image.convert_from_path(
            f'./ishare_mr_it/pdfs/{isin}_MR_IT_it.pdf',
            dpi=300,
            grayscale=True
        )
        page = images[info_data["pagina"]]
        w,h = page.size
        output_file_name = f'./ishare_mr_it/images/{isin}_{info_name}.jpg'
        crop_box = tuple( map( lambda x: int(x), [
            info_data['bbox_w'][0]*w, info_data['bbox_h'][0]*h,
            info_data['bbox_w'][1]*w, info_data['bbox_h'][1]*h
        ]))
        page.crop(crop_box).save(output_file_name, 'JPEG')

isin = 'IE0005042456'

parse_downloaded_isin(isin)


print("fatto")

