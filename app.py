from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

# TMDb API setup
API_KEY = '8658b9440153fced012b15bfa0266dc7'
API_URL = 'https://api.themoviedb.org/3/movie/popular'
POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'  # Poster base URL

def get_movies():
    response = requests.get(API_URL, params={'api_key': API_KEY})
    if response.status_code == 200:
        data = response.json()
        return [{'title': movie['title'], 'poster': POSTER_BASE_URL + movie['poster_path']} for movie in data['results']]
    return []

@app.route('/')
def index():
    movies = get_movies()
    movie = random.choice(movies) if movies else {"title": "No movies available", "poster": ""}
    return render_template('index.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
