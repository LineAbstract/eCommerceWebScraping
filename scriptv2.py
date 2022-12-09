from selenium import webdriver # webdriver
from selenium.webdriver.chrome.service import Service # this creates the web driver instance
from selenium.webdriver.common.by import By # select specific elements on the web page
from selenium.common.exceptions import NoSuchElementException # handles end of pagination
from selenium.webdriver.support.wait import WebDriverWait # generates wait time
from selenium.webdriver.support import expected_conditions as EC # needed for wait time
import csv

# setup CSV
file = open("laptops_sorted_final.csv", "w", newline='') # creates new csv file
writer = csv.writer(file) # setting up writer instance to write to file
writer.writerow(["id", "name", "price", "specifications", "number_of_reviews"]) # setting up column headers

# creates Chrome Service & WebDriver instance
browser_driver = Service("/Users/coderino/Library/Mobile Documents/com~apple~CloudDocs/Coding/chromedriver")
scraper = webdriver.Chrome(service = browser_driver) # another object we're creating from a class

# GET page to scrape
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

# scrape
header_list = ["id", "name", "price", "specifications", "number_of_reviews"]
data_list = []
unique_id = 1
while True:
    laptops = scraper.find_elements(By.CLASS_NAME, "col-sm-4")
    for laptop in laptops:
        name = laptop.find_element(By.CLASS_NAME, "title").text
        
        price = laptop.find_element(By.CLASS_NAME, "caption")
        price_v2 = price.find_element(By.CLASS_NAME, "pull-right").text
        price_strip = price_v2.strip("$")
        price_final = float(price_strip)

        specifications = laptop.find_element(By.CLASS_NAME, "description").text
        
        number_of_reviews = laptop.find_element(By.CLASS_NAME, "ratings")
        number_of_reviews_v2 = number_of_reviews.find_element(By.CLASS_NAME, "pull-right").text
        number_of_reviews_final = number_of_reviews_v2.split(" ")[0]

        # before writing row, add all scraped items to a list (or dictionary, as it doesn't allow for dups)
        table_dict = {"id": unique_id,
                    "name": name,
                    "price": price_final,
                    "specifications": specifications,
                    "number_of_reviews": number_of_reviews_final}
        data_list.append(table_dict)

        unique_id += 1
    try:
         # wait for data to load 
        wait = WebDriverWait(scraper, 10)
        element_to_watch = scraper.find_element(By.CLASS_NAME, "col-md-9")
        wait.until(EC.visibility_of(element_to_watch))
        # click next page
        cookie_banner = scraper.find_element(By.XPATH, '//*[@id="closeCookieBanner"]')
        cookie_banner.click()
        element = scraper.find_element(By.PARTIAL_LINK_TEXT, "›")
        element.click()
    except NoSuchElementException:
        break

# sort list of dictionaries by ['price'] key in dictionaries
sorted_data_list = sorted(data_list, key=lambda a: a['price'])

# change price in list of dictionaries to a string
# append $ character to price string in list of dictionaries
# write data row to csv file
for dicts in sorted_data_list:
    # dicts['price'] = str(dicts['price'])
    dicts['price'] = f"${dicts['price']}"
    writer.writerow(
        [dicts['id'], dicts['name'], dicts['price'], dicts['specifications'],dicts['number_of_reviews']]
        )

file.close()
scraper.quit()