import constants
from copy import deepcopy
#deepcopy constructs a new object and copies the data: https://docs.python.org/3/library/copy.html
def print_team_statistics(local_team):
    experienced_players = len([player['experience'] for player in local_team if player['experience'] == True])
    print(f'the number of experienced players = {experienced_players}')
    players_on_team = [player['name'] for player in local_team]
    height_on_team = [player['height'] for player in local_team]
    print(players_on_team)
    #print('f the number of players on team = {players_on_team}
    print(height_on_team)
    #print('f the height of players on team = {height_on_team}')
    print(len(players_on_team))
    #print('f the full amount of all players on team = {len(players_pn_team)}
    print(sum(height_on_team)/len(players_on_team))
    #print('f the sum of all heights of all players on teams divided by the full amount of players on teams ={sum(height_on_team)/len(players_on_team)}
    

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
    panthers = []
    bandits = []
    warriors = []

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
      
    #print(experienced_player)
    while experienced_player:
        panthers.append(experienced_player.pop())
        warriors.append(experienced_player.pop())
        bandits.append(experienced_player.pop())
    print(panthers)

    while non_experienced_player:
        panthers.append(non_experienced_player.pop())
        warriors.append(non_experienced_player.pop())
        bandits.append(non_experienced_player.pop())
    #print(panthers)
    print_team_statistics(panthers)
    print_team_statistics(warriors)
    print_team_statistics(bandits)

    # divide players into two lists experienced or not, then assign them to a team evenly

def main():
    print("Hello, welcome to the bball game")
    new_player_list = processPlayers()
    assignPlayersToTeam(new_player_list)
    
    
    #-panth, warrs, bands = assignPlayer()
#-return panthers, warrios, bandits

#+displayStatistics(panthers) = panthers.count()

   #how many exp players on each team =
  #for every player, how many team
  #true
  
  #of players = 6
  #if you want to see average height type...
 
if __name__ == '__main__':
    main()
    
    #display team stats:name, total players/exp/non exp/average height of team
