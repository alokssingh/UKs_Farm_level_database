
# SerpAPi, Geocoding, selenium scraping, Entity Matching with Sentence-BERT

# Project Overview
This project consists of four different tasks, each in its own folder, with a common `requirements.txt` file for all dependencies.

## Folder Structure & Tasks
1. **SBERT (Entity Matching)** - Uses Sentence-BERT to compare names between two Excel files.
2. **Scraping (SERPAPI)** - Scrapes search results using SERPAPI based on keywords.
3. **Geocoding** - Handles geolocation-related tasks.
4. **Web Scraping (Selenium)** - Generalized web scraping using Selenium.

## Installation
Ensure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

## Usage
### 1. SBERT (Entity Matching)
This script compares names between two Excel files using Sentence-BERT (SBERT) for similarity analysis. The results are saved in an output Excel file.

#### How It Works
1. Reads two Excel files and extracts names from the "Name" column.
2. Uses Sentence-BERT (`compare_names_with_sentence_bert`) to compare names from both files.
3. Saves similarity results in `result_sbert.xlsx`.

#### Running the Script
```bash
python sbert/main.py file1.xlsx file2.xlsx
```

### 2. Scraping (SERPAPI)
This script processes search keywords from an Excel file and saves results to CSV and JSON files.

#### How It Works
1. Reads keywords from `keyword_postcode_Organic_Farms.xlsx`.
2. Iterates through each keyword, formatting it into filenames.
3. Calls `serpapi_pages(keyword, filename_json)` to fetch search results.
4. Saves results in CSV using `write_to_csv(data1, filename_csv)`.

#### Running the Script
```bash
python scraping/main.py
```
Ensure `keyword_postcode_Organic_Farms.xlsx` exists in the directory.

### 3. Geocoding
This script extracts latitude and longitude coordinates from addresses using a geocoding API and saves the results in JSON and Excel formats.

#### How It Works
1. Reads addresses from an Excel file (`filename.xlsx`).
2. Extracts latitude and longitude for each address using `geocoding.extract_lat_lng()`.
3. Saves the results in a JSON file inside a directory (`tester`).
4. Converts the JSON data into an Excel file for easy access.

#### Running the Script
```bash
python geocoding/main.py
```
Make sure to update `api_key` in `geocoding/main.py` with your geocoding API key and have an Excel file (`filename.xlsx`) with an address column.

### 4. Web Scraping (Selenium)
This script automates web scraping using Selenium to extract farm-related data and save it to an Excel file.

#### How It Works
1. Sets up the Selenium WebDriver using `setup_webdriver()`.
2. Scrapes data from multiple pages (`start_page = 1` to `end_page = 50`) using `scrape_data(driver, start_page, end_page)`.
3. Extracts `name`, `farm`, and `address` details from the target website.
4. Saves the scraped data into an Excel file (`farms.xlsx`).

#### Running the Script
```bash
python selenium_scraping/main.py
```
Ensure Selenium and WebDriver dependencies are correctly installed and configured.


## License
This project is licensed under the MIT License.

