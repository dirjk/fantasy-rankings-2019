import json
import string


def normalize_yahoo():
    path = './original-data-2021/ppr/yahoo-sports-expert-ranks-half-ppr.csv'
    save_path = './parsed-data-2021/ppr/yahoo-sports-expert-ranks-half-ppr.json'
    with open(path, 'r') as f:
        lines = f.readlines()
        players = []
        for i, line in enumerate(lines):
            player = []
            #rank, name, position, team
            data = line.rstrip().split(',')
            player.append(data[0])
            player.append(data[1].split('(')[0].strip())
            player.append(data[1].split('(')[1].split(')')[0].split('-')[1].strip())
            player.append(data[1].split('(')[1].split(')')[0].split('-')[0].strip())
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)

def normalize_sports_illustrated():
    path = './original-data-2021/ppr/sports-illustrated-ppr.csv'
    save_path = './parsed-data-2021/ppr/sports-illustrated-ppr.json'
    with open(path, 'r') as f:
        lines = f.readlines()
        players = []
        for i, line in enumerate(lines):
            player = []
            #rank, name, position, team
            data = line.rstrip().split(',')
            player.append(str(i + 1))
            player.append(data[0].strip())
            player.append(data[1].rstrip(string.digits).strip())
            player.append(data[2].strip())
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)


def normalize_fantasy_pros(standard=True):
    path = ''
    save_path = ''
    if standard:
        path = './original-data-2021/standard/fantasy-pros-standard.csv'
        save_path = './parsed-data-2021/standard/fantasy-pros-standard.json'
    else:
        path = './original-data-2021/ppr/fantasy-pros-ppr.csv'
        save_path = './parsed-data-2021/ppr/fantasy-pros-ppr.json'
    # open the file:
    with open(path, 'r') as f:
        lines = f.readlines()
        players = []
        for line in lines:
            player = []
            #rank, name, position, team, bye
            data = line.rstrip().split(',')
            player.append(data[0].strip())
            name = data[2].split('(')[0].strip()
            player.append(name.strip())
            position = data[3].rstrip(string.digits)
            player.append(position.strip())
            team = data[2].split('(')[1].split(')')[0]
            player.append(team.strip())
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)

def normalize_fantasy_calc_standard(standard=True):
    path = ''
    save_path = ''
    if standard:
        path = './original-data-2021/standard/fantasy-football-calculator-standard.csv'
        save_path = './parsed-data-2021/standard/fantasy-football-calculator-standard.json'
    else:
        path = './original-data-2021/ppr/fantasy-football-calculator-ppr.csv'
        save_path = './parsed-data-2021/ppr/fantasy-football-calculator-ppr.json'
    # open the file:
    with open(path, 'r') as f:
        lines = f.readlines()
        players = []
        for line in lines:
            player = []
            #rank, name, position, team, bye
            data = line.rstrip().split(',')
            # rank
            player.append(data[0])
            if data[6] == '':
                name = data[1] + ' ' + data[2]
                team = data[3]
                position = data[4]
                bye = data[5]
            else:
                name = data[1] + ' ' + data[2] + ' ' + data[3]
                team = data[4]
                position = data[5]
                bye = data[6]
            player.append(name.strip())
            player.append(position.strip())
            player.append(team.strip())
            player.append(bye.strip())
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)


if __name__ == "__main__":
    normalize_fantasy_calc_standard(standard=True)
    normalize_fantasy_calc_standard(standard=False)
    normalize_fantasy_pros(standard=True)
    normalize_fantasy_pros(standard=False)
    normalize_sports_illustrated()
    normalize_yahoo()