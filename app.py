from flask import Flask, render_template, request, redirect, url_for
import requests
from logo import Logo

app = Flask(__name__)

TOKEN = "9fc1cdde8654b1b0d0253196b42c2158ebc1d0d9"

def shortener(LINK, TOKEN):
    response_data = {"long_url": LINK}
    header = {
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.post(url="https://api-ssl.bitly.com/v4/shorten", headers=header, json=response_data)
    shorten_link = response.json().get('link')
    return shorten_link

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = shortener(LINK=long_url, TOKEN=TOKEN)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', short_url=None)

if __name__ == '__main__':
    print(Logo)
    app.run(debug=True)
