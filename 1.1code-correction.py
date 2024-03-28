place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else:
    print("You find a hidden treasure!")