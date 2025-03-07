import random

suits=['Hearts','Spades','Diamonds','Clubs']
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck=[f'{rank} of {suit}' for suit in suits for rank in ranks]


random.shuffle(deck)
player1=[deck.pop()for _ in range(5)]
player2=[deck.pop()for _ in range(5)]

print(f'Player 1 : {player1}')
print(f'Player 2 : {player2}')
    