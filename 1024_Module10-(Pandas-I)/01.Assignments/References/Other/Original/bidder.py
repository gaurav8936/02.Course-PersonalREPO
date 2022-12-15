import random

class Bidder:
    class_counter = 0
    def __init__(self, num_users, num_rounds):
        self.users = num_users
        self.rounds = num_rounds
        self.balance = 0
        Bidder.class_counter += 1
        self.class_counter = Bidder.class_counter

    def __repr__(self):
        rep = f'Bidder(ID:{self.class_counter},Users:{self.users},Rounds:{self.rounds},Balance:{self.balance})'
        return rep

    def __str__(self):
        return self.__repr__()

    def bid(self, user_id):
        return random.randint(0,100000)

    def notify(self, auction_winner, price, clicked):
        if auction_winner and clicked:
            self.balance += 1
        if auction_winner:
            self.balance -= price