"""
Ask the user if they want "vegetarian" food. 
Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
"""

attendees = int(input("Enter number of attendees: "))
venue = "large hall"
facilities = "audio system" if attendees > 100 else "a projector" 
food = input("Are you a vagetarian? yes/no ") 
print(venue) if attendees > 100 else print("conference room")
print("We can use ", facilities) 
print("Veggie Delight Caterers as a vegetarian option" if food == "yes" else "Gourmet Meals Caterers for meat lovers")