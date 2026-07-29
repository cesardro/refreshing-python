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

#APIs
print("\n*****APIs*****")
import json

'''
# Load JSON data from a file
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print the keys of the JSON data to the shell
for k in json_data.keys():
    print(k + ': ', json_data[k])

'''

# An API is a set of functions and procedures that allow the creation of applications 
# which access the features or data of an operating system, application, or other service.

url = 'http://www.omdbapi.com?apikey=72bc447a&t=the+social+network'

# Perform the HTTP GET request: r
r = requests.get(url)

# Print the text of the response.
print(r.text)
######################################
# Import package
import requests

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
######################################
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Always include a descriptive User-Agent (Wikipedia requires this)
headers = {
    "User-Agent": "Checking out the Wikipedia API"
}

# Package the request, send the request and catch the response: r
r = requests.get(url, headers=headers)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

# Twitter APIs
print("\n*****Twitter APIs*****")
import teewpy
# Store credentials in relevant variables
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

# Create your Stream object with credentials
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)

# Filter your Stream variable
stream.filter(track=["clinton", "trump", "sanders", "cruz"])
################################
tweets_data = []
# Open connection to file
tweets_file = open('tweets.txt', "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
##################################
# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())

'''
                                                text lang
0  b"RT @bpolitics: .@krollbondrating's Christoph...   en
1  b'RT @HeidiAlpine: @dmartosko Cruz video found...   en
2  b'Njihuni me Zonj\\xebn Trump !!! | Ekskluzive...   et
3  b"Your an idiot she shouldn't have tried to gr...   en
4  b'RT @AlanLohner: The anti-American D.C. elite...   en
'''