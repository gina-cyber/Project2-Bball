import constants
from copy import deepcopy

def processPlayers():
    players = deepcopy(constants.PLAYERS)
    for player in players:
    #handle the data , convert to true /false, height to a number
         print(player['guardians'])
         if player['experience'] == 'YES':
            player['experience'] = True
         else:
            player['experience'] = False

         print(player['experience'])
         print(player['height'])
         height = player['height'].split()
         player['height'] = int(height[0])
         print(player['height'])
    return players
         

def assignPlayersToTeam(players):
    teams = constants.TEAMS[:]
    for team_name in teams:
        print(team_name)
    print("inside assign function")
    experienced_player = []
    non_experienced_player = []
    for player in players: 
        if player['experience'] == True:
            experienced_player.append(player)
        else:
            non_experienced_player.append(player)
      
    print(experienced_player)

    

    # divide players into two lists experienced or not, then assign them to a team evenly

def main():
    print("Hello, welcome to the bball game")
    new_player_list = processPlayers()
    assignPlayersToTeam(new_player_list)
   


if __name__ == '__main__':
    main()
