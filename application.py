


import constants
from copy import deepcopy

def processPlayers():
    players = deepcopy(constants.Players)
    for player in players:
    #handle the data , convert to true /false, height to a number
    print(player['guardian'])

def assignPlayersToTeam():

    print("inside assign function")

    # divide players into two lists experienced or not, then assign them to a team evenly


def main():
    print("Hello, welcome to the bball game")
    processPlayers()

  assignPlayersToTeam()

if __name__ == '__main__':
    main()
