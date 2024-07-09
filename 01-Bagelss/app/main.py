
from function import getSecretNum, getClues
from function import NUM_DIGITS, MAX_GUESSES



def main():
    print(
        
'''     Bagels, a deductive logic game By Ahmad Bilal <Python Developer>.
          
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        
        When I say:             That means:
          
        Pico                    One digit is correct but in the wrong position.
        Fermi                   One digit is correct and in the right position.
        Bagels                  No digit is correct.
            
        For example, if the secret number was 248 and you guessed 843, the
        clues would be Fermi Pico.'''.format(NUM_DIGITS))
          
    while True: # Main game loop.
        # this stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
    
    
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        
    
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
    
if __name__ == '__main__':
    main()