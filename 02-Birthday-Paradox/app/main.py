
from function import getBirthdays, getMatch

# Display the intro:
print('''Birthday Paradox, by Ahmad Bilal <ahmadbilal20152016@gmail.com>
      
      The Birthday Paradox shows us that in a grouop of N people, the odds
      that two of them have matching birthdays is surprisingly high.
      This program does a Monte Carlo simulation (that is, repeated random
      simulations) to explore this concept.
      
      (It's not actually a paradox, it's just a surprising result.)
      ''')

# set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May',
          'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # keep asking until the user enters a valid amount
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <=100):
        numBDays = int(response)
        break # user has entered a valid amount.
    
print()

# Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays= getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
        
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
    
print()    
print()    


# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
    
else: 
    print('there are notmatching birthdays.')
    
print()


#Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times....')
input('Press Enter to begin....')

print("Let's run another 100,000 simulations.")
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations run.....')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch = simMatch + 1
        
print('100,000 simulations run.')


#Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")
                    