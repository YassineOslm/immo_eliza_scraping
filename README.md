# 🏠 Challenge - Collecting Data

## 📌 Description

This project is part of a data collection challenge aimed at building a **real estate dataset** with **at least 10,000 entries** for properties across **Belgium**. The dataset will later be used to train a **Machine Learning model** for predicting real estate prices.

The collected data includes property details such as location, type, size, number of rooms, price, and other features like terrace, garden, pool, etc.

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/challenge-collecting-data.git
cd challenge-collecting-data
```

2. (Recommended) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

To run the scraper:

```
python main.py
```

This will start collecting property data from the target website and save it into a real_estate_data.csv file.

⚠️ Note: The script may take time depending on the number of pages and the scraping strategy.

## 📊 Dataset Columns

- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale
- Number of rooms
- Living Area
- Fully equipped kitchen (1/0)
- Furnished (1/0)
- Open fire (1/0)
- Terrace (1/0) + area
- Garden (1/0) + area
- Surface of the land
- Surface area of the plot of land
- Number of facades

Missing information is set to `None`.

## 🧠 Strategy

- Python with `requests`, `BeautifulSoup`, `pandas`.
- Multiprocessing/threading to improve performance.
- Clean CSV output with standardized fields and no duplicates.

## 👤 Contributors

- Trainee : Yassine Aarab
- Coach: Jean Cheramy
