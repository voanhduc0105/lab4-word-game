# Hangman game logic utilities

def validate(guess: str, guessed_letters: list[str]) -> str:
    if len(guess) > 1:
        return "Guessed word should only be 1 letter."
    if not guess.isalpha():
        return "Guessed word should be an alphabet character. No numbers or special characters."
    if guess in guessed_letters:
        return "Letter has already been guessed. Do another guess!"
    return None

def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
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

while flag < 5:
    o.system('clear')
    print('Hangman Game\n--------------------')
    print('1. Start Game')
    print('2. Show Records')
    print('3. Load Records')
    print('4. Save Records')
    print('5. Exit Game\n')
    flag = input('Select a mode (1-5): ')
    if flag not in ('1', '2', '3', '4', '5'):
        print('Invalid choice.')
        timedel(0.5)
    else:
        flag = int(flag)
        if flag == 1:
            diff = 0
            while diff not in ('1', '2', '3', '4'):
                timedel(0.5)
                print('Game Difficulty\n--------------------')
                print('1. Easy')
                print('2. Normal')
                print('3. Hard')
                print('4. Return')
                diff = input('Select a difficulty (1-4): ')
                if diff not in ('1', '2', '3', '4'):
                    print('Invalid choice.')
                    timedel(0.5)
            if diff == '4':
                pass
            else:
                secret_word = words[diff][rand.randint(0, len(words[diff])-1)].upper()
                guessed = []
                lives = 6
                score = 0
                difficulty = 'Easy' if diff == '1' else 'Normal' if diff == '2' else 'Hard'
                timedel(1)
                if secret_word != '': 
                    while lives > 0 and score != len(secret_word):
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
                        guess = input('Guess letter: ')
                        guess = guess.upper()
                        error = validate(guess, guessed)
                        if error:
                            print(error)
                        else:
                            guessed, temp_lives = update_game_state(secret_word, guessed, guess, lives)
                            if lives != temp_lives:
                                lives = temp_lives
                            else:
                                score+=secret_word.count(guess)
                        o.system('clear')
                    if lives == 0:
                        print('You lost!')
                        print(hangman[6])
                        print('\n\nWord:          ', end='')
                        print(display_letters)
                        print(f'Your word was: {secret_word.upper()}\n')
                        enterdel()
                    else:
                        print('You won!')
                        print(hangman[6-lives])
                        print('\n\nWord:          ', end='')
                        display_letters = ''
                        for i in secret_word:
                            if i in guessed:
                                display_letters += f' {i.upper()} '
                            else:
                                display_letters += ' _ '
                        print(display_letters)
                        print(f'Your word was: {secret_word.upper()}\n')
                        enterdel()
                    history[f'{len(history)+1}'] = {'word': secret_word, 'state': 'LOSE' if lives == 0 else 'WIN', 'difficulty': difficulty, 'wrong_guesses': 6-lives,}
                        
                else:
                    print('Failed to select word. Returning...')
                    timedel(1)
        elif flag == 2:
            timedel(0.5)
            print('Show Records\n--------------------')
            if len(history) == 0:
                print('Nothing is here. Please start a new game or load records!\n')
                
            else:
                for i in history:
                    print(f'{i}. Word: {history[i]['word']}')
                    print(f'   - Difficulty: {history[i]['difficulty']}')
                    print(f'   - State: {history[i]['state']}')
                    print(f'   - Wrong Guesses: {history[i]['wrong_guesses']}')
                    print('--------------------')
            enterdel()
        elif flag == 3:
            timedel(0.5)
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
        elif flag == 4:
            timedel(0.5)
            print('Save Records\n--------------------')
            with open('save.txt', 'w') as f:
                f.write(str(history))
            ti.sleep(0.5)
            print('File Saved!\n')
            enterdel()
