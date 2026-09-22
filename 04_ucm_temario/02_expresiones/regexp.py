# Import the re module
import re

sentiment_analysis = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

sentiment_analysis = "Agh,snow! User_mentions:9, likes: 5, number of retweets: 4"

print(re.findall(r"User_mentions:\d", sentiment_analysis))
print(re.findall(r"likes:\s\d", sentiment_analysis))
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))

sentiment_analysis = "He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready."

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)

print('##############################################')

# This is a Pandas Series.

for tweet in sentiment_analysis:
    # Write regex to match http links and print out result
    print(re.findall(r"http\S+", tweet))

    # Write regex to match user mentions and print out result
    print(re.findall(r"@\w+\d*", tweet))

# Output:
"""
    ['https://www.tellyourstory.com']
    ['@blueKnight39']
    []
    ['@anitaLopez98', '@MyredHat31']
    ['https://radio.foxnews.com']
    ['@YourBestCompany', '@foxRadio']
"""

for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\s\w+\s\w+", date))

"""
['32 minutes ago']
"""

for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w{1,2}\s\w+\s\d{4}", date))

"""
['1st May 2019']
['23rd June 2018']
"""

for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w{1,2}\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))

"""
['23rd June 2018 17:54']
"""

print('##############################################')

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))

""" 
['ITS', 'NOT', 'ENOUGH', 'TO', 'SAY', 'THAT', 'IMISS', 'U', '']
"""

print('##############################################')

print('##############################################')

print('##############################################')
