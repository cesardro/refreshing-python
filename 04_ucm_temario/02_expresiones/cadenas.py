from string import Template
from datetime import datetime
movie = 'oh my God! desserts I stressed was an ugly movie'

# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
    print(movie_title)

print('##############################################')

movie = 'the film,however,is all good<\i>'

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = ' '.join(movie_no_comma)
print(movie_join)

print('##############################################')

file = 'mtv films election, a high school comedy, is a current example\nfrom there, director steven spielberg wastes no time, taking us into the water on a midnight swim'

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(',')
    print(substring_split)


print('##############################################')

movies = """Word not found
I believe you I always said that the actor is amazing in every movie he has played
it's astonishing how frightening the actor norton looks with a shaved head and a swastika on his chest.
200    it's clear that he's passionate about his beli...
201    I believe you I always said that the actor act...
202    it's astonishing how frightening the actor act...
"""

for movie in movies:
    # If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))

print('##############################################')

wikipedia_article = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.'
my_list = []

# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
    print(my_string.format(first_pos, second_pos))


print('##############################################')

courses = ['artificial intelligence', 'neural networks']
# Create a dictionary
plan = {
    "field": courses[0],
    "tool": courses[1]
}

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))

print('##############################################')


# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"
print(message.format(today=get_date))

print('##############################################')

fact1 = 21
field1 = 'sexiest job'
fact2 = 2500000000000000000
field2 = 'data is produced daily'
field3 = 'Individuals'
fact3 = 72.41415415151
fact4 = 1.09

print(f"Data science is considered {field1!r} in the {fact1:d}st century")

print(f"About {fact2:e} of {field2} in the world")

print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

print('##############################################')

number1 = 120
number2 = 7
string1 = 'httpswww.datacamp.com'
list_links = ['www.news.com', 'www.google.com', 'www.yahoo.com',
              'www.bbc.com', 'www.msn.com', 'www.facebook.com', 'www.news.google.com']

print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:.2f}% of the posts contain links")

east = {
    "date": datetime(2023, 5, 15),
    "price": 1232443
}

# Access values of date and price in east dictionary
print(
    f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

print('##############################################')

tools = ['Natural Language Toolkit', '20', 'month']
# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template(
    "We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))

print('##############################################')

answers = {'answer1': 'I really like the app. But there are some features that can be improved'}

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")