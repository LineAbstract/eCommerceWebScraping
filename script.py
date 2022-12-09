
from selenium import webdriver # webdriver
from selenium.webdriver.chrome.service import Service # this creates the web driver instance
from selenium.webdriver.common.by import By # select specific elements on the web page
from selenium.common.exceptions import NoSuchElementException # handles end of pagination
from selenium.webdriver.support.wait import WebDriverWait # generates wait time
from selenium.webdriver.support import expected_conditions as EC # needed for wait time
import csv

# Setup CSV
file = open("laptops_final.csv", "w", newline='') # creates new csv file
writer = csv.writer(file) # setting up writer instance to write to file
writer.writerow(["id", "name", "price", "specifications", "number_of_reviews"]) # setting up column headers

# Creates Chrome Service & WebDriver instance
browser_driver = Service("/Users/coderino/Library/Mobile Documents/com~apple~CloudDocs/Coding/chromedriver")
scraper = webdriver.Chrome(service = browser_driver) # another object we're creating from a class

# GET page to scrape
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

# Scrape
unique_id = 1
while True:
    laptops = scraper.find_elements(By.CLASS_NAME, "col-sm-4")
    for laptop in laptops:
        name = laptop.find_element(By.CLASS_NAME, "title").text
        
        price = laptop.find_element(By.CLASS_NAME, "caption")
        price_final = price.find_element(By.CLASS_NAME, "pull-right").text

        specifications = laptop.find_element(By.CLASS_NAME, "description").text
        
        number_of_reviews = laptop.find_element(By.CLASS_NAME, "ratings")
        number_of_reviews_v2 = number_of_reviews.find_element(By.CLASS_NAME, "pull-right").text
        number_of_reviews_final = number_of_reviews_v2.split(" ")[0]
        writer.writerow(
            [unique_id, name, price_final, specifications, number_of_reviews_final])
        unique_id += 1
    try:
         # Wait for data to load 
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

file.close()
scraper.quit()

# to add... sort by price before writing to csv
    # must strip price of $ and turn to float
    # for every object (laptop), save variables to a dictionary and append dictionary to list
    # sort saved list by dictionary key of ['price']
    # concatenate $ to ['price']
    # write all rows to file