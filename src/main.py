from ImmoElizaScraper import ImmoElizaScraper

if __name__ == "__main__":
    print("Scraping the data...")
    scraper = ImmoElizaScraper()
    scraper.load_data()
    print("Done !")