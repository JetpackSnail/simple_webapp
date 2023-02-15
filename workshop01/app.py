from flask import Flask, render_template
from helpers import get_rand_quote, get_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', quote=get_rand_quote(), repo_url=get_url())
