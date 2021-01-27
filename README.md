# Blackjack
An introduction to python to make a blackjack game with the dealer taking a stand at a soft 17. After you quit, there is a summary of how many games were won.

|Command option|Description|
|---|---|
|-d/--decks|number of decks to use (max of 8)|

## How To Play
You play against the dealer. The deck(s) are shuffled and a card is dealt to each player. The first card of each hand is revealed. Each card has a face value. Jacks, Queens, and Kings all have a value of 10. Aces can have a value of 1 or 11. The rest of the cards have the same value as shown on the card. You enter 'h' for "hit" to draw additional cards and 's' for "stay" to stop.  

## How To Win
The total count of your hand should be as close to 21 as possible without going over and should be higher than the total of the dealer's hand. In case of a tie, it's called a "push".

## Run locally
```
python3 game.py
```

Run with multiple decks
```
python3 game.py -d 4
python3 game.py --decks 4
```
  