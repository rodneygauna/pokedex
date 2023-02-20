'''
Flask application that searches for pokemon and displays their information
Uses the PokeAPI to get the pokemon information
'''

from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Home page to search and display pokemon'''
    if request.method == 'POST':
        pokemon_name = request.form['pokemon_name']
        if pokemon_name:
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                pokemon = response.json()
                pokemon_types = [t['type']['name'] for t in pokemon['types']]
                pokemon_games = [g['version']['name']
                                 for g in pokemon['game_indices']]
                return render_template('index.html',
                                       pokemon=pokemon,
                                       pokemon_types=pokemon_types,
                                       pokemon_games=pokemon_games)
            return render_template('index.html', error='Pokemon not found')
        return render_template('index.html', error='Try searching again')
    return render_template('index.html')
