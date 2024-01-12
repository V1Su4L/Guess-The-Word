# imports
import random, time

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
reMatch = True
while reMatch:
    # selecting 1 random sentences.
    choice = quotes[random.randint(0, len(quotes) - 1)]
    chosen = []
    # print sentences as '_'
    for word in choice:
        chosen.append('_' * len(word))

    under_sentence = ' '.join(chosen)
    full_sentence = ' '.join(choice)
    score = 0
    start_Time = 0
    while '_' in under_sentence:
        guess = input(f'The expression is "{under_sentence}", guess a character: \n')
        # exit in the middle
        if guess == 'exit':
            print('Left in the middle')
            break
        # check if the length of the input is more than 1
        if len(guess) > 1:
            print('there too much characters, please enter 1 character each time')
            continue
        # check if the input is a letter.
        if not guess.isalpha():
            print('please enter only letters.')
            continue
        # check if this is correct answer and first time guessed
        if guess in full_sentence and guess not in under_sentence:
            print('Correct Answer')
            score += 5
            correct = [index for index, char in enumerate(full_sentence) if char == guess]
            for i in correct:
                under_sentence = under_sentence[:i] + guess + under_sentence[i + 1:]
        # if letter guessed before
        elif guess in under_sentence:
            print('guessed already, try again...')
            continue
        # if letter is not in the string
        elif guess not in full_sentence:
            print('letter not in the sentence, try again... ')
            score -= 1
            continue
        # check if the user didn't put exit:
    if guess != 'exit':
        # check how many seconds it took to the user to complete the task
        if (time.time() - start_Time) < 30:
            print('Fast answer, here is a bonus of 100 points.')
            score += 100
            print(f'you guessed the whole sentence, it was: {full_sentence} ,\n score: {score}\n ')
            # while the user didn't enter Y or N, he'll be prompted again and again
    while reMatch != 'Y' or reMatch != 'N':
        reMatch = input("Would you like to play another round?(Y/N) \n")
        # The user doesn't want to continue for another round, exiting game
        if reMatch == 'N':
            reMatch = False
            print("thanks for playing the game...Bye bye!\n")
            break
        # The user wants to play once more
        elif reMatch == 'Y':
            reMatch = True
            print("Ok, so we're playing another round!\n")
            startTime = time.time()
            break
