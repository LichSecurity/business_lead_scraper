import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

SEARCH_TERM = "dentists"
LOCATION = "Cleveland, OH"
OUTPUT_FILE = "leads_output.csv"
MAX_PAGES = 3

def init_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def build_url(search, location, page):
    return f"https://www.yellowpages.com/search?search_terms={search}&geo_location_terms={location}&page={page}"

def scrape_page(driver, url):
    driver.get(url)
    time.sleep(2)  # Let content load

    listings = driver.find_elements(By.CLASS_NAME, "result")
    leads = []

    for listing in listings:
        try:
            name = listing.find_element(By.CLASS_NAME, "business-name").text.strip()
        except:
            name = ""

        try:
            phone = listing.find_element(By.CLASS_NAME, "phones").text.strip()
        except:
            phone = ""

        try:
            category = listing.find_element(By.CLASS_NAME, "categories").text.strip()
        except:
            category = ""

        try:
            website = listing.find_element(By.CLASS_NAME, "track-visit-website").get_attribute("href")
        except:
            website = ""

        leads.append({
            "name": name,
            "phone": phone,
            "category": category,
            "website": website
        })

    return leads

def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "category", "website"])
        writer.writeheader()
        writer.writerows(data)

def scrape_all():
    driver = init_browser()
    all_data = []

    for page in range(1, MAX_PAGES + 1):
        url = build_url(SEARCH_TERM, LOCATION, page)
        print(f"Scraping {url}")
        leads = scrape_page(driver, url)
        all_data.extend(leads)
        time.sleep(2)  # polite delay

    driver.quit()
    return all_data

if __name__ == "__main__":
    print("Starting headless lead scraping...")
    data = scrape_all()
    save_to_csv(data, OUTPUT_FILE)
    print(f"Done. {len(data)} leads saved to '{OUTPUT_FILE}'.")
