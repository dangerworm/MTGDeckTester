from mtgsdk import Card
from mtgsdk import Set

set_name = 'M20'

m20_set = Set.find(set_name).all()
m20_cards = Card.where(set=set_name).all()

for card in m20_cards:
    print(card.name)


