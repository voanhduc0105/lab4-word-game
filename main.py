# Hangman game logic utilities

def validate(guess: str, guessed_letters: list[str]) -> str:
    """
    Validates a guess: must be single letter, alphabetic, not previously guessed, and not empty.
    Returns error message or None if valid.
    """
    if guess == '':
        return "Guessed word cannot be empty."
    if len(guess) > 1:
        return "Guessed word should only be 1 letter."
    if not guess.isalpha():
        return "Guessed word should be an alphabet character. No numbers or special characters."
    if guess in guessed_letters:
        return "Letter has already been guessed. Do another guess!"
    return None

def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
    """
    Updates game state: appends guess to list, decrements lives if incorrect, increments score if correct.
    Returns updated guessed_letters and lives.
    """
    guessed_letters.append(guess)
    if guess in secret_word:
        return (guessed_letters, lives)
    else:
        lives -= 1
        return (guessed_letters, lives)    


words = {
    '1': ['apple', 'fruit', 'chair', 'house', 'water', 'bread', 'grass', 'cloud', 'horse', 'light'],
    '2': ['jungle', 'cactus', 'basket', 'frozen', 'magnet', 'rocket', 'pirate', 'shadow', 'planet', 'bridge'],
    '3': ['oxygen', 'rhythm', 'syntax', 'quartz', 'sphinx', 'nymph', 'cryptic', 'vortex', 'eclipse', 'phantom']
}

import os as o
import time as ti
import random as rand
import ast



def enterdel():
    input('Press Enter to continue...')
    o.system('clear')

def timedel(t):
    ti.sleep(t)
    o.system('clear')

flag = 0
hangman = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]

history = {}
computerguess = []

def main_menu():
    global history
    choice = ""
    while choice != "5":
        o.system('clear')
        print('Hangman Game\n--------------------')
        print('1. Start Game')
        print('2. Show Records')
        print('3. Load Records')
        print('4. Save Records')
        print('5. Exit Game\n')
        choice = input('Select a mode (1-5): ')
        
        if choice == '1':
            play_game()
        elif choice == '2':
            show_records()
        elif choice == '3':
            load_records()
        elif choice == '4':
            save_records()
        elif choice == '5':
            break
        else:
            print('Invalid choice.')
            timedel(0.5)

def play_game():
    global history
    o.system('clear')
    diff = ""
    while diff not in ('1', '2', '3', '4'):
        print('Game Difficulty\n--------------------')
        print('1. Easy')
        print('2. Normal')
        print('3. Hard')
        print('4. Return\n')
        diff = input('Select a difficulty (1-4): ')
        if diff not in ('1', '2', '3', '4'):
            print('Invalid choice.')
            timedel(0.5)
    
        
    if diff == '4':
        return
    
    timedel(0.5)
    mode = ""
    while mode not in ('1', '2'):
        print('Game Mode\n--------------------')
        print('1. Singleplay')
        print('2. Auto-Play\n')
        mode = input('Select game mode (1-2): ')
        if mode not in ('1', '2'):
            print('Invalid choice.')
            timedel(0.5)
    if mode == '1':
        singleplay(diff)
    elif mode == '2':
        autoplay(diff)


def autoplay(diff):
    # The bot should try to guess AEIOU first
    global computerguess
    secret_word = words[diff][rand.randint(0, len(words[diff])-1)].upper()
    fails = 0
    while secret_word in computerguess:
        fails += 1
        secret_word = words[diff][rand.randint(0, len(words[diff])-1)].upper()
        if fails > 10:
            break
    computerguess.append(secret_word)

    cons = 'BCDFGHJKLMNPQRSTVWXYZ'
    # there is a 10% chance for the computer to know what the word is, sort of.
    if rand.randint(1, 10) == 3:
        consonants = secret_word
        while len(consonants) < 12:
            l = cons[rand.randint(0, len(cons)-1)]
            if l not in consonants:
                consonants += l
    else:
        consonants = cons
    vowels = 'AEIOU'
    vowc = 0
    guessed = []
    lives = 6
    score = 0
    difficulty = 'Easy' if diff == '1' else 'Normal' if diff == '2' else 'Hard'
    timedel(1)
    if fails < 10:
        if secret_word != '':
            while lives > 0 and score != len(secret_word):
                o.system('clear')
                print(f'Difficulty: {difficulty}')
                print(f'The computer have {lives} tries left!')
                print(hangman[6-lives])
                print('\nWord:          ', end='')
                display_letters = ''
                for i in secret_word:
                    if i in guessed:
                        display_letters += f' {i.upper()} '
                    else:
                        display_letters += ' _ '
                print(display_letters)
                if len(guessed) == 0:
                    print('The computer have not made any guesses yet!')
                else:
                    letters = ''
                    for i in range(len(guessed)):
                        if i != len(guessed) - 1:
                            letters += f'{guessed[i]}, '
                        else:
                            letters += f'{guessed[i]}.'
                    print(f'Guessed letters: {letters}')

                if vowc <= len(vowels)-1:
                    # it has not guessed all vowels
                    # again, no string manip, so we just select and rerun.
                    guess = vowels[rand.randint(0, len(vowels)-1)]
                    while guess in guessed:
                        guess = vowels[rand.randint(0, len(vowels)-1)]
                    vowc += 1
                else:
                    guess = consonants[rand.randint(0, len(consonants)-1)]
                    while guess in guessed:
                        guess = consonants[rand.randint(0, len(consonants)-1)]
                
                ti.sleep(1)

                error = validate(guess, guessed)
                if error:
                    print(error)
                else:
                    print(f'The computer guessed {guess}.')
                    ti.sleep(1)
                    guessed, temp_lives = update_game_state(secret_word, guessed, guess, lives)
                    if lives != temp_lives:
                        print('It was the wrong letter!')
                        lives = temp_lives
                        ti.sleep(1)
                    else:
                        print('It was the correct letter!')
                        score += secret_word.count(guess)
                        ti.sleep(1)

            o.system('clear')
            if lives == 0:
                print('The computer lost!')
                print(hangman[6])
                print('\nWord:          ', end='')
                display_letters = ''
                for i in secret_word:
                    display_letters += f' {i.upper()} '
                print(display_letters)
                print(f'The word was: {secret_word.upper()}\n')
                enterdel()
            else:
                print('The computer won!')
                print(hangman[6-lives])
                print('\nWord:          ', end='')
                display_letters = ''
                for i in secret_word:
                    display_letters += f' {i.upper()} '
                print(display_letters)
                print(f'The word was: {secret_word.upper()}\n')
                enterdel()
            
            history[f'{len(history)+1}'] = {'word': secret_word, 'state': 'LOSE' if lives == 0 else 'WIN', 'difficulty': difficulty, 'wrong_guesses': 6-lives, 'gamemode': 'Auto Play'}
        else:
            print('Failed to select word. Returning...')
            timedel(1)
    else:
        print('Out of words. Returning...')
        timedel(1)


def singleplay(diff):
    secret_word = words[diff][rand.randint(0, len(words[diff])-1)].upper()
    guessed = []
    lives = 6
    score = 0
    difficulty = 'Easy' if diff == '1' else 'Normal' if diff == '2' else 'Hard'
    timedel(1)
    if secret_word != '':
        while lives > 0 and score != len(secret_word):
            o.system('clear')
            print(f'Difficulty: {difficulty}')
            print(f'You have {lives} tries left!')
            print(hangman[6-lives])
            print('\nWord:          ', end='')
            display_letters = ''
            for i in secret_word:
                if i in guessed:
                    display_letters += f' {i.upper()} '
                else:
                    display_letters += ' _ '
            print(display_letters)
            if len(guessed) == 0:
                print('You have not made any guesses yet!')
            else:
                letters = ''
                for i in range(len(guessed)):
                    if i != len(guessed) - 1:
                        letters += f'{guessed[i]}, '
                    else:
                        letters += f'{guessed[i]}.'
                print(f'Guessed letters: {letters}')
            guess = input('Guess letter: ').strip().upper()
            error = validate(guess, guessed)
            if error:
                print(error)
            else:
                guessed, temp_lives = update_game_state(secret_word, guessed, guess, lives)
                if lives != temp_lives:
                    lives = temp_lives
                else:
                    score += secret_word.count(guess)
        
        o.system('clear')
        if lives == 0:
            print('You lost!')
            print(hangman[6])
            print('\nWord:          ', end='')
            display_letters = ''
            for i in secret_word:
                display_letters += f' {i.upper()} '
            print(display_letters)
            print(f'Your word was: {secret_word.upper()}\n')
            enterdel()
        else:
            print('You won!')
            print(hangman[6-lives])
            print('\nWord:          ', end='')
            display_letters = ''
            for i in secret_word:
                display_letters += f' {i.upper()} '
            print(display_letters)
            print(f'Your word was: {secret_word.upper()}\n')
            enterdel()
        
        history[f'{len(history)+1}'] = {'word': secret_word, 'state': 'LOSE' if lives == 0 else 'WIN', 'difficulty': difficulty, 'wrong_guesses': 6-lives, 'gamemode': 'Single Play'}
    else:
        print('Failed to select word. Returning...')
        timedel(1)

def show_records():
    o.system('clear')
    print('Show Records\n--------------------')
    if len(history) == 0:
        print('Nothing is here. Please start a new game or load records!\n')
    else:
        for i in history:
            print(f'{i}. Word: {history[i]['word']}')
            print(f'   - Difficulty: {history[i]['difficulty']}')
            print(f'   - State: {history[i]['state']}')
            print(f'   - Wrong Guesses: {history[i]['wrong_guesses']}')
            print(f'   - Gamemode: {history[i]['gamemode']}')
            print('--------------------')
    enterdel()

def load_records():
    global history
    o.system('clear')
    print('Load Records\n--------------------')
    try:
        with open('save.txt', 'r') as f:
            history = ast.literal_eval(f.read())
        print('Save File Found!')
        ti.sleep(0.5)
        print('Load Complete!\n')
        enterdel()
    except FileNotFoundError:
        print('No Saves Found. Creating New Save.')
        with open('save.txt', 'w') as f:
            f.write(str(history))
        ti.sleep(0.5)
        print('New Save File Created!\n')
        enterdel()

def save_records():
    o.system('clear')
    print('Save Records\n--------------------')
    with open('save.txt', 'w') as f:
        f.write(str(history))
    ti.sleep(0.5)
    print('File Saved!\n')
    enterdel()

if __name__ == "__main__":
    main_menu()