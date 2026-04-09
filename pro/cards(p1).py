#This is a program from finding the probabilty of being neither king nor a spade.

card = 52
kings = 4
spades = 13
spades_kings = 1

non_spade_non_king = card - (kings + spades - spades_kings)
prob = non_spade_non_king / card
print("The Probability is : %f" %prob)