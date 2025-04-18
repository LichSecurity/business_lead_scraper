# Business Lead Scraper (Yellow Pages)

A headless Python web scraper that extracts real business leads from YellowPages.com using Selenium and Chrome.  
This tool collects business name, phone number, category, and website, then exports it all to a clean CSV file.

## Features

- Automates scraping of Yellow Pages using a headless browser
- Extracts:
  - Business name
  - Phone number
  - Category
  - Website (if available)
- Saves data to `leads_output.csv`
- Uses real browser behavior to bypass bot detection

## Use Case

Perfect for:
- Digital marketing and SEO agencies
- Freelancers and cold outreach specialists
- Anyone building local lead lists for prospecting and outreach

## How to Use

### 1. Install Requirements

```bash
pip install selenium webdriver-manager

2. Run the Script
bash
Copy
Edit
python scraper.py
The script scrapes 3 pages of results by default for the search term "dentists" in "Cleveland, OH".

3. Output
Results are saved in:

Copy
Edit
leads_output.csv
With the following columns:

name

phone

category

website

Sample Output
Each row in the CSV includes:

name: Business name

phone: Phone number (if available)

category: List of services or business types

website: Direct business website link (if listed)

Example:


Name	Phone	Category	Website
Bright Smile Dental	(216) 555-1234	Dentists, Cosmetic Dentistry	https://brightsmile.com
Cleveland Family Dental	(216) 555-5678	Dentists, Pediatric Dentistry, Implant Dentistry	https://clevelandfamdent.com
Aspen Dental	(216) 555-9012	Dentists, Dental Clinics	https://aspendental.com
SmileWorks Ortho	(440) 555-2020	Orthodontists, Dentists	
Midtown Dental Care	(216) 555-4040	Dentists, Periodontists	https://midtowndental.com
Customization
To change the business type or location, open scraper.py and edit these lines:

python
Copy
Edit
SEARCH_TERM = "dentists"
LOCATION = "Cleveland, OH"
MAX_PAGES = 3
You can adjust MAX_PAGES to scrape more or fewer results.

Dependencies
Python 3.x

selenium

webdriver-manager

Install everything with:

bash
Copy
Edit
pip install selenium webdriver-manager
Author
Built by: Logan Hugli
Python automation engineer focused on business-impact tools, data scraping, and API integrations.