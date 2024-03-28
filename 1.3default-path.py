"""
If the user makes an invalid choice at any point, use the pass statement for now. 
Later, you can enhance this to provide feedback or a different branch of the story.
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
       pass
    else:
        print("You can find beauty in the dark, let the moonlight guide you")