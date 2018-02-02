from flask import Flask, render_template, request
import os
import tweepy

app = Flask(__name__)

script_dir = os.path.dirname(__file__)
tweet_file = 'data/hex.txt'
tweet_path = os.path.join(script_dir, tweet_file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():

    with open(tweet_path) as f:
        stuff = f.readlines()[-1]

    return render_template('suggestions.html', suggestions=stuff)


if __name__ == '__main__':
    app.run(debug=True)
