import constants
from copy import deepcopy
#deepcopy constructs a new object and copies the data: https://docs.python.org/3/library/copy.html
def print_team_statistics(local_team):
    experienced_players = len([player['experience'] for player in local_team if player['experience'] == True])
    print(f'the number of experienced players = {experienced_players}')
    players_on_team = [player['name'] for player in local_team]
    height_on_team = [player['height'] for player in local_team]
    print('The names of my players are')
    print(players_on_team)
    #print('f the number of players on team = {players_on_team}
    ##print('f the number of total players is = {number_of_players_on_on_team}')
    print('The heights of my players are') 
    print(height_on_team)
    #?print('f the height of players on team = {height_on_team}')
    #print(f'the average height of the team is {average_height_on_team}')
    ##total_height_on_team = [player['height'] for player in local_team]=len(players_on_team)
    #print(len(players_on_team))
    print(f'the full amount of all players on team = {len(players_on_team)}')
    print (f'average_height_team = {sum(height_on_team)/len(players_on_team)}')
    #print (f'average_height_on_team=total_height_on_team/number_of_players_on_team
    #Not Needed:print('f the sum of all heights of all players on teams divided by the full amount of players on teams ={sum(height_on_team)/len(players_on_team)}

    def print_team_statistics(local_team):
    players_on_team = [player['name'] for player in local_team]
    guardians_on_team = [player['guardians'] for player in local_team]
    print(f'the total count of players on team = {len(players_on_team)}')
    experienced_players = len([player['experience'] for player in local_team if player['experience'] == True])
    inexperienced_players = len([player['experience'] for player in local_team if player['experience'] == False])
    print(f'the number of experienced players = {experienced_players}')
    print(f'the number of Inexperienced players = {inexperienced_players}')
    height_on_team = [player['height'] for player in local_team]
    height_on_team_in_strings = [str(player['height']) for player in local_team]
    print('The names of my players are')
    print(",".join(players_on_team))
    print('The guardians of my players are')
    print(",".join(guardians_on_team))
    print (f'average_height_team = {sum(height_on_team)/len(players_on_team)}')
    print()
    print("The details of the players are:")
    for a_player in local_team:
      print("player name: " + a_player['name'])
      print("guardian: " + a_player['guardians'])
      print("height:" + str(a_player['height']))
      print()



def processPlayers():
    players = deepcopy(constants.PLAYERS)
    for player in players:
    #handle the data , convert to true /false, height to a number
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
   
        height = player['height'].split()
        player['height'] = int(height[0])
       
    return players
         

def assignPlayersToTeam(players):
    teams = constants.TEAMS[:]
    panthers = []
    bandits = []
    warriors = []

    
    experienced_player = []
    non_experienced_player = []
    for player in players: 
        if player['experience'] == True:
            experienced_player.append(player)
        else:
            non_experienced_player.append(player)
            
    inexperienced_players = []
    #count the inexperienced, then display
    inexperienced_players = len([player['experience'] for player in local_team if player['experience'] == False])
    print(f'the number of Inexperienced players = {inexperienced_players}')

      
    #print(experienced_player)
    while experienced_player:
        panthers.append(experienced_player.pop())
        warriors.append(experienced_player.pop())
        bandits.append(experienced_player.pop())
   

    while non_experienced_player:
        panthers.append(non_experienced_player.pop())
        warriors.append(non_experienced_player.pop())
        bandits.append(non_experienced_player.pop())
    #print(panthers)
    #print_team_statistics(panthers)
    #print_team_statistics(warriors)
    #print_team_statistics(bandits)
    return panthers, warriors, bandits
  
def displayMenuOptions(panthers, warriors, bandits):
    while True:
        menu()
        command = input("Please enter the number for the COMMAND that you want >   ")
        print()
        if command == '1':
            sub_menu()
            option = input("Please enter the number for the OPTION that you want >   ")
            if (option == '1'):
              print("TEAM name: Panthers")
              print_team_statistics(panthers)
            elif (option == '2'):
              print("TEAM name: Warriors")
              print_team_statistics(warriors)
            else:
              print("TEAM name: Bandits")
              print_team_statistics(bandits)

            if (option == '1'):
              print_team_statistics(panthers)
            elif (option == '2'):
              print_team_statistics(warriors)
            else:
              print_team_statistics(bandits)
              
        elif command == '2':
            print("Good bye.\n\n")
            break
        else:
            print("\nThat is not a valid option. Please try again. \n")
            continue
            
def menu():
    print()
    print('These are the options for the Basketball Stats game')
    print("type 1 to display team_stats")
    print("type 2 to display to quit")

      
    
def sub_menu():
    print("type 1 for panthers")
    print("type 2 for bandits")
    print("type 3 for warriors")


   
    # divide players into two lists experienced or not, then assign them to a team evenly

def main():
    print("Hello, welcome to the bball game")
    new_player_list = processPlayers()
    panthers, warriors, bandits = assignPlayersToTeam(new_player_list)
    displayMenuOptions(panthers, warriors, bandits)
    #panthwers, warriors, bandits = assignPlayer()
    #return panthers, warriors, bandits

#+displayStatistics(panthers) = panthers.count()

   #how many exp players on each team =
  #for every player, how many team
  #true
  
  #of players = 6
  #if you want to see average height type...
if __name__ == '__main__':
    main()
    
    #display team stats:name, total players/exp/non exp/average height of team
    
