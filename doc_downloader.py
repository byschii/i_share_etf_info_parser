import requests
from bs4 import BeautifulSoup

def download_ishare_etf_document(isin, path = "./ishare_mr_it/pdfs/"):
    isin = isin.upper()
    ishare_check_url = f'https://www.justetf.com/it/etf-profile.html?isin={isin}'
    ishare_check = requests.get(ishare_check_url).text
    instrument_title = BeautifulSoup(ishare_check, 'html.parser').find('span', class_="h1").text
    if "iShare" in instrument_title and "ETF" in instrument_title:
        pdf_document = requests.get(f"https://www.justetf.com/servlet/download?isin={isin}&documentType=MR&country=IT&lang=it")
        full_path = f"{path}{isin}_MR_IT.pdf"
        with open(f"{full_path}", "wb") as f:
            f.write(pdf_document.content)
        return full_path
    else:
        raise ValueError(f"isin [{isin}] is not iShare EFT")


