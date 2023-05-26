print("Welcome to movie recommendations!")
start = input("Would you like to begin?\n")
if start == "yes":
    flag = True
if start == "no":
    print("Goodbye")
    exit()

movie_choices = {
    "comedy": ["Just go with it", "Shotgun wedding", "Year one", "You again"],
    "action": ["Inception", "Sand castle", "Gladiator", "Troy"],
    "documentaries": ["Explained", "Grizzly man", "Mankind: The story of all of us"]
}

comedy_index = 0
action_index = 0
documentaries_index = 0

while flag:
    movie_type = input("Do you prefer comedy, action, or documentaries?\n")
    if movie_type == "comedy":
        specific_movie = movie_choices[movie_type][comedy_index]
        comedy_index += 1
        print(f"Your recommendation is '{specific_movie}'")

    elif movie_type == "action":
        specific_movie = movie_choices[movie_type][action_index]
        action_index += 1
        print(f"Your recommendation is '{specific_movie}'")

    elif movie_type == "documentaries":
        specific_movie = movie_choices[movie_type][documentaries_index]
        documentaries_index += 1
        print(f"Your recommendation is '{specific_movie}'")


    keep_going = input("Keep going? Yes or no\n")
    if keep_going == "no":
        print("Hope you enjoyed! Goodbye")
        flag = False



#I should go back and turn the repeat code into a function
#code will break once index has been used enough to be out of range