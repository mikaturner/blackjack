import art
import random
import replit

############### Blackjack Project 
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#(I'm ignoring the above list of cards and creating a tuple list with cards and values because it's prettier :-))

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

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

continue_playing = True

#Selects a random card from deck
def random_card(num_cards):
    '''Takes player_hand or dealer_hand, and # of cards to add'''
    new_cards = random.sample(inf_deck, num_cards)
    return new_cards

#Sums value of cards in hand
def hand_total(hand):
    '''Takes dealer or player hand, sums cards and handles Ace whether it is a 1 or 11'''
    total = 0
    ace_count = 0
    
    for card in hand:
      total += card[1] 
      if card[1] == 11:
        ace_count += 1
    if total > 21 and ace_count > 0:
      total -= (ace_count-1) * 10
      if total > 21:
        total -= 10
    return total
  
####Black Jack Game########
def blackJackGame ():
  player_hand = []
  player_total = 0

  dealer_hand = []
  dealer_total= 0
  hit_stay = True
  print(art.logo) 
  
  #populate player's initial hand
  player_hand = random_card(2)
  
  #populate dealer's initial hand
  dealer_hand = random_card(2)
  dealer_total = hand_total(dealer_hand)  
  first_dlr_card = (dealer_hand[0])[0]

  def hand_string(hand, subject):
    '''Creates a string to describe dealer or player hand depending on current cards in hand'''
    part_1 = f"{subject} hand: "
    card_string = ""
    just_cards = []
    for card in hand:
        just_cards.append(card[0])
    card_string = " and ".join(just_cards)        
    return part_1 + card_string

  def hand_total_string(hand_total, subject):
    '''Creates a string to display dealer or player hand total'''
    return (f"{subject} total is {hand_total}")  

  #Creates string to display dealer hand and total
  def hnd_str(hand, subject, total):
    hnd_str = hand_string(hand, subject)
    hnd_tl = hand_total_string(total, subject)
    return f"{hnd_str}\n{hnd_tl}"  

  #calculates and prints initial player hand total
  player_total = hand_total(player_hand)
  
  #Display player hand and total
  plr_hnd_str = hnd_str(player_hand, "Your", player_total)
  print(plr_hnd_str)

  #Display dealer's first card
  print(f"Dealer's first card is {first_dlr_card}")

  ######Black Jack Game Logic###########
    
  #If Black Jack is True
  if player_total == 21 or dealer_total == 21:   
    if player_total == dealer_total:
      print("It's a Tie!")
    #handles dealer or player Black Jack
    else: 
      bj_msg = "Black Jack! You Win!" if player_hand == 21 else "Dealer Wins with Black Jack!"
      print(bj_msg)
    print(hnd_str(dealer_hand, "Dealer", dealer_total))
  
  #If Black Jack not True
  else:    
  #2 Check if dealer hand is at least 17 if not cards are drawn until at least 17 is reached      
    while dealer_total < 17:
      new_card = random_card(1)
      dealer_hand += new_card
      dealer_total = hand_total(dealer_hand)
    
  #3 elif player hand is < 21 ask player if they want to stay or hit (if yes add this card to total)  
    while hit_stay:
      if player_total < 21:
        another_card = (input("Do you want to hit? 'y'or'n': ")).lower()
        if another_card == 'y':
          new_card = random_card(1)
          player_hand += new_card
          player_total = hand_total(player_hand)
          print(hnd_str(player_hand, "Your", player_total))
          
          if player_total >= 21:
            hit_stay = False
          elif player_total == 21:
            print("You Win!")
            print(hnd_str(dealer_hand, "dealer", dealer_total))
            hit_stay = False  
        else: 
          hit_stay = False

    #dealer hand should be static at this point
    dlr_string = hnd_str(dealer_hand, 'Dealer', dealer_total)
    
    #### Busts##########      
    if player_total > 21 or dealer_total > 21:
      #4 dealer & player bust (both totals > 21), dealer default wins
      if player_total >21 and dealer_total > 21:
        print(f"Player and Dealer Both Bust. Dealer Wins by default with {dlr_string}")
      
      #5 only player busts  
      else:
        bust_message = f"Bust! Dealer Wins with {dlr_string}" if player_total > 21 else f"You win with {player_total}! Dealer Busts with {dlr_string}" 
        print(bust_message)
    
    ######Player or Dealer Non-Black Jack Wins and Tie #####    
    else:    
      #player and dealer tie
      if dealer_total == player_total:
        print(f"You tied with your score of {player_total} and {dlr_string}")

      #Player or Dealer Hand Higher
      else:
        winner_msg = f"You win with {player_total}. Dealer loses with {dlr_string}" if player_total > dealer_total else f"Dealer wins with {dlr_string}. You lose with your total of {player_total}."
        print(winner_msg)

while continue_playing:
  blackJackGame()
  keep_playing = input("Do you want to keep playing? y or n:")
  if keep_playing == "n":
    continue_playing = False
  else: 
    replit.clear()



