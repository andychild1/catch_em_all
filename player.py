class Player:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.fish = []
        self.tot_weight = 0

    def get_credits(self):
        return self.credits

    def buy_baits(self, bait):
        self.credits -= bait.cost

    def earn_from_fish(self, fish):
        self.credits += fish.value