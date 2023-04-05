import csv
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytz

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
url = 'https://www.restart-fitness.ru/raspisanie/'
csv_file = 'visitor_counts.csv'

rescan_minutes = 5
# looping every n minutes
while True:
    # Get the current date and time in the desired format
    current_time = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime('%Y-%m-%d %H:%M:%S')
    try:
        # Create a new instance of the Chrome driver (you can use any other supported browser driver)
        driver = webdriver.Chrome(options=chrome_options)
        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load
        time.sleep(5)

        # Find the div tag containing the visitor count and extract the number
        # /html/body/section[6]/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]
        # <div class="online-people_rz">Now 35 visitors</div>
        # document.querySelector("body > section.bh > div > div > div.content_rz.show-choice_rz > div > div > div.wr-rsp > div > div.menu-group_rz > div.online-people_rz")
        # body > section.bh > div > div > div.content_rz.show-choice_rz > div > div > div.wr-rsp > div > div.menu-group_rz > div.online-people_rz
        # <div class="online-people_rz">Now 35 visitors</div>

        # vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
        visitor_element = driver.find_element(By.CLASS_NAME, 'online-people_rz')
        if visitor_element is not None:
            visitor_text = visitor_element.text.strip()
            # Extract the number from the text (using a regular expression)
            import re

            visitor_count = int(re.search(r'\d+', visitor_text).group())
        else:
            visitor_count = None

        # Close the browser window
        driver.quit()
        # Append the date, time, and visitor count to the CSV file
        with open(csv_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([current_time, visitor_count])
        print([current_time, visitor_count])
    except Exception as Err:
        print([current_time, str(Err)])
    time.sleep(60 * rescan_minutes)
