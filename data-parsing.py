import json

def ff_calculator_parse():
    # this function reads unformatted data from fantasy football calculator .csv file,
    # parses and formats as json data.
    # this function also sets up the json data structure so that following functions
    # can look players up by name.
    # --------------------
    results = {}
    # open the file
    with open('./original-data/fantasy-football-calculator-rankings.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            # parse contents of file into python dict
            player = { 'rankings': {} }
            data_items = line.rstrip().split(',')
            player['rankings']['ff-calculator'] = int(data_items[0].rstrip())
            player['player-name'] = data_items[1].rstrip()
            player['bye-week'] = data_items[4].rstrip()
            player['team-name'] = data_items[3].rstrip()
            player['position'] = data_items[2].rstrip()
            results[data_items[1].rstrip()] = player
    # save data as json in new file
    with open('./parsed-data/data.json', 'w') as f:
        json.dump(results, f, indent=4)
    # done.

def yahoo_parse():
    # open existing data
    final_data = None
    with open('./parsed-data/data.json', 'r') as j:
        text = j.read()
        json_data = json.loads(text)
        results = {}
        # open the file
        with open('./original-data/yahoo-fantasy-rankings.csv', 'r') as f:
            lines = f.readlines()
            for line in lines[5:]:
                # parse the file
                data_items = line.rstrip().split(',')
                player_name = data_items[1].rstrip()
                if player_name in json_data.keys():
                    json_data[player_name]['rankings']['yahoo'] = int(data_items[0])
                else:
                    player = { 'rankings': {}}
                    player['rankings']['yahoo'] = int(data_items[0])
                    player['player-name'] = data_items[1].rstrip()
                    player['team-name'] = data_items[2].rstrip()
                    player['position'] = data_items[3].rstrip()
                    json_data[player_name] = player
        final_data = json_data
    with open('./parsed-data/data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    # done.

def si_parse():
    # open existing data
    final_data = None
    with open('./parsed-data/data.json', 'r') as j:
        text = j.read()
        json_data = json.loads(text)
        results = {}
        # open the file
        with open('./original-data/sports-ilustrated-rankings.csv', 'r') as f:
            lines = f.readlines()
            for line in lines[5:]:
                # parse the file
                data_items = line.rstrip().split(',')
                player_name = data_items[1].rstrip()
                if player_name in json_data.keys():
                    json_data[player_name]['rankings']['sports-illustrated'] = int(data_items[0])
                else:
                    player = { 'rankings': {}}
                    player['rankings']['sports-illustrated'] = int(data_items[0])
                    player['player-name'] = data_items[1].rstrip()
                    player['team-name'] = data_items[2].rstrip()
                    player['position'] = data_items[3].rstrip()
                    json_data[player_name] = player
        final_data = json_data
    with open('./parsed-data/data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    # done.

def ff_pros_parse():
    # open existing data
    final_data = None
    with open('./parsed-data/data.json', 'r') as j:
        text = j.read()
        json_data = json.loads(text)
        results = {}
        # open the file
        with open('./original-data/fantasy-pros-rankings.csv', 'r') as f:
            lines = f.readlines()
            for line in lines[2:]:
                # parse the file
                data_items = line.rstrip().split(',')
                player_name = ' '.join(data_items[2].rstrip().split(' ')[:-1])
                team_name = data_items[2].rstrip().split(' ')[-1]
                if player_name in json_data.keys():
                    json_data[player_name]['rankings']['fantasy-pros'] = int(data_items[0])
                    json_data[player_name]['position'] = data_items[3].rstrip()
                else:
                    player = { 'rankings': {}}
                    player['rankings']['fantasy-pros'] = int(data_items[0])
                    player['player-name'] = data_items[1].rstrip()
                    player['team-name'] = team_name
                    player['position'] = data_items[3].rstrip()
                    json_data[player_name] = player
        final_data = json_data
    with open('./parsed-data/data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    # done.

def rankings_calc():
    final_rankings = {}
    missing_players = []
    with open('./parsed-data/data.json', 'r') as j:
        text = j.read()
        json_data = json.loads(text)
        for key in json_data.keys():
            player = json_data[key]
            count = 0
            total = 0
            for ranking in player['rankings'].keys():
                count = count + 1
                total = total + player['rankings'][ranking]
            if 'position' not in player:
                print('incomplete player: ', key, count, (total/float(count)))
                missing_players.append(key)
            player['rank'] = (total/float(count))
            final_rankings[key] = player
    with open('./parsed-data/data.json', 'w') as f:
        json.dump(final_rankings, f, indent=4)
    missing_players.sort()
    # print(missing_players)
    # done.

if __name__ == "__main__":
    ff_calculator_parse()
    yahoo_parse()
    si_parse()
    ff_pros_parse()
    rankings_calc()