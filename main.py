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

# selecting 3 random sentences.
choice = list(random.sample(quotes, k=3))
print(choice)

for i in range(3):
    sentence = ' '.join(['_' * len(word) for word in choice[i]])
    print(sentence)
