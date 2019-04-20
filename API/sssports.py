from flask import Flask, render_template
app = Flask(__name__)

import requests
import json
import pandas as pd

API_KEY = '4915aca12c724fa2ae27a0230086ef1d'
ENDPOINT = 'https://api.football-data.org/v2/'
headers = {'X-Auth-Token' : API_KEY}

"""
	Standings 
"""
standingsResponse = requests.get(ENDPOINT + 'competitions/2021/standings', headers = headers)
standingsResult = standingsResponse.json()['standings'][0]['table'] #list

eplStandings = pd.DataFrame()
for i in range(len(standingsResult)):
	temp = pd.DataFrame(standingsResult[i]).iloc[2]
	row = pd.DataFrame(temp).T
	eplStandings = pd.concat([eplStandings, row], ignore_index = True)

eplStandingsColumns = ['position','team','playedGames','won','draw','lost','points','goalsFor','goalsAgainst','goalDifference']

"""
	Matches
"""
matchesResponse = requests.get(ENDPOINT + 'competitions/2021/matches/', headers = headers)
matchesResult = matchesResponse.json()['matches']

eplMatches = pd.DataFrame()
for match in matchesResult:
	temp = dict([('homeTeam', match['homeTeam']['name']), ('homeScore', match['score']['fullTime']['homeTeam']), ('dash', '-'), ('awayScore', match['score']['fullTime']['awayTeam']), ('awayTeam', match['awayTeam']['name'])])
	row = pd.DataFrame(temp, index = [0])
	eplMatches = pd.concat([eplMatches,row], ignore_index = True)

eplMatchesColumns = ['homeTeam','homeScore','dash','awayScore','awayTeam']

@app.route("/home")
def home():
	return render_template('home.html') 

@app.route("/standings")
def standings():
	return render_template('standings.html', epltable=eplStandings.to_html(index=False, columns=eplStandingsColumns))

@app.route("/matches")
def matches():
	return render_template('matches.html', eplmatches=eplMatches.to_html(index=False, columns=eplMatchesColumns, header=False))

if __name__ == "__main__":
	app.run(debug = True)
