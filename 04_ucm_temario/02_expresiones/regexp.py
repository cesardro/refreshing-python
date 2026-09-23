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

# Write a regex to match a valid email address
regex = r"[A-Za-z\d\w]+@.+\.com"
emails = ['n.john.smith@gmail.com',
          '87victory@hotmail.com', '!#mary-=@msca.net']

for example in emails:
    # Match the regex to the string
    if re.findall(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(
            email_example=example))
    else:
        print("The email {email_example} is invalid".format(
            email_example=example))

print('##############################################')

string = 'I want to see that <strong>amazing show</strong> again!'

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", " ", string)

# Print out the result
print(string_notags)

# Since it is lazy it will check one by one and once it finds the next match it will stop, it is not greedy.
# If in this case we do not use lazy expresion it would delete the whole string -> <strong>amazing show</strong>
# However in this case since it is lazy, it will delete only -> <strong>

print('##############################################')

# Write a lazy regex expression
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# ['5', '3', '6', '1', '2']

# Write a greedy regex expression
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

# ['536', '12']

print('##############################################')

# Write a greedy regex expression to match
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# ["(They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying)"]

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.+?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)

# ['(They were so cute)', "(I'm crying)"]

print('##############################################')

sentiment_analysis = ['Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',
                      'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.', 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']

# Write a regex that matches email
regex_email = r"([a-zA-Z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))

print('##############################################')

flight = 'Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)

# Print the matches
print("Airline: {} Flight number: {}".format(
    flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(
    flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

print('##############################################')

sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!',
                      'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.', "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

print('##############################################')

sentiment_analysis = ['That was horrible! I really dislike the movie The cabin and the ant. So boring.',
                      "I disapprove the movie Honest with you. It's full of cliches.", 'I dislike very much the concert After twelve Tour. The sound was horrible.']

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)

    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))

print('##############################################')

contract = 'Provider will invoice Client for Services performed within 30 days of performance.  Client will pay Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. It is understood that payments to Provider for services rendered shall be made in full as agreed, without any deductions for taxes of any kind whatsoever, in conformity with Provider’s status as an independent contractor. Signed on 03/25/2001.'

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
    "day": dates.group(2),
    "month": dates.group(1),
    "year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(
    data=signature))

print('##############################################')

html_tags = ['<body>Welcome to our course! It would be an awesome experience</body>',
             '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>', '<nav>About me Links Contact me!']


for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag = re.match(r"<(\w+)>.*?</\1>", string)

    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1)))
    else:
        # If it doesn't match capture only the tag
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))

print('##############################################')

sentiment_analysis = ['@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times',
                      'Staying at a friends house...neighborrrrrrrs are so loud-having a party', 'Just woke up an already have read some e-mail']


# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\1\w*"

for tweet in sentiment_analysis:
    # Find if there is a match in each tweet
    match_elongated = re.search(regex_elongated, tweet)

    if match_elongated:
        # Assign the captured group zero
        elongated_word = match_elongated.group(0)

        # Complete the format method to print the word
        print("Elongated word found: {word}".format(word=elongated_word))
    else:
        print("No elongated word found")


print('##############################################')

sentiment_analysis = 'You need excellent python skills to be a data scientist. Must be! Excellent python'

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=[pP]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)

print('##############################################')

cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)

for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)

print('##############################################')

print('##############################################')

print('##############################################')
