############### Blackjack Project 
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#I'm ignoring the above list of cards and creating a dictionary with keys that are prettier :-)

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
  "A♦️": 11,
  "2♦️": 2,
  "3♦️": 3,
  "4♦️": 4,
  "5♦️": 5,
  "6♦️": 6,
  "7♦️": 7,
  "8♦️": 8,
  "9♦️": 9,
  "J♦️": 10,
  "Q♦️": 10,
  "K♦️": 10,
  "A♠": 11,
  "2♠": 2,
  "3♠": 3,
  "4♠": 4,
  "5♠": 5,
  "6♠": 6,
  "7♠": 7,
  "8♠": 8,
  "9♠": 9,
  "J♠": 10,
  "Q♠": 10,
  "K♠": 10,
  "A❤️": 11,
  "2❤️": 2,
  "3❤️": 3,
  "4❤️": 4,
  "5❤️": 5,
  "6❤️": 6,
  "7❤️": 7,
  "8❤️": 8,
  "9❤️": 9,
  "J❤️": 10,
  "Q❤️": 10,
  "K❤️": 10,
]

player_hand = []
player_total = 0

dealer_hand = []
dealer_total= 0

#populate player initial hand
def initial_hand():
  '''Populates player and computers initial hands'''
  player_hand = random.sample(inf_deck_dict.items(), 2)
  print(player_hand) 

  dealer_hand = random.sample(inf_deck_dict.items(), 2)
  print(dealer_hand)
  
  first_plr_card = (player_hand[0])[0]
  second_plr_card = (player_hand[1])[0]
  def player_total():
    for each in player_hand:
      #work on player hand 2nd item addition tomorrow
  first_dlr_card = (dealer_hand[0])[0]
  second_dlr_card = (dealer_hand[1])[0]
  
  print(first_plr_card)
  print(second_plr_card)
  print(first_dlr_card)
  print(second_dlr_card)
initial_hand()


#print(len(inf_deck_dict)), Deck length is 48



#Black Jack Game Logic

#1 Check if Player initial hand == 21
  #If yes then check if dealer additional one card hand equals 21
    #Tie 
  #Elif Player hand == 21 and dealer hand <21 or >21 
    #Player Wins
#2 if player hand is < 21 ask player if they want another card (add this card to total)
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
