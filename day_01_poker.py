import random

class Card(object):

    def __init__(self, point, suit):
        self.point = point
        self.suit = suit


    def __str__(self):
        if self.point == 1:
            point_str = 'A'
        elif self.point == 11:
            point_str = 'J'
        elif self.point == 12:
            point_str = 'Q'
        elif self.point == 13:
            point_str = 'K'
        else:
            point_str = str(self.point)
        return '%s%s' % (self.suit, point_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """
    生成52张牌
    """
    def __init__(self):
        suits = ['♠️', '♥️', '♣️', '♦️']
        self.cards = [Card(point, suit) for suit in suits for point in range(1, 14)]
        self.current = 0

    def shuffle(self):
        '''洗牌-随机乱序'''
        self.current = 0
        random.shuffle(self.cards)

    @property
    def next(self):
        '发牌'
        card = self.cards[self.current]
        self.current += 1
        return card

    def has_next(self):
        return self.current < len(self.cards)


class Player(object):

    def __init__(self, name):
        self.name = name
        self.cards_on_hand = []

    def get(self, card):
        self.cards_on_hand.append(card)

    def arrange(self, car_key):
        self.cards_on_hand.sort(key=car_key)

# 排序规则-先根据花色再根据点数排行
def get_key(card):
    return (card.suit, card.point)

def main():
    p = Poker()
    # print(p.cards)
    p.shuffle()

    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

    for _ in range(13):
        for player in players:
            player.get(p.next)

    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)


if __name__ == '__main__':
    main()
