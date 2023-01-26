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

#Selects a random card from deck
def random_card(num_cards):
    '''Takes player or dealer hand to add card to and # of cards to add'''
    new_cards = random.sample(inf_deck, num_cards)
    return new_cards

#Sums value of cards in hand
def hand_total(hand, plr_bool):
    '''Takes dealer or player hand, sums cards and handles question if player (True state) receives Ace whether it is a 1 or 11'''
    total = 0
    for card in hand: 
        if card[1] < 11:
            total += card[1]
        else:
          #If player deck bool will be True
          if plr_bool:
            change_value = int(input("Would you like the Ace to be valued as 11 or 1?: "))
            if change_value == 1:
               total += 1
            else: 
               total += card[1]
          #Handles dealer hand Aces with 11 if other card <=10
          elif total <= 10:
            total += card[1]
          else:
            total += 1
    return total

#populate player's initial hand
player_hand = random_card(2)

#populate dealer's initial hand
dealer_hand = random_card(2)
dealer_total = hand_total(dealer_hand, False)

#How to pull values out of tuple list for each hand  

first_dlr_card = (dealer_hand[0])[0]

def check_ace (card):
  if card.count(11) > 0:
    change_value = int(input("Would you like the Ace to be valued as 11 or 1?: "))
    return change_value
  else:
    return (card[0])[1]
      
def hand_string(hand, subject):
  '''Creates a string to describe player hand depending on current cards in hand'''
  part_1 = f"{subject} hand: "
  card_string = ""
  just_cards = []
  for card in hand:
      just_cards.append(card[0])
  card_string = " and ".join(just_cards)        
  return part_1 + card_string

print(hand_string(player_hand, "Your"))  

player_total = hand_total(player_hand, True)

def hand_total_string(hand_total, subject):
  return (f"{subject} hand total is {hand_total}")

#prints initial player hand total
print(hand_total_string(player_total, "Your"))

print(f"Dealer's first card is {first_dlr_card}")

def dealer_string(hand, total):
  dealer_hand_string = hand_string(hand,'Dealer')
  dealer_hand_total = hand_total_string(total, "Dealer's")
  return f"{dealer_hand_string} {dealer_hand_total}" 

#Black Jack Game Logic

#1 Is player initial hand == 21 (BlackJack)
  #If yes then check if dealer's initial hand equals 21
  #Tie 
if player_total == 21 & dealer_total == 21:
    print(dealer_string(dealer_hand, dealer_total))
    print("It's a Tie!")

#elif player hand == 21 and dealer hand !21 Player Wins
elif player_total == 21:
    print(dealer_string(dealer_hand, dealer_total))
    print("You Win!")

#elif player hand is < 21 ask player if they want another card (if yes add this card to total)  
hit_stand = True
while hit_stand:
  if player_total < 21:
    another_card = (input("Do you want another card? 'y'or'n': ")).lower()
    if another_card == 'y':
        new_card = random_card(1)
        player_hand += new_card
        player_total += check_ace(new_card)
        print(hand_string(player_hand, "Your"))
        print(hand_total_string(player_total, "Your"))
        if player_total < 21:
          hit_stand = True
        else:
          hit_stand = False
    elif player_total == 21 and dealer_total >= 17:
        print(dealer_string(dealer_hand, dealer_total))
        print("You Win!")
        hit_stand = False
    elif player_total > 21 and dealer_total >= 17:
        print(hand_string(player_hand, "Your"))
        print(hand_total_string(player_total, "Your"))
        print(dealer_string(dealer_hand, dealer_total))
        print("You Bust, Dealer Wins!")
    else: 
        hit_stand = False

#next player hand is < 21 & they hold move on to dealer hand
#dealer hand must be at least 17 if not cards are drawn until at least 17 is reached      
while dealer_total < 17:
  new_card = random_card(1)
  dealer_hand += new_card
  dealer_total = hand_total(dealer_hand, False)

print(dealer_string(dealer_hand, dealer_total))

#player bust and dealer does not bust
if player_total > 21 and dealer_total <= 21:
    print (f"Bust! Dealer Wins with {dealer_string(dealer_hand, dealer_total)}")

#dealer and player bust, dealer default wins
elif player_total >21 and dealer_total > 21:
    print(f"Player and Dealer Both Bust, Dealer with {dealer_string(dealer_hand, dealer_total)}, Dealer Wins by Default")

#player and dealer tie
elif dealer_total == player_total:
  print(f"You tied with your score of {player_total} and {dealer_string(dealer_hand, dealer_total)}")

#Dealer Busts  
elif dealer_total > 21:
  print(f"Dealer Busts with {dealer_string(dealer_hand, dealer_total)}. You Win!")

#Dealer total higher than player's, dealer win
elif dealer_total > player_total:
  print(f"Dealer wins with {dealer_string(dealer_hand, dealer_total)}. You lose with your total of {player_total}.")

#Player total higher than dealer, player wins
elif player_total > dealer_total and player_total < 21:
  print(f"You win with {player_total}. Dealer loses with {dealer_string(dealer_hand, dealer_total)}")

