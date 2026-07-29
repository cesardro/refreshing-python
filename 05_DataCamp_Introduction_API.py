# APIs -> Application Programming Interface
# SOAP: Focus on strict and formal API design + Enterprise application.
# REST: Focus on simplicity & scalability + Most common API architecture.
# GraphQL: Focus on flexibility + Optimized for performance.

# urllib vs requests
'''
URLLIB
from urllib.request import urlopen
api = "http://api.music-catalog.com/"
with urlopen(api) as response:
    data = response.read()  
    string = data.decode()
    print(string)
'''
'''
REQUESTS
import requests
api = "http://api.music-catalog.com/"
response = requests.get(api)
print(response.text)
'''

# GET -> Read: Check the mailbox contents.
# POST -> Create: Drop a new package in the mailbox.
# PUT -> Update: Replace all packages with a new one.
# DELETE -> Delete: Remove all packages from the mailbox.
'''
GET = Retrieve a resourceresponse = requests.get('http://350.5th-ave.com/unit/243')
POST = Create a resourceresponse = requests.post('http://350.5th-ave.com/unit/243', data={"key": "value"})
PUT = Update an existing resourceresponse = requests.put('http://350.5th-ave.com/unit/243', data={"key": "value"})
DELETE = Remove a resourceresponse = requests.delete('http://350.5th-ave.com/unit/243')
'''

import requests

# Create query params to get API specifics.
query_params = {'artist': 'Deep Purple', 'include_track' : True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
#print(response.url)
# Print the lyric
#print(response.text)

'''
http://localhost:3000/lyrics/random?artist=Deep+Purple&include_track=True
Come on, come on, come on. Let's go space truckin' - Deep Purple, Space Truckin
'''

# Status Codes
# 1XX -> Informational responses.
# 2XX -> Successful responses.
# 3XX -> Redirection message.
# 4XX -> Client error responses.
# 5XX -> Server error responses.
# Most common -> 200 OK - 404 Not Found - 500 Internal Server Error

response = requests.get('http://localhost:3000/movies')

# Check if the response.status_code is equal to the requests.codes value for "200 OK"
if (response.status_code == requests.codes.ok):
    print('The server responded succesfully!')
  
# Or if the request was not successful because the API did not exist, 404
elif (response.status_code == requests.codes.not_found):
    print('Oops, that API could not be found!')

###################################
# Add a header to use in the request
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code  == requests.codes.not_acceptable):
    print('The server can not respond in XML')
    
    # Print the accepted content types
    print('These are the content types the server accepts: ' + response.headers['accept'])
else:
    print(response.text)

'''
The server can not respond in XML
These are the content types the server accepts: application/json, text/plain
'''