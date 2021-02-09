import requests
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    image_tag = "<img src=" + response['icon_url'] + ">"

    return "<strong>Random joke from chuck norris: </strong>" + response['value'] + image_tag


if __name__ == '__main__':
    app.run(debug=True)
