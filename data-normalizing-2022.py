import json
import string

currentYear = '2023'

def normalize_betiq():
    path = f"./original-data-{currentYear}/standard/betiq-yahoo.csv"
    save_path = f"./parsed-data-{currentYear}/standard/betiq-yahoo.json"
    with open(path, 'r') as f:
        lines = f.readlines()
        players = []
        for i, line in enumerate(lines):
            player = []
            data = line.strip().split(',')
            #rank, name, position, team
            player.append(data[0])
            player.append(data[1].replace('.K.','K').replace('.J.', 'J'))
            if 'DST' in data[2]:
                # rank, defense name, DST
                player.append('DST')
            else:
                if 'K' in data[2]:
                    player.append('K')
                else:
                    player.append(data[2][:2])
                player.append(data[3])
            print(player)
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)


def normalize_sporting_news(standard=True, year=currentYear):
    path = f"./original-data-{currentYear}/standard/sporting-news-standard.csv"
    save_path = f"./parsed-data-{currentYear}/standard/sporting-news-standard.json"
    with open(path, 'r') as f:
        lines = f.readlines()
        players = []
        for i, line in enumerate(lines):
            player = []
            data = line.replace('"','').strip().split(',')
            if year == '2022':
                if len(data) == 4:
                    #rank, name, position, team
                    player.append(data[0].strip())
                    player.append(data[1].strip())
                    player.append(data[3].strip())
                    player.append(data[2].strip())
                else:
                    # rank, defense name, DST
                    player.append(data[0])
                    temp = data[1].split()
                    player.append(data[1].strip())
                    player.append(data[2])
                    player.append(temp[-1].strip())
            elif year == '2023':
                data = [ x for x in data if x]
                if data[-1] != 'DST':
                    #players: rank, name, position, team
                    player.append(data[0])
                    name = ' '.join(data[1:-2])
                    player.append(name)
                    player.append(data[-1])
                    player.append(data[-2])
                else:
                    # defense: rank, defense name, dst
                    player.append(data[0])
                    team = ' ' .join(data[1:-1])
                    player.append(team)
                    player.append(data[-1])
                    print(data)
                print(player)
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)
    

def normalize_yahoo():
    path = f"./original-data-{currentYear}/ppr/yahoo-sports-expert-ranks-half-ppr.csv"
    save_path = f"./parsed-data-{currentYear}/ppr/yahoo-sports-expert-ranks-half-ppr.json"
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
    path = f"./original-data-{currentYear}/ppr/sports-illustrated-ppr.csv"
    save_path = f"./parsed-data-{currentYear}/ppr/sports-illustrated-ppr.json"
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
        path = f"./original-data-{currentYear}/standard/fantasy-pros-standard.csv"
        save_path = f"./parsed-data-{currentYear}/standard/fantasy-pros-standard.json"
    else:
        path = f"./original-data-{currentYear}/ppr/fantasy-pros-ppr.csv"
        save_path = f"./parsed-data-{currentYear}/ppr/fantasy-pros-ppr.json"
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
        path = f"./original-data-{currentYear}/standard/fantasy-football-calculator-standard.csv"
        save_path = f"./parsed-data-{currentYear}/standard/fantasy-football-calculator-standard.json"
    else:
        path = f"./original-data-{currentYear}/ppr/fantasy-football-calculator-ppr.csv"
        save_path = f"./parsed-data-{currentYear}/ppr/fantasy-football-calculator-ppr.json"
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
            name = data[1]
            team = data[2]
            position = data[3]
            bye = data[4]
            player.append(name.strip())
            player.append(position.strip())
            player.append(team.strip())
            player.append(bye.strip())
            players.append(player)
        with open(save_path, 'w') as f:
            json.dump(players, f, indent=4)


if __name__ == "__main__":
    normalize_fantasy_calc_standard(standard=True)
    #normalize_fantasy_calc_standard(standard=False)
    normalize_fantasy_pros(standard=True)
    #normalize_fantasy_pros(standard=False)
    normalize_sporting_news(standard=True, year=currentYear)
    # normalize_sports_illustrated()
    # normalize_yahoo()
    normalize_betiq()