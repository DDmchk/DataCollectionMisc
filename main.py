import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = 'https://www.restart-fitness.ru/raspisanie/'

# Make a GET request to the page
response = requests.get(url)

# Collect the date and time of the request
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
data_to_save = f"Date and time of request: {dt_string}\n"

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
visitor_count = 0
# Find the "visitor" span tag and extract the numeric value
visitor_tag = soup.find('div', {'class': 'online-people_rz'})
if visitor_tag is not None:
    visitor_text = visitor_tag.text.strip()
    visitor_count = visitor_text.split(' ')[-2]
    data_to_save += f"Visitor count: {visitor_count}\n"
else:
    data_to_save += "Visitor count not found on the page\n"

# Add the visitor count to the data to be saved
data_to_save += f"Visitor count: {visitor_count}\n"

# Write the data to a text file
with open("webpage_data.txt", "w") as file:
    file.write(data_to_save)