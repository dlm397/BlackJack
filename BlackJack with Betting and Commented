import random
import time



again = True # Defines Boolean used for game repetition
a = 0        # Choice int used to make decisive actions
wallet = 100 # Defines wallet and give player 100 to start with

while again == True:

  # Checks for bankruptcy and asks for magic word for additional 100
  if wallet == 0:
    word = str(input("you're bankrupt :( say the magic word to recieve new funds!"))
    if word == "please":
      print("That's the special word! Here's 100 more dollars")
      wallet = 100
    else:
      print("That's not it D: better luck next time.")
      break
  
  # Tells you how much is in your wallet before beginning this round of play
  print("You have ", wallet," in you wallet.")
  # Asks you to place your bet
  bet = int(input("How much would you like to bet?"))

  # Checks to insure your bet is within your budget restraint
  while bet > wallet:
    print("You do not have enough money")
    bet = int(input("Your bet must be less than your wallet. You have ", wallet," in your wallet. How much would you like to bet?"))

 # Establishes players hand
  player_hand = random.randint(1,10) + random.randint(1,10);
  dealer_hand = random.randint(1,10) + random.randint(1,10);

  # Tells players what is in their hand
  print("The Dealer has ", dealer_hand ," in hand")
  print("You have ", player_hand ," in hand")

  # Asks players to decide wheither to hit or stand, using int a as an input
  while a != 2:
    a = int(input("Would you like to hit(1), or stand(2)?"))
    if a != 1 and a != 2 and a != 3:
        print("Invalid input")
    elif a == 1:
        player_hand += random.randint(1,10)
        print("You now have ", player_hand ," in hand")
    elif a == 2:
      pass
    if player_hand > 21:
      print("You lose")
      a = 2
      wallet = wallet - bet

  #Plays the dealer's turn, hitting below 17, standing above
  if player_hand < 22:
    print("It's now the dealer's turn.")
    print("The dealer has ",dealer_hand," in hand")
    while dealer_hand < 17:
      dealer_hand += random.randint(1,10)
      print("The dealer hits, now they have ",dealer_hand," in hand")
      time.sleep(2)
      if dealer_hand < 17:
        print("The Dealer hits again")
      else:
        print("The Dealer stands")

    # Determines win or loss, pays bet
    if dealer_hand < player_hand or dealer_hand >= 22:
      print("You win")
      wallet = wallet + bet * 2
    elif dealer_hand >= player_hand:
      print("You lose")
      wallet = wallet - bet
      bet = 0

  a = 0

  # Asks player if they would like to play again
  again = bool(input("Would you like to continue playing, yes (True) or no (False)"))
