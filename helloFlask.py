from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/demos')
@app.route('/demos/<category>')
def showDemo(category="Composition"):
	return render_template("demo_page.html",category=category)
