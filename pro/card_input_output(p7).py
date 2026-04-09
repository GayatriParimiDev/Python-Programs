# This program is executed to find the lucky cards.

card = input("Enter a card (e.g., 'Ace of Spades'): ")

lucky_cards = {"Ace of Hearts", "Seven of Diamonds", "King of Clubs"}

if card in lucky_cards:
    print("Lucky! Congratulations!")
else:
    print("Better luck next time!")