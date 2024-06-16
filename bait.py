class Bait:
    def __init__(self, id, name, cost):
        self.id = id
        self.name = name
        self.cost = cost
        self.count = 10

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id

    def display_baits(self):
        name = self.get_name()
        id = self.get_id()
        string = id + "-" + name + "\n"
        return string
    
    def check_bait_count(self):
        if self.count < 0:
            print(f"No more {self.get_name()} left...buy some baits or change bait.")
        return self.count