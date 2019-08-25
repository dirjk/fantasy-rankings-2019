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
                    # print('new player!', player_name)
                    player = { 'rankings': {}}
                    player['rankings']['yahoo'] = int(data_items[0])
                    player['player-name'] = data_items[1].rstrip()
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
                    # print('new player!', player_name)
                    player = { 'rankings': {}}
                    player['rankings']['sports-illustrated'] = int(data_items[0])
                    player['player-name'] = data_items[1].rstrip()
                    json_data[player_name] = player
        final_data = json_data
    with open('./parsed-data/data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    # done.
if __name__ == "__main__":
    ff_calculator_parse()
    yahoo_parse()
    si_parse()