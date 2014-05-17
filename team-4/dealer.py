def dealer_logic(hand, deck):
	looping = False
	bust = False
	while looping:
		score = 0
		for card in hand:
			score += card['val']

		for card in hand:
			if card['val'] == 1:
				if score + 10 <= 21:
					score += 10

		if score >= 17:
			looping = False
		else:
			hand.append(deck.pop())

	return score


def another_card(self, cards, dealer_card):
	score = calculate_max_score(cards)
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




8			Double on 5 to 6. Otherwise hit.
9			Double on 2 to 6. Otherwise hit.
10			Double on 2 to 9. Otherwise hit.
11			Always double.
12			Stand on 4 to 6. Otherwise hit.
13 to 16		Stand on 2 to 6. Otherwise hit.
17 to 21		Always stand.
A,2 to A,5		Double on 4 to 6. Otherwise hit.
A,6                     Double on 2 to 6. Otherwise hit.
A,7                     Double on 3 to 6. Stand on 2,7,8 or A.
                        Hit on 9 or 10.
A,8                     Double on 6. Otherwise stand.
A,9                     Always stand.
A,A            	        Always split.
2,2                     Split on 3 to 7. Otherwise hit.
3,3                     Split on 4 to 7. Otherwise hit.
4,4                     Same as 8 above.
5,5                     Same as 10 above.
6,6                     Split on 2 to 6. Otherwise hit.
7,7                     Split on 2 to 7. Stand on 10. Otherwise hit.
8,8                     Always split.
9,9                     Split on 2 to 9 except 7. Stand on 7,10 or A.
10,10			Always stand.


