#urllib
print("\n*****urllib*****")
from urllib.request import urlretrieve
import pandas as pd

# Download the file from the URL.
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save the file to the current working directory.
urlretrieve(url, 'winequality-red.csv')

# Read the CSV file into a DataFrame and display the first few rows.
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
################################
url1 = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read the Excel file into a pandas ExcelFile object: xls
xls = pd.read_excel(url1, sheet_name=None)

# Print the sheetnames to the shell
print(xls.keys())

# Read in the sheet '1700' from dictionary.
print(xls['1700'].head())

# HTTP requests
print("\n*****HTTP requests*****")

from urllib.request import urlopen, Request

# Define the URL to download from: url
url2 = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Create a 'Request' object: request
request = Request(url2)

# Send the request and catch the response: response
response = urlopen(request)

# Print the datatype of response to the shell
print(type(response))

#########################################
# Define the URL to download from: url
html = response.read()

# Print the html
#print(html)

# Be polite and close the response!
response.close()
#########################################
# Import package
import requests
# Define the URL to download from: url
url3 = 'http://www.datacamp.com/teach/documentation'
# Perform the HTTP GET request: r.
r = requests.get(url3)
# Print the text of the response.
text = r.text
# Print the html
#print(text)

#Scraping the web
print("\n*****Scraping the web*****")
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

# Download the HTML from the URL: r
r = requests.get(url)

# Contain the HTML in the variable html_doc
html_doc = r.text

# Analyze the HTML using BeautifulSoup: soup and creates a BeautifulSoup object from the HTML document.
soup = BeautifulSoup(html_doc)

# Legibly format the HTML using the prettify() method and store it in pretty_soup.
pretty_soup = soup.prettify()

# Print the response
#print(pretty_soup)
#######################################
url1 = 'https://www.python.org/~guido/'
r = requests.get(url1)
html_doc = r.text
soup = BeautifulSoup(html_doc)

# Print the title of the HTML document to the shell.
print(soup.title)

# Print the text of the HTML document to the shell.
print(soup.get_text())
########################################
url2 = 'https://www.python.org/~guido/'
r = requests.get(url2)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.title)

# Find all 'a' tags (which define hyperlinks) on the page and store them in a_tags.
a_tags = soup.find_all('a')

# Print the URLs to the shell.
for link in a_tags:
    print(link.get('href'))