#Name: Nicholas Boes (nboes)
#Final Problem: 2

#Import the team class
from Football_Classes import teams

def get_conference(team_list):
    #Obtains the conference from the user and checks for valid input
    conf_list = []
    cont = True
    while cont:
        conf = input("What conference do you want?->")
        try:
            #Checks for numbers
            conf = float(conf)
            print(f"Input ({conf}) is a number. Try again with a string.")
        except ValueError:
            for team in team_list:
                if conf == team.get_conf():
                    conf_list.append(team)
            #Checks for no team matches
            if conf_list == []:
                print(f"I found no teams from the {conf} conference. Try again with a different (or actual) conference.")
            else:
                break
        except:
            print("Something broke!")
            exit(1)
    return conf_list

def get_total_wins(conf_list):
    #Gets the total wins for a conference
    tot_wins = 0
    for team in conf_list:
        tot_wins += team.get_wins()
    return tot_wins

def output_teams(conf_list, tot_wins):
    #Loops through and displays each item and the total wins for the conference
    for team in conf_list:
        print(f"Perc: {round((team.get_win_perc()* 100),2)} | Wins: {team.get_wins()} | Loss: {team.get_loss()} | Conf: {team.get_conf()} | Name: {team.get_name()}")
    print(f"Total Wins in the {conf_list[0].get_conf()} conference: {tot_wins} wins")
        
def main():
    #Create object team_list from the teams' records, name, and division (conference)
    team_list = []
    team_list.append(teams("Bears", "North", 6, 6))
    team_list.append(teams("Packers", "North", 8, 1))
    team_list.append(teams("Lions", "North", 4, 6))
    team_list.append(teams("Saints", "South", 9, 2))
    team_list.append(teams("Panthers", "South", 5, 6))
    #Get the conference information
    conf = get_conference(team_list)
    #Find the total wins for the conference
    total_wins = get_total_wins(conf)
    #Outputs the results
    output_teams(conf, total_wins)
main()
