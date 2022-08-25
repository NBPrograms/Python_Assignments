#Nicholas Boes - HW 6.1

def open_actor_file():
    #Opens file
    #Makes sure it is there
    #Puts the file into an array 
    fn = "actors.txt"
    try:
        in_file = open(fn, "r")
    except FileNotFoundError:
        print(f"Check the file: {fn} and try again")
        exit(1)
    noms = in_file.readlines()
    noms.remove(noms[0])
    return noms

def get_actor_input():
    #Ask for actor input
    #Checks if it is a valid input
    loop = True
    while loop:    
        try:
            actor = input("What is the name of the actor you are interested in?->")
            actor = float(actor)
            print("Sorry, numbers and decimals are not acceptable. Try again.")
            continue
        except ValueError:
            break
        except:
            print("\nSomething broke!")
            exit(1)
    return actor

def search_for_actor(noms, actor):
    #Creates a new nomination list
    #Tokenizes the old nomination list
    #Checks if the old nomination list matches the inputed actor
    num_noms = []
    for item in noms:
        toks = item.split(",")
        if actor == toks[3]:
            num_noms.append(item.strip())
    if num_noms == []:
        print(f"Sorry, {actor} was never nominated.")
        return 0
    return num_noms

def output_results(num_noms, nominee):
    #Finds the number of times the actor was nominated
    #Tokenizes the new nomination list
    #Makes sure the win/loss is printed
    #Displays the number of nominations, the years, the actor, the win/loss result, and the movies
    noms = len(num_noms)
    print(f"Actor {nominee} was nominated {noms} times.")
    for item in num_noms:
        toks = item.split(",")
        year = toks[0]
        win_lose = int(toks[2])
        actor = toks[3]
        movie = toks[4]
        if win_lose == 1:
            result = "Yes"
        else:
            result = "No"
        print(f"Yr: {year} | Actor: {actor} | Win: {result} | Movie: {movie}")

def ask_to_continue():
    #Asks for input if the user wants to continues
    #Checks for valid input
    #If yes continue, if no exit
    cont = True
    while cont:
        try:
            answer = input("Would you like to enter another actor? (Y or N)->")
            if answer.upper() != "Y" and answer.upper() != "N":
                print("That does not tell me what you want to do.")
                continue
            elif answer.upper() == "N":
                return 0
            elif answer.upper() == "Y":
                return 1
        except:
            print("\nSomething broke!")
            exit(1)

def main():
    #Open file and put into array
    #Get input of the actor wanted
    #Search the actors name in the file to find the number of times nominated
    #Outputs results if condition is met
    #If met, displays the number of nominations, the year, the actor, the win/loss column, and the movie
    #Asks the user if they want to go again
    keep_going = True
    while keep_going:
        nom_list = open_actor_file()
        actor = get_actor_input()
        num_noms = search_for_actor(nom_list, actor)
        if num_noms != 0:  
            output_results(num_noms, actor)
        yes_no = ask_to_continue()
        if yes_no == 0:
            print("Okay, we're done. You must of run out of actors!")
            break
        else:
            continue
main()