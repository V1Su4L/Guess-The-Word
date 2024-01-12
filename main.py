# imports
import random

# list of quotes:
quotes = [
    ['Act', 'as', 'if'],
    ['Act', 'without', 'expectation'],
    ['All', 'is', 'well'],
    ['Allow', 'for', 'delays'],
    ['Always', 'be', 'honest'],
    ['Always', 'be', 'yourself'],
    ['Always', 'deliver', 'quality'],
    ['Ask', 'powerful', 'questions'],
    ['Audit', 'your', 'metrics'],
    ['Audit', 'your', 'mistakes']
]

# selecting 1 random sentences.
choice = list(random.sample(quotes, k=1))
print(choice)

# print sentences as '_'
for i in range(len(choice)):
    sentence = ' '.join(['_' * len(word) for word in choice[i]])
    print(sentence)

# get user input
user_input = input('Enter 1 character: ')
