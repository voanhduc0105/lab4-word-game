# My original Thinking

## The states of a game like Hangman:
    - Start Menu: Pretty self explanatory.
    - Show Records: Show previous records of the game, history of losing and winning, and the words in said matches
    - Difficulty Menu: Easy, Normal or Hard
    - Game Playing: Self explanatory. The entire game is here.
    - Game win: should show the word guessed, the number of guesses, the number of wins in total (Like this is the n'th win from you!)
    - Game over: Should show the word guessed, the number of lost (This is the n'th lost from you!)
    - Loading Saved Game state (Saved games should be stored in a file) (If there are no saves, create a new one instead) (saved games are only records of won and lost game. ending a game abrubtly will NOT save it into the file)
    - Instructions: Shows instruction

## Variables that are required:
    - game_state: directs the state of game (start, selection, game, end, ...) (can be integer if we know what we are doing)
    - word: a list containing the words we can guess. Can split to word easy/normal/hard. 
    - difficulty: easy, normal or hard (can be integers: 0, 1, 2)
    - wrong guesses: counts the number of wrong guesses
    - cap: limits how many wrong guesses a user can have. Default to 6
    - last_games: dictionary, logs info of previous games won and lost, structure should be something like {'game_1': {'word': 'example', 'state': 'win', 'difficulty: easy', 'wrong_guesses': 2}, 'game_2': {'word': 'cataclysm', 'state': 'lose', 'difficulty': 'normal', 'wrong_guesses': 7}, ...}
    - f: only used for file reading (aka loading saved game) (should use literal_eval() from ast library to convert string to dictionaries)

## Rules and Invariants:
    - Rules:
        + Based on the difficulty, select a secret random word (the game will do that). The higher the difficulty, the longer and complex the word is.
        + Player guess one letter at a time.
        + If the user guess correctly, show how many of that word exists within the string, and show its location as well.
        + Wrong guesses will do nothing and count up the wrong guesses count variable by 1
        + If the user guessed the word, end game in success
        + If the user ran out of chances, or when the hangman is fully drawn (or if the wrong guesses exceeds the cap), game ends in failure
 
    - Invariants:
        + The only allowed input are UPPERCASE single characters
        + Words should NOT containe hyphens, numbers or special character.
        + Secret word never gets changed once chosen
        + A letter already guessed cannot be guessed again (does not have penalty on the player though)
        + Number of Wrong guesses will never decrease (Always increase)
        + Unless specified, the cap should not change throughout the game, even when the difficulty changes
        + On top of game, show game info (like difficulty, )
        + When the user makes a correct guess, show location of letters. For example, the chosen word is CATALOGUE (On display initially, should show _ _ _ _ _ _ _ _ _). If the user guessed A, the screen should only show A, that means, the display shows _ A _ A _ _ _ _ _
        + Game ends when user win or lost, no extra turn. If the user lost, reveal the word.

## Bugs and Edge Cases:
    - Bugs:
        + Failure to pick a word. If such case happens, just exit back to the main screen, returning the error unable to select word.

    - Edge Cases:
        + If the user decided to play without loading a save file, do not log anything. Even when user load after playing a few rounds, we do not log said rounds to the file loaded.
        + User enters more than one character, like 'ab', or 'hello', or enter special characters / numbers, like '1' or '!', or enter no input. In that case, simply tell the user not to do that. Do not apply penalty.
        + Player respond with lowercase character. We can use upper() to normalize them. Do not apply penalty
        + If user already guessed the same character again, warn them. Do not apply penalty

# Copilot suggestion

## App States

    "Based on your notes in MY_NOTES.md, you've outlined a solid set of states for a Hangman-style word game: Start Menu, Show Records, Difficulty Menu, Game Playing, Game Win, and Game Over. These cover the core flow from setup to conclusion.

    To help refine this, what do you think about adding states for things like loading saved games, handling pauses, or displaying help/tutorial screens? How might the game transition between these states— for example, from Game Playing back to the Start Menu if the player quits? What assumptions are you making about user input or error handling in each state?"

## App Variables

    "Based on the Hangman game states you've outlined in MY_NOTES.md, let's think about the variables needed to support them. Variables help track data across states, like the current game progress, player history, or settings.

    What do you think are the key pieces of information that need to persist or change during gameplay? For example, in the Game Playing state, what would you need to store for the secret word, guesses, and remaining attempts? How might variables like player win/loss counts or difficulty settings connect to states like Show Records or Difficulty Menu?

    To get you started, common variables for a game like this could include:

        A string for the secret word.
        A set or list of guessed letters.
        An integer for wrong guesses (and a max limit based on difficulty).
        A dictionary or list for game records (wins, losses, words used).
        A string or enum for the current state (e.g., "start_menu", "game_playing").
        Perhaps a file path or data structure for saved games.
        What assumptions are you making about how these variables are initialized or updated between states? For instance, how would the secret word be chosen in Game Playing, and how does it relate to the Difficulty Menu?
    What assumptions are you making about how these variables are initialized or updated between states? For instance, how would the secret word be chosen in Game Playing, and how does it relate to the Difficulty Menu?"

## App Rules and Invariants

    Rules
        - Based on the difficulty level, select a random secret word (higher difficulty means longer and more complex words).
        - Players guess one letter at a time
        - Correct guesses reveal the number of instances of the letter and their positions in the word.
        - Incorrect guesses increase the wrong guesses count but have no other effect.
        - The game ends in a win if the entire word is guessed.
        - The game ends in a loss if wrong guesses exceed the cap (default of 6).
    Invariants
        - Only uppercase single characters are accepted as input.
        - Words must not contain hyphens, numbers, or special characters.
        - The secret word remains unchanged once selected.
        - Letters that have already been guessed cannot be guessed again (no penalty applied).
        - Wrong guesses counts never decrease.
        - The cap on wrong guesses does not change unless explicitly specified, even across difficulty levels.
        -Game information (e.g., difficulty) is displayed at the top of the screen.
        - Correct guesses update the display to show letter positions (e.g., for the word "CATALOGUE", initially shown as _ _ _ _ _ _ _ _ _, guessing "A" reveals _ A _ A _ _ _ _ _).
        - The game ends immediately upon win or loss; the word is revealed on loss.

## App Bugs

Common Bugs in Word Guess / Hangman Implementations
Based on typical implementations and the notes in your MY_NOTES.md, here are some frequent bugs and issues:

    Word Selection Failure: If the word list is empty, corrupted, or the random selection fails (e.g., due to an index error), the game might crash or fail to start. Mitigation: Add checks to ensure a valid word is selected; if not, return to the main menu with an error message.

Input Validation Issues:

    Accepting invalid inputs like multiple characters ("ab"), special characters ("!"), numbers ("1"), or empty strings without penalty. This can lead to unexpected behavior or crashes.
    Not normalizing case (e.g., treating lowercase as invalid instead of converting to uppercase).
    Allowing repeated guesses of the same letter without warning or penalty, potentially causing infinite loops or incorrect state.
    Guess Counting Errors:

        Off-by-one errors in wrong guesses (e.g., incrementing wrong guesses on correct inputs).
        Not incrementing counters properly, leading to inaccurate win/loss tracking.
    Display Update Problems:

        Incorrectly revealing letters (e.g., showing positions for wrong guesses or failing to update the masked word on correct guesses).
        Not handling multiple occurrences of a letter (e.g., only revealing one instance instead of all).
    Win/Loss Condition Bugs:

        Failing to detect a win when all letters are guessed (e.g., due to case mismatches or incomplete checks).
        Not ending the game when wrong guesses exceed the cap, allowing continued play.
        Revealing the word prematurely or not at all on loss.
    State Management Issues:

        Game state not resetting properly between rounds (e.g., carrying over guessed letters or wrong counts).
        Transitions between menus/states failing (e.g., not returning to start menu on quit).
    File I/O and Persistence Bugs:

        Errors loading/saving game records (e.g., file not found, corruption, or using wrong data structures like failing to parse dictionaries from strings).
        Not handling cases where saves are missing or invalid, leading to crashes.
    Edge Cases in Gameplay:

        Words with no letters (unlikely, but could cause division by zero or empty loops).
        Very long words causing display issues.
        Concurrent access to shared files (though rare in single-player).
To avoid these, implement robust input sanitization, thorough testing with edge cases, and clear error handling. Use assertions or unit tests for invariants like non-decreasing counters.


# Auto-Play addition
## My plans
    - Since there is a difficulty selector, the program SHOULD ask to play singleplayer or auto-play after one has selected a difficulty
    - Should re-use the code from maingame, but replace the user input with computer input
    - Rename the maingame code to singleplay or something similar
    - To implement computer input, I decide to force the computer to guess the vowels first (since it is the smartest move while playing hangman), then randomly select the consonants later
    - Change display to say computer select, and allow delays to let the user read what the bot is playing.

## Possible bugs and edge case
    - The random may pick the same word twice, so add a global list that tracks all the words that the bot guesses.
    - There will be a while loop which will ensure the computer doesnt pick the same word again. If all words are taken, implement a variable. If there are too many failure to pick a word, simply exit the loop
    - Unless extremely lucky, the computer cannot win due to the nature of randomness. So there will be a 10% chance for the consonants list to only include the letters of the word + a few letters, max length being 12. This ensures the computer has a slightly higher chance to win.