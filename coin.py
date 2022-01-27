import random

play = True
totalScore = 0

coin1Turns = ''
coin2Turns = ''

coinFlips = 0

while play:
  coin1 = random.randint(0,1)
  coin2 = random.randint(0,1)
  if coin1 == 0:
    print("Coin 1 is heads")
    coin1Turns += "H"
  else:
    print("Coin 1 is tails")
    coin1Turns += "T"
  if coin2 == 0:
    print("Coin 2 is heads")
    coin2Turns += "H"
  else:
    print("Coin 2 is tails")
    coin2Turns += "T"
  coinFlips += 1

  if 'HHH' in coin1Turns and 'HHH' not in coin2Turns:
    play = False
    print("Coin 1 wins!")
    print("Total number of flips: {}".format(coinFlips))
  
  if 'HHH' in coin2Turns and 'HHH' not in coin1Turns:
    play = False
    print("Coin 2 wins!")
    print("Total number of flips: {}".format(coinFlips))
  
  if 'HHH' in coin2Turns and 'HHH' in coin1Turns:
    play = False
    print("There is a tie!")
