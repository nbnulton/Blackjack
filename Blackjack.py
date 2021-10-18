

#dealer shuffles deck
#dealer deals two cards to self (one card is visible)
#   if card value count < 17
#       hit
#   else:
#       stand
#dealer deals two cards to player (both cards are visible)
#   if card value = 21
#       blackjack
#       player wins
#   else:
#       show card value count
#player chooses: hit or stand
#hit
#   dealer gives card to player
#   update card value count
#   if card value count > 21
#       bust, dealer wins
#       play again?
#   else:
#       hit or stand


#aces
#   if card value count < 21
#       ace == 1 or ace == 11
#       if card value count >= 20
#           ace == 1
#       else
#           ace == 11


import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

card_01 = Card("A-Di", 1 or 11)
card_02 = Card("2-Di", 2)
card_03 = Card("3-Di", 3)
card_04 = Card("4-Di", 4)
card_05 = Card("5-Di", 5)
card_06 = Card("6-Di", 6)
card_07 = Card("7-Di", 7)
card_08 = Card("8-Di", 8)
card_09 = Card("9-Di", 9)
card_10 = Card("10-Di", 10)
card_11 = Card("J-Di", 11)
card_12 = Card("Q-Di", 12)
card_13 = Card("K-Di", 13)

card_14 = Card("A-He", 1 or 11)
card_15 = Card("2-He", 2)
card_16 = Card("3-He", 3)
card_17 = Card("4-He", 4)
card_18 = Card("5-He", 5)
card_19 = Card("6-He", 6)
card_20 = Card("7-He", 7)
card_21 = Card("8-He", 8)
card_22 = Card("9-He", 9)
card_23 = Card("10-He", 10)
card_24 = Card("J-He", 11)
card_25 = Card("Q-He", 12)
card_26 = Card("K-He", 13)

card_27 = Card("A-Sp", 1 or 11)
card_28 = Card("2-Sp", 2)
card_29 = Card("3-Sp", 3)
card_30 = Card("4-Sp", 4)
card_31 = Card("5-Sp", 5)
card_32 = Card("6-Sp", 6)
card_33 = Card("7-Sp", 7)
card_34 = Card("8-Sp", 8)
card_35 = Card("9-Sp", 9)
card_36 = Card("10-Sp", 10)
card_37 = Card("J-Sp", 11)
card_38 = Card("Q-Sp", 12)
card_39 = Card("K-Sp", 13)

card_40 = Card("A-Cl", 1 or 11)
card_41 = Card("2-Cl", 2)
card_42 = Card("3-Cl", 3)
card_43 = Card("4-Cl", 4)
card_44 = Card("5-Cl", 5)
card_45 = Card("6-Cl", 6)
card_46 = Card("7-Cl", 7)
card_47 = Card("8-Cl", 8)
card_48 = Card("9-Cl", 9)
card_49 = Card("10-Cl", 10)
card_50 = Card("J-Cl", 11)
card_51 = Card("Q-Cl", 12)
card_52 = Card("K-Cl", 13)

print(card_01.suit, card_01.value)


class Table():

    def __init__(self, draw_pile, dealer_hand, player_hand):
        self.draw_pile = [card_01, card_02, card_03, card_04, card_05, card_06, card_07, card_08, card_09, card_10, card_11, card_12, card_13, card_14, card_15, card_16, card_17,
        card_18, card_19, card_20, card_21, card_22, card_23, card_24, card_25, card_26, card_27, card_28, card_29, card_30, card_31, card_32, card_33, card_34, card_35, card_36,
        card_37, card_38, card_39, card_40, card_41, card_42, card_43, card_44, card_45, card_46, card_47, card_48, card_49, card_50, card_51, card_52]
        self.player_hand = {}
        self.dealer_hand = {}


    def shuffle_cards(self, draw_pile):
        #shuffle cards
        pass


    def deal_player_cards(self, draw_pile, player_hand):
        #deal card to player
        pass

    def deal_dealer_cards(self, draw_pile, dealer_hand):
        #deal card to dealer
        pass

    def show_both_player_cards(self, player_hand):
        #show player cards
        pass

    def show_one_dealer_card(self, dealer_hand):
        #show only one of dealer's cards
        pass

    def count_dealer_cards(self, dealer_hand):
        #count dealer's cards
        #must hit 17
        pass

    def count_player_hand(self, player_hand):
        #count player's cards
        pass

    def compare_hands(self, player_hand, dealer_hand):
        #compare player's and dealers cards
        pass


class UI():
    pass




    










    

