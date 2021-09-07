import json

global_players = {}

ppr_paths = [
    './parsed-data-2021/ppr/yahoo-sports-expert-ranks-half-ppr.json',
    './parsed-data-2021/ppr/sports-illustrated-ppr.json',
    './parsed-data-2021/ppr/fantasy-pros-ppr.json',
    './parsed-data-2021/ppr/fantasy-football-calculator-ppr.json'

]
standard_paths = [
    './parsed-data-2021/standard/fantasy-pros-standard.json',
    './parsed-data-2021/standard/fantasy-football-calculator-standard.json'
]

def combine_data():
    # reset every time:
    global_players = {}
    # ppr:
    # paths = ppr_paths
    # save_path = './parsed-data-2021/ppr/data.json'
    # standard:
    paths = standard_paths
    save_path = './parsed-data-2021/standard/data.json'
    # combined:
    # paths = ppr_paths + standard_paths
    # save_path = './parsed-data-2021/combined-data.json'

    path_count = len(paths)
    for path in paths:
        key = path.split('/')[-1].split('.')[0]
        with open(path, 'r') as f:
            players = json.load(f)
            for data in players:
                #rank, name, position, team, bye
                name = data[1]
                player = {'rankings': {}}
                if not name in global_players.keys():
                    # they don't exist!
                    player['player-name'] = name
                    player['team-name'] = data[3]
                    player['position'] = data[2]
                else:
                    player = global_players[name]
                # here we do the bye week            
                try:
                    player['bye-week'] = data[4]
                except:
                    pass
                # and the ranking for this source
                player['rankings'][key] = data[0]
                # finally we put it back into the global store
                global_players[name] = player
    # now we calculate the rank for each player in the global state
    print("Players with missing sources:")
    for key in global_players.keys():
        player = global_players[key]
        sum = 0
        source_count = len(player['rankings'].keys())
        for source in player['rankings'].keys():
            sum = sum + int(player['rankings'][source])
        player['rank'] = sum / source_count
        if source_count != path_count:
            print(player['player-name'])
        global_players[key] = player
    with open(save_path, 'w') as f:
        json.dump(global_players, f, indent=4)





if __name__ == '__main__':
    combine_data()