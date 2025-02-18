import pandas as pd
from webdriver_setup import setup_webdriver
from data_scraper import scrape_data

# Setup WebDriver
driver = setup_webdriver()

# Scrape data
start_page = 1
end_page = 50
name, shop, address = scrape_data(driver, start_page, end_page)

# Close the WebDriver
driver.quit()

# Create dictionary
dd = {
    'name': name,
    'farm': shop,
    'address': address
}

# Convert dictionary to DataFrame
df = pd.DataFrame(dd)

# Save DataFrame to Excel file
df.to_excel("falkirkherald_farms.xlsx", index=False)
