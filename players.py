### This file contains a function that will return a list with the 
# four player from 'ParticipantsList.txt' as instances of the Player class


def players_bj():    

    from bj_classes import Player
    
    attribute_file = open('ParticipantsList.txt', mode='rt', encoding='utf-8')
    attribute_list = attribute_file.readlines()
    

    Player1 = attribute_list[0].split()
    Player2 = attribute_list[1].split()
    Player3 = attribute_list[2].split()
    Player4 = attribute_list[3].split()


    player1 = Player(str(Player1[0]),
                            str(Player1[1]),
                            2020 - int(Player1[2]),
                            str(Player1[3]),
                            int(Player1[4])
                            )


    player2 = Player(str(Player2[0]),
                            str(Player2[1]),
                            2020 - int(Player2[2]),
                            str(Player2[3]),
                            int(Player2[4])
                            )


    player3 = Player(str(Player3[0]),
                            str(Player3[1]),
                            2020 - int(Player3[2]),
                            str(Player3[3]),
                            int(Player3[4])
                            )

    player4 = Player(str(Player4[0]),
                            str(Player4[1]),
                            2020 - int(Player4[2]),
                            str(Player4[3]),
                            int(Player4[4])
                            )
    players_list = [player1, player2, player3, player4]
    return players_list


