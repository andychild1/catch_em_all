from random import randrange, choice

class Fish:
    def __init__(self):
        self.name = None
        self.size = None
        self.weight = 0
        self.value = 0
        self.bait = None

    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_weight(self):
        return self.weight
    def get_value(self):
        return self.value

    def set_name(self, bait):
        if bait == "a":
            self.name = choice(["CARP", "ROACH", "TENCH", "BLUEGILL", "BASS", "EAL"])
        elif bait == "b":
            self.name = choice(["ROACH", "BLUEGILL", "IDLE"])
        elif bait == "c":
            self.name = choice(["CARP", "GOLDEN CARP", "CATFISH"])
        elif bait == "d":
            self.name = choice(["CARP", "GOLDEN CARP", "GRASS CARP"])
        elif bait == "e":
            self.name = choice(["ROACH", "GOLDEN CARP", "BLUEGILL"])
        elif bait == "f":
            self.name = choice(["BASS", "PIKE", "CATFISH"])
        else:
            return "Something's wrong"
        

    def set_size_and_weight(self):
        name = self.get_name()
        if name == "CARP":
            self.size = randrange(20, 150)
            self.weight = randrange(1, 35)
        elif name == "PIKE":
            self.size = randrange(30, 156)
            self.weight = randrange(1, 16)
        elif name == "BASS":
            self.size = randrange(12, 40)
            self.weight = randrange(1, 8)
        elif name == "ROACH" or name == "BLUEGILL" or name == "GOLDEN CARP":
            self.size = randrange(5, 20)
            self.weight = randrange(1, 2)
        elif name == "GRASS CARP":
            self.size = randrange(30, 180)
            self.weight = randrange(1, 36)
        elif name == "EAL":
            self.size = randrange(10, 120)
            self.weight = randrange(1, 4)
        elif name == "CATFISH":
            self.size = randrange(30, 140)
            self.weight = randrange(2, 48)
        elif name == "TENCH" or name == "IDLE":
            self.size = randrange(15, 40)
            self.weight = randrange(1, 8)
        else:
            return "No fish matching this name"
        
    def set_value(self, weight):
        if weight <= 5:
            self.value = 3
        elif weight >= 6 and weight <= 10:
            self.value = 6
        elif weight >= 11 and weight <= 15:
            self.value = 10
        elif weight >= 16 and weight <= 20:
            self.value = 14
        elif weight >= 21 and weight <= 25:
            self.value = 18
        else:
            self.value = 25
