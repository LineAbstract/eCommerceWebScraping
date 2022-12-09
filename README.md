# eCommerceWebScraping
Web scraping with Selenium and a simple Tableau visualization.

Please review ***scriptv2.py*** along with ***laptop_scrape_visualization.twbx*** per your convenience. 

Included in this repo you will notice two files, script.py and scriptv2.py.
- **script.py** is the first iteration of my scrape and does not include the sorting of the data by the price column. 
- **scriptv2.py** is the second iteration of this project and includes the sorting of data by the price column and is the more complete form of this project. 

1. As a data analyst, I want to set up my Python project with all necessary imports and drivers to utilize Selenium for web scraping.
2. As a data analyst, I want to **scrape data from the given website**, getting laptop information from **all 20 pages** of data by handling ***pagination***.
    - Target site: https://webscraper.io/test-sites/e-commerce/static/computers/laptops
3. As a data analyst, I want to write code that will store each laptop I scrape inside a **Python List**.
    - The data points to grab for each laptop will be **name, price, specifications, and number of reviews**.
    - Utilize your browser’s Developer Tools to explore the structure of the HTML page and figure out how to select the card elements!
4. As a data analyst, I want to clean and format my data so that all of my data is free of any duplicates, null values, and other anomalies, then write the data to a **CSV file** and include a **UNIQUE ID** number for each row.
    - The ID will be an integer and needs to be different for each row, starting at the number 1 for the first row.
    - ***No need to use Pandas for any cleaning/wrangling of data.*** 
5. As a data analyst, I want to import my CSV file into a new Tableau workbook as a data source and create **(1) visualization** of my choosing to represent a comparison of the number of reviews a laptop has to its price.
6. As a data analyst, I want to include a **README** file in my Python project answering the following questions:
    - What was the biggest challenge of scraping the web site?
        - There were multiple challenges that were overcome: 
        - In the first version of the script, the largest challenges were selecting the correct element for the number of reviews and splitting it to get the result that was expected, along with realizing that there's a 'cookiebanner' that would popup that needed to be closed before the scraper could be instructed to move to the next page and continue on. 
        - In the second version of the script that includes sorting by the *price* column, the most challenging aspect was figuring out how to iterate through the large list of dictionaries and both change the datatype of *price* to a string and append a $ back to it. 
    - What insight, if any, did you gain from the analysis and visualization of the laptop data?
        - I don't think there are many insights to be gained, however it's visible that there is a larger portion of laptops that are over the price of $1000. Laptops in green are priced at over $1000 and those under $1000 are in blue. 
7. As a data analyst, I want to save my Tableau workbook as a Tableau Public project so that I may share the results of my analysis easily.
8. (Bonus) As a data analyst, I want to **sort all of the data by price** BEFORE exporting it to a CSV using Python code.