import blackjack

g = sorted(globals())

for x in g:
    print(x)

#print(__name__)

#blackjack.deal_card(blackjack.dealer_card_frame)
blackjack.play()
#print(blackjack.cards)

personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details
print(name, country)
print(_)