import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/joke')
def joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    return {
        'setup': joke['setup'],
        'punchline': joke['punchline']
    }

if __name__ == '__main__':
    app.run(debug=True)
