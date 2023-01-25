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

first_dlr_card = (dealer_hand[0])[0]

def hand_string(hand, total, subject):
  '''Creates a string to describe player hand depending on current cards in hand'''
  part_1 = f"{subject} hand: "
  card_string = ""
  just_cards = []
  for card in hand:
      just_cards.append(card[0])
  card_string = " and ".join(just_cards)        
  part_2 = f" for a total of {total}."
  return part_1 + card_string + part_2

print(hand_string(player_hand, player_total, "Your"))  

print(f"Dealer's first card is {first_dlr_card}")

#def addtnl_card (hand, total, subject):
#  new_card = random_card(1)
#  hand += new_card
#  total= hand_total(hand)
#  if total >= 21:
#    print("Bust!")
#  print(hand_string(hand, total, subject))

#Black Jack Game Logic

#1 Check if Player initial hand == 21
  #If yes then check if dealer additional one card hand equals 21
    #Tie 
if player_total == 21 & dealer_total == 21:
    print(f"{hand_string(dealer_hand, dealer_total, 'Dealer')}")
    print("It's a Tie!")

#elif Player hand == 21 and dealer hand <21 or >21 Player Wins
elif player_total == 21:
    print(f"{hand_string(dealer_hand, dealer_total, 'Dealer')}")
    print("You Win!")

#elif player hand is < 21 ask player if they want another card (add this card to total)  
hit_stand = True
while hit_stand:
  if player_total < 21:
    another_card = (input("Do you want another card? 'y'or'n': ")).lower()
    if another_card == 'y':
        new_card = random_card(1)
        player_hand += new_card
        player_total= hand_total(player_hand)
        print(hand_string(player_hand, player_total, "Your"))
       # addtnl_card(player_hand, player_total, "Your")
    
        if player_total == 21 and dealer_total >= 17:
          print(f"{hand_string(dealer_hand, dealer_total, 'Dealer')}")
          print("You Win!")
          hit_stand = False
    else: 
        hit_stand = False
 #Else if player hand is < 21 and they hold move on to dealer Hand
#else:
while dealer_total < 17 and player_total <= 21:
  new_card = random_card(1)
  dealer_hand += new_card
  dealer_total = hand_total(dealer_hand)
  print(hand_string(dealer_hand, dealer_total, "Dealer"))
  #addtnl_card(dealer_hand, dealer_total, "Dealer")

#player bust and dealer does not bust
if player_total > 21 and dealer_total <= 21:
    print (f"Bust! Dealer Wins with {hand_string(dealer_hand, dealer_total, 'Dealer')}")
elif player_total >21 and dealer_total > 21:
    print(f"Player and Dealer Both Bust, Dealer with {hand_string(dealer_hand, dealer_total, 'Dealer')} , Dealer Wins by Default")
#if player and dealer tie
elif dealer_total == player_total:
  print(f"You tied with your score of {player_total} and {hand_string(dealer_hand, dealer_total, 'Dealer')}")
 #if dealer hand > 21 # Dealer Busts  
elif dealer_total > 21:
  print(f"Dealer Busts with {hand_string(dealer_hand, dealer_total, 'Dealer')}. You Win!")
elif dealer_total > player_total:
  print(f"Dealer wins with {hand_string(dealer_hand, dealer_total, 'Dealer')}. You lose with your total of {player_total}.")
elif player_total > dealer_total and player_total < 21:
  print(f"You win with {player_total}. Dealer loses with {hand_string(dealer_hand, dealer_total, 'Dealer')}")

      
  
  #if !<17 and !>21 compare dealer hand value to player hand value, whomever has highest hand wins, if scores are == then tie
