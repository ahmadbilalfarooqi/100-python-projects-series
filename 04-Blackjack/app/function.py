# all function define here

import sys
import random

# set up the constant:
HEARTS = chr(9829) # character 9829 is '♥️'
DIAMONDS = chr(9830) # character 9830 is '♦️'
SPADES = chr(9824) # character 9824 is '♠️'
CLUB = chr (9827) # character 9827 is '♣️'

BACKSIDE = 'backside'

# =======================================================
# getBet function start here
def getBet(maxBet):
    '''Ask the player how much they want to bet for this round'''

    while True: # keep asking until they enter a valid amount.
        print('How much do you? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
            
        if not bet.isdecimal():
            continue # if the player didn't enter a number, ask again.
        
        bet = int(bet)
        if 1 <=bet <= maxBet:
            return bet # player entered a valid bet.
        
        
# ======================================================
# getDeck function start here
def getDeck():
    '''Return a list of (rank, suit) tuples for all 52 cards.'''
    deck=[]
    for suit in (HEARTS, DIAMONDS, SPADES, CLUB):
        for rank in range(2,11):
            deck.append((str(rank), suit)) # add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # add the face and ace cards.
            
    random.shuffle(deck)
    return deck


# =============================================================
# displayHands function start here
def displayHands(playerHand, dealerHand, showDealerHand):
    '''Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False'''
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # hide the dealer's first card:
        displayCards ([BACKSIDE] + dealerHand[1:])
        
    # show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)
    
    
# =================================================================
# getHandValue function start here
def getHandValue(cards):
    '''Returns the value of the cares. Face cards are worth
    10, aces are worth 11 or 1 (this function picks the most suitable ace value).'''
    value = 0
    numberOfAces =0
    
    # add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces +=1
        elif rank in ('K', 'Q', 'J'): # face cards are worth 10 points.
            value += 10
        else: 
            value +=int(rank) # numbered cards are worth their number.
            
            
    # add the value for the aces:
    value +=numberOfAces # add 1 per ace.
    for i in range(numberOfAces):
        # if another 10 can be added with busing, do so:
        if value + 10 <= 21:
            value += 10
    return value


# ==============================================================================
# displayCards function start here
def displayCards(cards):
    '''Display all the cards in the cards list.'''
    rows =  ['', '', '', '', ''] # The text to display on each row.
    
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|## | '
            rows[3] += '|## | '
        else:
            # print the card's front:
            rank, suit = card # the card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
            
    ## print each row on the screen:
    for row in rows:
        print(row)



# ======================================================================
# getMove function start here
def getMove(playerHand, money):
    '''Asks the player for their move, and returns 'H'for hit,
    'S' for stand, and 'D'for double down.
    '''
    while True: # keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']
        
        # the player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
            
        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move # player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # player has entered a valid move.
        
        