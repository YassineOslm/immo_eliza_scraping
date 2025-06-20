from bs4 import BeautifulSoup
from patchright.sync_api import sync_playwright
from PropertyParser import PropertyParser
import pandas as pd
import os
from tqdm import tqdm

class ImmoElizaScraper:
    def __init__(self):
        self.base_url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?"
        self.parser = PropertyParser()

    def __str__(self) -> str:
        return "ImmoElizaScraper"

    def save_to_csv(self, data: list[dict], filename1: str = "immoweb_data.csv"):
        df = pd.DataFrame(data)
        file_exists1 = os.path.exists(filename1)
        df.to_csv(filename1, mode="a", index=False, header=not file_exists1, na_rep="")
        #file_exists2 = os.path.exists(filename2)
        #df.to_csv(filename2, mode="a", index=False, header=not file_exists2, na_rep="None")


    def collect_basic_infos(self, page, nb_page: int) -> list[dict]:
        all_basic_info = []
        page.goto(self.base_url + f"countries=BE&page={nb_page}&orderBy=newest")
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        search_results = soup.find("div", id="searchResults").find("ul", id="main-content").find("div").find_all('li')
        properties = [result for result in search_results if result.find("a", class_="card__title-link")]
        for prop in tqdm(properties):
            basic_info = self.parser.extract_card_basic_info(prop)
            all_basic_info.append(basic_info)
        return all_basic_info



    def enrich_property(self, info: dict, page) -> dict:
        try:
            detailed = self.parser.extract_detailed_property_info(page, info["url"])
            return info | detailed
        except Exception as e:
            print(f"Error processing {info['url']}: {e}")
            return info

    def load_data(self, nb_pages: int = 15):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            for nb_page in tqdm(range(10, nb_pages + 1)):
                basic_infos = self.collect_basic_infos(page, nb_page)
                for info in basic_infos:
                    detail_page = browser.new_page()
                    enriched = self.enrich_property(info, detail_page)
                    detail_page.close()
                    self.save_to_csv([enriched])
            page.close()
            browser.close()