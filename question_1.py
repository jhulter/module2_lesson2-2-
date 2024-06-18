#Task1:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

else:
    pass

# Task 2

if place == "cave":
    light = input("Do you want a torch or proceed in the dark? (torch/dark)")
    if light == "torch":
        print("You can see drawings left by neanderthals")
    elif light == "dark":
        print("After a few steps with no light you just fell down a huge hole and broke both your legs and will probably die now...")

# Task 3
    else:
        pass
else:
    pass

