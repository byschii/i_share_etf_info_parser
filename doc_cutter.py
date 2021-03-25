import pdf2image
import os

def cut_ishare_etf_document(isin, ishare_info_places):
    for info_name, info_data in ishare_info_places.items():
        print('parsing', info_name)
        images = pdf2image.convert_from_path(
            f'./ishare_mr_it/pdfs/{isin}_MR_IT.pdf',
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