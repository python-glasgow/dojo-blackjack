from cards import Deck

class Game(object):

    def setup(self, decks, games):

        ## Call shuffle
        deck = Deck().deck 

        for game in range(0, games):    

            # deal
            player_cards = []
            dealer_cards = []

            for card in range(0,2):
                player_cards.append(deck.pop())
                dealer_cards.append(deck.pop())

            # call player logic
            player_score = self.player_logic(player_cards, deck, dealer_cards[0])
            dealer_score = self.dealer_logic(dealer_cards, deck)

            for card in player_cards:
                print card

            for card in dealer_cards:
                print card

            print "Player score {0}".format(player_score)
            print "Dealer score {0}".format(dealer_score)

            if  player_score > 21:
                print "Dealer Wins :("
            else:                
                if  dealer_score > 21:
                    print "PLAYER WINS!! :D"
                else:
                    if player_score > dealer_score:
                        print "PLAYER WINS!! :D"
                    else:
                        print "Dealer Wins :("
            
            if game % 5 == 0:
                print "reshuffle!"
            # call shuffle

    def player_logic(self, player_cards, deck, dealer_card):

        max_score = self.calculate_max_score(player_cards)
        min_score = self.calculate_min_score(player_cards)

        twist = self.player_decision(min_score, max_score)

        while self.another_card(player_cards, dealer_card):

            # Add the next card
            player_cards.append(deck.pop())

            max_score = self.calculate_max_score(player_cards)
            min_score = self.calculate_min_score(player_cards)

            twist = self.player_decision(min_score, max_score)

        if max_score > 21:
            return min_score

        return max_score
            
    def dealer_logic(self, hand, deck):
        looping = True
        bust = False
        score = 0
        while looping:
            score = 0
            for card in hand:
                score += card['val']

            for card in hand:
                if card['val'] == 1:
                    if score  <= 11:
                        score += 10

            if score >= 17:
                looping = False
            else:
                hand.append(deck.pop())

        return score      

    def player_decision(self, min_score, max_score):

        if max_score < 17:
            return True    
        elif max_score > 21 and min_score < 17:
            return True

        return False

    def another_card(self, cards, dealer_card):
        score = self.calculate_max_score(cards)
        if score == 8:
            return True
        elif score == 9:
            return True
        elif score == 10:
            return True
        elif score == 11:
            return True
        elif score == 12:
            if dealer_card < 4:
                return True
            if dealer_card > 6:
                return True
            return False
        elif score == 13:
            if dealer_card < 2:
                return True
            if dealer_card > 6:
                return True
            return False
        elif score == 14:
            if dealer_card < 2:
                return True
            if dealer_card > 6:
                return True
            return False
        elif score == 15:
            if dealer_card < 2:
                return True
            if dealer_card > 6:
                return True
            return False
        elif score == 16:
            if dealer_card < 2:
                return True
            if dealer_card > 6:
                return True
            return False
        return False

    # Adds up the card values, assumes Ace is 1
    def calculate_min_score(self, cards):
        score = 0

        for card in cards:
            score = score + card["val"]

        return score

    # Adds up the card values, assumes Ace is 11
    def calculate_max_score(self, cards):
        score = 0

        for card in cards:
            score = score + card["val"]

            if card["val"] == 1:
                score = score + 10

        return score


if __name__ == "__main__":
    game = Game()
    game.setup(1, 5)
