#Task1:

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


#Task2:



if attendees > 100:
    print("An audio system and projector will be required")
else:
    print("No need for any audio system or projector")

#Task3:

food = input("Vegetarian? (yes/no)")

if food == "yes":
    print("We recommend Veggie Delight Caterers")
else:
    print("We recommend Gourmet Meals Caterers")

