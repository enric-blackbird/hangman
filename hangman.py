from random import choice
import words

def get_unique_letters(word):
    unique_letters = set()
    for letter in word:
        unique_letters.add(letter)
    return unique_letters

def ask_dificulty_level():
    selected_difficulty = ''
    while (selected_difficulty in words.difficulty_levels) == False:
        selected_difficulty = input('Please select your difficulty level: easy, medium, hard: ')
        selected_difficulty = selected_difficulty.lower()
    return selected_difficulty

def get_random_word(difficulty_level):
    return choice(words.difficulty_levels[difficulty_level])

def generate_discovered_word(secret_word, requested_letters):
    discovered_so_far = ''
    for letter in secret_word:
        if (letter in requested_letters):
            discovered_so_far += ' ' + letter + ' '
        else:
            discovered_so_far += ' _ '
    return discovered_so_far

remaining_lifes = 7

difficulty_level = ask_dificulty_level()
secret_word = get_random_word(difficulty_level)

requested_letters = set()
remaining_letters = get_unique_letters(secret_word)


while remaining_lifes > 0 and len(remaining_letters) > 0:

    print(generate_discovered_word(secret_word, requested_letters))
    print('Remaining lifes:', remaining_lifes)

    requested_letter = input('What letter would you like to try now? ')

    if len(requested_letter) != 1 or requested_letter.isalpha() == False:
        print('Please choose a single letter.')
        continue

    requested_letter = requested_letter.upper()

    if requested_letter in requested_letters:
        print('You already used that letter.')
        continue

    if requested_letter in secret_word:
        print('Awesome! ' + requested_letter + ' is a secret letter!')
        remaining_letters.remove(requested_letter)
    else:
        print('Oh no! ' + requested_letter + ' is not in the secret word!')
        remaining_lifes -= 1

    requested_letters.add(requested_letter)

if (remaining_lifes == 0):
    print('It is OK to be a loser.')
elif (remaining_lifes == 7):
    print('Dude you are amazing!')
else:
    print('Congratulations, you won!')

print('The secret word was: ' + secret_word)
