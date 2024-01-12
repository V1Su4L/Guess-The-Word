import random
import time

# List of quotes
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

re_match = True

while re_match:
    # Select a random quote
    choice = random.choice(quotes)
    chosen = ['_' * len(word) for word in choice]
    under_sentence = ' '.join(chosen)
    full_sentence = ' '.join(choice)
    score = 0
    start_time = time.time()

    while '_' in under_sentence:
        guess = input(f'The expression is "{under_sentence}", guess a character: \n')

        if guess == 'exit':
            print('Left in the middle')
            re_match = False
            break

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue

        if guess in full_sentence and guess not in under_sentence:
            print('Correct Answer')
            score += 5
            correct = [index for index, char in enumerate(full_sentence) if char == guess]
            under_sentence = ''.join([guess if i in correct else under_sentence[i] for i in range(len(under_sentence))])
        elif guess in under_sentence:
            print('Guessed already, try again...')
        else:
            print('Letter not in the sentence, try again...')
            score -= 1

    if (time.time() - start_time) < 30:
        print('Fast answer, here is a bonus of 100 points.')
        score += 100

    print(f'You guessed the whole sentence, it was: {full_sentence},\nScore: {score}\n')

    while True:
        re_match = input("Would you like to play another round? (Y/N) \n").upper()
        if re_match in {'Y', 'N'}:
            break
        else:
            print("Please enter either 'Y' or 'N'.")

if re_match == 'N':
    print("Thanks for playing the game... Bye bye!\n")
