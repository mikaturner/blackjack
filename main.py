############### Blackjack Project 
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#I'm ignoring the above list of cards and creating a tuple list with cards and values because it's prettier :-)

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
inf_deck = [
  ("A☘️", 11),
  ("2☘️", 2),
  ("3☘️", 3),
  ("4☘️", 4),
  ("5☘️", 5),
  ("6☘️", 6),
  ("7☘️", 7),
  ("8☘️", 8),
  ("9☘️", 9),
  ("J☘️", 10),
  ("Q☘️", 10),
  ("K☘️", 10),
  ("A♦️", 11),
  ("2♦️", 2),
  ("3♦️", 3),
  ("4♦️", 4),
  ("5♦️", 5),
  ("6♦️", 6),
  ("7♦️", 7),
  ("8♦️", 8),
  ("9♦️", 9),
  ("J♦️", 10),
  ("Q♦️", 10),
  ("K♦️", 10),
  ("A♠", 11),
  ("2♠", 2),
  ("3♠", 3),
  ("4♠", 4),
  ("5♠", 5),
  ("6♠", 6),
  ("7♠", 7),
  ("8♠", 8),
  ("9♠", 9),
  ("J♠", 10),
  ("Q♠", 10),
  ("K♠", 10),
  ("A❤️", 11),
  ("2❤️", 2),
  ("3❤️", 3),
  ("4❤️", 4),
  ("5❤️", 5),
  ("6❤️", 6),
  ("7❤️", 7),
  ("8❤️", 8),
  ("9❤️", 9),
  ("J❤️", 10),
  ("Q❤️", 10),
  ("K❤️", 10),
]

player_hand = []
player_total = 0

dealer_hand = []
dealer_total= 0

#Pull a random card from deck
def random_card(num_cards):
    '''Function takes input of player or dealer hand list to add card to and number of cards to add'''
    new_cards = random.sample(inf_deck, num_cards)
    return new_cards

#Function for summing values of hands
def hand_total(hand):
    '''Function takes dealer or player hand, and associated total and adds together card values and returns it to player_total or dealer_total'''
    total = 0
    for card in hand:  
        total += card[1]
    return total

#populate player's initial hand
player_hand = random_card(2)
player_total = hand_total(player_hand)

#populate dealer's initial hand
dealer_hand = random_card(2)
dealer_total = hand_total(dealer_hand)

#How to pull values out of tuple list for each hand  

first_plr_card = (player_hand[0])[0]
second_plr_card = (player_hand[1])[0]

first_dlr_card = (dealer_hand[0])[0]
second_dlr_card = (dealer_hand[1])[0]

def player_string(hand):
  '''Creates a string to describe player hand depending on current cards in hand'''
  part_1 = "Your hand is "
  card_string = ""
  just_cards = []
  for card in hand:
      just_cards.append(card[0])
  card_string = " and ".join(just_cards)        
  part_2 = f" for a total of {player_total}."
  return part_1 + card_string + part_2

print(player_string(player_hand))  
#print(f"Your hand is {first_plr_card} and {second_plr_card} for a total of {player_total}")

print(f"Dealer's first card is {first_dlr_card}")

#Black Jack Game Logic

#1 Check if Player initial hand == 21
  #If yes then check if dealer additional one card hand equals 21
    #Tie 
if player_total == 21 & dealer_total == 21:
    print("It's a Tie!")

#elif Player hand == 21 and dealer hand <21 or >21 Player Wins
elif player_total == 21:
    print("You Win!")

#elif player hand is < 21 ask player if they want another card (add this card to total)  
elif player_total < 21:
    another_card = (input("Do you want another card? 'y'or'n': ")).lower()
    if another_card == 'y':
        new_card = random_card(1)
        player_hand += new_card
        hand_total(player_hand)  

    #If total is >21 player Busts and Dealer Wins
    #If player hand is <21 ask if they want another card and repeat  step two logic if they do want another card
    #Elif if player hand is < 21 and they hold move on to dealer Hand
#3 Dealer hand, add an additional card 
  #if dealer hand > 21 
      # Dealer Busts
  #if dealer hand < 17
      # Add another card to dealer hand and check above logic (aka if >21 dealer busts)
  #else draw another card and check if > 21 (bust)
  # or < 17 draw
  #if !<17 and !>21 compare dealer hand value to player hand value, whomever has highest hand wins, if scores are == then tie
