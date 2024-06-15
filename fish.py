from random import randrange, choice

class Fish:
    def __init__(self):
        self.name = None
        self.size = None
        self.weight = 0
        self.value = 0
        self.bait = None

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

