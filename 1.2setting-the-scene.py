"""
Based on the corrected code from Task 1, expand the game. 
If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
"""

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else:
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Some light might keep some animals away.")
    else:
        print("You can find beauty in the dark, let the moonlight guide you")
    