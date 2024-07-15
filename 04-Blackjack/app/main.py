'''
04-Project-Blackjack-Game
Blackjack, also known as 21, is a card game
where players try to get as close to 21 points
as possible without going over. This program
uses images drawn with text characters, called
ASCII art. American Standard Code for Information
Interchange (ASCII) is a mapping of text characters
to numeric codes that computers used before Unicode
replaced it.
'''

import sys
from function import getBet, displayHands, getHandValue, getDeck, getMove



def main ():
    print('''
          Blackjack Game by Ahmad Bilal <ahmadbilal20152016@gmail.com>
          Rules :
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through are worth their face value.
            (H) it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet 
            but must hit exactly one more time before standing. 
            In case of a lie, the bet is returned to the player.
            The dealer stops hitting at 17.
          ''')
    
    money = 5000
    while True: # main game loop
        # check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()
        
        # Let the player enter their bet for this round:
        print("Money:", money)
        bet = getBet(money)
        
        # give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerhand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        
        # Handle player actions:
        print("Bet: ", bet)
        while True: # keep looping until player stands or busts.
            displayHands (playerHand, dealerhand, False)
            print()
            
            # check if the player has bust:
            if getHandValue(playerHand) > 21:
                break
            # get the players move, either H, S, or D:
            move = getMove(playerHand, money - bet)
            
            # handle the player actions:
            if move == 'D':
                # player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)
                
            if move in ('H', 'D'):
                # hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)
                
                if getHandValue(playerHand) > 21:
                    # the player has busted:
                    continue
                
            if move in ('S', 'D'):
                # stand/doubling down stops the player's turn.
                break
            
        # handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue (dealerhand) < 17:
                # The dealer hits:
                print('Dealer hits.....')
                dealerhand.append(deck.pop())
                displayHands(playerHand, dealerhand, False)
                
                if getHandValue(dealerhand) > 21:
                    break # the dealer has busted.
                input('Press Enter to continue....')
                print('\n\n')
                
        # show the final hands:
        displayHands(playerHand, dealerhand, True)
        
        playerValue= getHandValue(playerHand)
        dealerValue = getHandValue(dealerhand)
        
        #handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money+=bet
        elif(playerValue>21) or (playerValue < dealerValue):
            print("You lost!")
            money -=bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money+=bet
        elif playerValue == dealerhand:
            print("It's a tie, the bet is returned to you.")
        input("Press Enter to Continue.....")
        print("\n\n")
        

# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()