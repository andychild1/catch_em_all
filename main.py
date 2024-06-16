import time
from fish import Fish
from weather import Weather
from player import Player
from bait import Bait
from max_heap import MaxHeap
import json

# Initialize baits
bait_dicts = [{"id": "a", "name": "worms", "cost": 5}, {"id": "b", "name": "larvas", "cost": 5}, {"id": "c", "name": "cheese", "cost": 8}, {"id": "d", "name": "sweetcorn", "cost": 10}, {"id": "e", "name": "bread", "cost": 5}, {"id": "f", "name": "live bait", "cost": 15}]
bait_list = [Bait(b["id"], b["name"], b["cost"]) for b in bait_dicts]

# Main functions

def start_game():
        print(r'''

    ___      _       _                              _ _ 
   / __\__ _| |_ ___| |__     ___ _ __ ___     __ _| | |
  / /  / _` | __/ __| '_ \   / _ \ '_ ` _ \   / _` | | |
 / /__| (_| | || (__| | | | |  __/ | | | | | | (_| | | |
 \____/\__,_|\__\___|_| |_|  \___|_| |_| |_|  \__,_|_|_|
                                                       
           .----         -                                    
      .-*'`    `*-.._.-''/
     ()  ) * )  ,       (  
      `*-._`._(__.--*"`.\
                       
''')
        print("\nWelcome to Catch em all!\n")
        weather = Weather()
        print(weather.sky_conditions())


def fishing(player):
    fish = Fish()
    choose_bait(fish, player)
    action = input("Enter C to cast..\n").upper()
    while action != "C":
        action = input("Please enter C or c to cast...\n").upper()
    if action == "C":
        fish.set_value(fish.get_weight())
        print("***************************************************************\n")
        print(f"You caught a {fish.get_name()} with a size of {fish.get_size()} cm and a weight of {fish.get_weight()} kg.\n")
        print("***************************************************************\n")
        print(f"You earned {fish.get_value()}$\n")
        player.earn_from_fish(fish)
        player.fish.append({"name": fish.get_name(), "weight": fish.get_weight()})
        player.tot_weight += fish.get_weight()
        print(f"Credits: {player.get_credits()}\n")
        fish_again(player)



def choose_bait(fish, player):
    print("These are the baits available:\n")
    for b in bait_list:
        print(b.display_baits())
    bait_choice = input("Choose a bait:\n")
    if bait_choice not in ["a", "b", "c", "d", "e", "f"]:
        print("Enter a valid choice...\n")
        choose_bait(fish, player)
    else:
        if bait_choice == "a":
            fish.set_name(bait_choice)
            fish.set_size_and_weight()
            bait_list[0].count -= 1
            bait_left = bait_list[0].check_bait_count()
            if bait_list[0].count < 0:
                qty = 0
            else:
                qty = bait_list[0].count
            print(f"Bait: {bait_list[0].get_name()}, Qty: {qty}")
            if bait_left < 0:
                buy_or_change_bait(bait_list[0], player, fish)
        elif bait_choice == "b":
            fish.set_name(bait_choice)
            fish.set_size_and_weight()
            bait_list[1].count -= 1
            bait_left = bait_list[1].check_bait_count()
            if bait_list[1].count < 0:
                qty = 0
            else:
                qty = bait_list[1].count
            print(f"Bait: {bait_list[1].get_name()}, Qty: {qty}")
            if bait_left < 0:
                buy_or_change_bait(bait_list[1], player, fish)
        elif bait_choice == "c":
            fish.set_name(bait_choice)
            fish.set_size_and_weight()
            bait_list[2].count -= 1
            bait_left = bait_list[2].check_bait_count()
            if bait_list[2].count < 0:
                qty = 0
            else:
                qty = bait_list[2].count
            print(f"Bait: {bait_list[2].get_name()}, Qty: {qty}")
            if bait_left < 0:
                buy_or_change_bait(bait_list[2], player, fish)
        elif bait_choice == "d":
            fish.set_name(bait_choice)
            fish.set_size_and_weight()
            bait_list[3].count -= 1
            bait_left = bait_list[3].check_bait_count()
            if bait_list[3].count < 0:
                qty = 0
            else:
                qty = bait_list[3].count
            print(f"Bait: {bait_list[3].get_name()}, Qty: {qty}")
            if bait_left < 0:
                buy_or_change_bait(bait_list[2], player, fish)
        elif bait_choice == "e":
            fish.set_name(bait_choice)
            fish.set_size_and_weight()
            bait_list[4].count -= 1
            bait_left = bait_list[4].check_bait_count()
            if bait_list[4].count < 0:
                qty = 0
            else:
                qty = bait_list[4].count
            print(f"Bait: {bait_list[4].get_name()}, Qty: {qty}")
            if bait_left < 0:
                buy_or_change_bait(bait_list[4], player, fish)
        elif bait_choice == "f":
            fish.set_name(bait_choice)
            fish.set_size_and_weight()
            bait_list[5].count -= 1
            bait_left = bait_list[5].check_bait_count()
            if bait_list[5].count < 0:
                qty = 0
            else:
                qty = bait_list[5].count
            print(f"Bait: {bait_list[5].get_name()}, Qty: {qty}")
            if bait_left < 0:
                buy_or_change_bait(bait_list[5], player, fish)
        else:
            print("No bait available")

def buy_or_change_bait(bait, player, fish):
    choice = input("Do you wish to buy some baits or change bait?\n buy/change\n")
    if choice == "buy":
        buy_baits(bait, player)
    elif choice == "change":
        choose_bait(fish, player)
    else:
        print("Please enter 'buy' or 'change'...\n")
        buy_or_change_bait(bait, player, fish)

def buy_baits(bait, player):
    print(f"Buying some {bait.get_name()}\n")
    player.credits -= bait.cost
    bait.count = 10
    print(f"You added {bait.count} {bait.get_name()}, your credits left are: {player.credits}")

def fish_again(player):
    choice = input("Do you wish to cast again?\n y/n\n")
    while choice not in ["y", "n", "c"]:
        choice = input("Please enter: y/n\n")
    if choice == "y":
        fishing(player)
    else:
        print("Your catches are: \n")
        for fish in player.fish:
            print(fish["name"], fish["weight"], "kg\n")
        print(f"Total fish weight: {player.tot_weight} kg\n")
        print(f"Total credits: {player.get_credits()}$\n")
        set_scores(player)
        print("\nTOP SCORES\n")
        read_scores()
        print("\n\n\nThank you for playing with Catch em All!\n")

def check_high_score():
    max_heap = MaxHeap()
    scores = open("top_scores.json")
    data = json.load(scores)
    if data["players"] == []:
        max_heap.add(0)
    for score in data["players"]:
        max_heap.add(score["scores"])
    return max_heap.heap_list[1]


def set_scores(player):
    if player.tot_weight > check_high_score():
        scores = {"player": player.name, "scores": player.tot_weight}
        with open("top_scores.json", "r+") as score:
            data = json.load(score)
            data["players"].append(scores)
            score.seek(0)
            json.dump(data, score, indent = 4)
    
    
def read_scores():
    scores = open("top_scores.json")
    data = json.load(scores)
    for score in reversed(data["players"]):
        print("Player: {0}, Scores: {1}kg".format(score["player"], score["scores"]))
        




def main():
    start_game()
    player_name = input("Enter your name: \n")
    if player_name == '':
        player_name = "player1"
    player = Player(player_name, 10)
    print(f"Welcome to Catch em All {player_name}!\n")
    fishing(player)
    



if __name__ == "__main__":
    main()