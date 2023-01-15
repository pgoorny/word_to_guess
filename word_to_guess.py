import random
import requests

def word_to_guess_generator():
    global display
    global letters
    global word_to_guess_decoded
### get random english word from the internet 
    word_site = 'http://www.mit.edu/~ecprice/wordlist.10000'
    response = requests.get(word_site)
    words = response.content.splitlines()
    word_to_guess = random.choice(words)
    word_to_guess_decoded = word_to_guess.decode("utf-8")
### list the word like [r, a, n, d, o, m]
    letters = list(word_to_guess_decoded)
### present the word like '_ _ _ _ _ _'
    display = '_' * len(word_to_guess_decoded)
    return display, letters, word_to_guess_decoded

def play():
    global display
    global letters
    global word_to_guess_decoded
    
    play = True
    while play:
        guess = input(f'Word to guess is: {display}. Guess a letter: ')
### if guessed letter is in word's list of letters, run a loop which checks if a guessed letter exists more than one time
        if guess in letters:
            n = -1
            for i in letters:
                if i == guess:
                    n += 1
### release guessed letter in in all positions
                    display = display[:n] + guess + display[n + 1:]
### if all words are releasedm then the game is over
                    if str(word_to_guess_decoded) == str(display):
                        play = False 
                        print(f'You guessed! The word to guess was: {word_to_guess_decoded}')
                        play_again()
                else:
                    n += 1 
        else:
            print('Try the letter again!')

def play_again():
        print('Do you want to play again? If yes, press [y]. If no, press [n]')
        
        while True:
            play_again = input()
            if play_again.lower() not in ['y', 'n']:
                print('Press again')
            if play_again.lower() == 'y':
                word_to_guess_generator()
                play()
                break
            if play_again.lower() == 'n':
                break

word_to_guess_generator()
play()




