import os
from flask import Flask, url_for, render_template, request, redirect
from flask import flash, session

app = Flask(__name__)

@app.route('/')
def SweetW2():
	return render_template('SweetWA2.html')


if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 1111))
	app.debug = True
	app.secret_key = '123.abc'
	app.run(host=host, port=port)
