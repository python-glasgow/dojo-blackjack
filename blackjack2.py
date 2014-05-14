# Group 1 - Dougal and Tom

from random import shuffle

cards = [(l, i + 1) for i in range(13) for l in ['a', 'b', 'c', 'd']]

shuffle(cards)


def hand_total(hand):
    return sum(card[1] for card in hand)

def loop(players):

    starting_players = players[:]

    while len(players) > 0:

        for player in players:

            print "\nPLAYER", player.__class__.__name__

            card = cards.pop(0)

            if hand_total(player.hand + [card, ]) > 21:
                print "bust", player.hand + [card, ]
                players.remove(player)
                player.hand.append(card)
                break

            response = player(card)

            if response == 1:
                print "hold"
                players.remove(player)
                break
            elif response == 2:
                print "hit"

    print '------'

    player_scores = [(hand_total(player.hand), player) for player in starting_players]

    sorted(player_scores)

    for score, player in player_scores:
        if hand_total(player.hand) > 21:
            print player.__class__.__name__, "bust with", score
            continue
        else:
            print player.__class__.__name__, "wins with", score
            break
    else:
        print "draw"


class Human(object):

    def __init__(self):
        self.hand = []

    def __call__(self, card):
        self.hand.append(card)
        print(self.hand)
        return int(raw_input("1. hold, 2. hit"))

class Bot(object):

    def __init__(self):
        self.hand = []

    def __call__(self, card):
        self.hand.append(card)
        current_total = hand_total(self.hand)
        aim = 21 - current_total
        held = [c for c in self.hand if c[1] < aim]
        chance = (((aim * 4.0) - len(held)) / (52 - len(self.hand))) * 100
        print "chance", chance
        if chance > 50:
            return 2
        return 1


if __name__ == "__main__":
    loop([Bot(), Human()])
