"""
Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like 
"audio system" or "projector" based on the number of attendees.
"""

attendees = int(input("Enter number of attendees: "))
venue = "large hall"
facilities = "audio system" if attendees > 100 else "a projector" 
print(venue) if attendees > 100 else print("conference room")
print("We can use ", facilities) 
