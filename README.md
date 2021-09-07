# fantasy-rankings-2019

a simple one day project that takes in multiple sources for fantasy football draft rankings, normalizes the data, and then displays using react.

Youtube video is available for watching development of this project.
https://youtu.be/J8EGp1Pksdo

To run the project on your local machine, you will need to install node and npm.

Once that is done, navigate into the `react-ff` folder and run `npm start`. The website should open automatically once the script is running.

# using this in the future

## what type of league are you in?

Lauren's Legit League is STANDARD scoring, not PPR (as of 2021).

WAFFL is PPR (as of 2021).

## collect all the data

(as of 2021):

https://fantasyfootballcalculator.com/rankings/standard

https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php

https://www.si.com/fantasy/2021/06/25/top-200-ppr-redraft-rankings

(note that I couldn't find a sports illustrated standard ranking list)

https://sports.yahoo.com/fantasy-football-draft-rankings-for-2021-nfl-season-164710339.html

## Normalize the data

Run the provided scripts. These scripts will parse the data from the copy/pasted format from the websites and normalize them to CSV files in the respective `parsed-data` folder.

`python data-normalizing-2021.py`

this script will create new `.json` files where each is a list of lists, where the items are formated:

`[ rank, name, team, position, bye week ]` not all sources have the bye week.

## combine the data into a final ranking

run the parsing script:

`python data-parsing-2021.py

this will display a list of players who don't have the full list of sources as part of their rankings. Go through this list and determine which ones should be combined (due to spelling differences, punctuation differences, etc), and  which ones can be ignored.

## set up the front end package.

copy the data.json file you want to use into the following javascript function:

`./react-ff/src/parsed-data/data.js: getData()`

then run `npm start` to start the website