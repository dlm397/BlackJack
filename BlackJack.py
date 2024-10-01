import random
import time

again = 1
a = 0

while again == 1:


  player_hand = random.randint(1,10) + random.randint(1,10);
  dealer_hand = random.randint(1,10) + random.randint(1,10);

  print("The Dealer has ", dealer_hand ," in hand")
  print("You have ", player_hand ," in hand")

  while a != 2:
    a = int(input("Would you like to hit(1), stand(2), or raise(3)?"))
    if a != 1 and a != 2 and a != 3:
        print("Invalid input")
    elif a == 1:
        player_hand += random.randint(1,10)
        print("You now have ", player_hand ," in hand")
    elif a == 2:
      pass
    elif a == 3:
      print("Sorry, this operation is not implemented yet")
    if player_hand > 21:
      print("You lose")
      a = 2
    elif player_hand == 21:
      print("You win")
      a = 2
  print("It's now the dealer turn.")
  print("The dealer has ",dealer_hand," in hand")
  while dealer_hand < 17:
    dealer_hand += random.randint(1,10)
    print("The dealer hits, now they have ",dealer_hand," in hand")
    time.sleep(2)
    if dealer_hand < 17:
      print("The Dealer hits again")
    else:
      print("The Dealer stands")

  if dealer_hand < player_hand or dealer_hand == 22:
    print("You win")
  elif dealer_hand >= player_hand:
    print("You lose")

  a = 0

  again = int(input("Would you like to continue playing, yes (1) or no (2)"))
