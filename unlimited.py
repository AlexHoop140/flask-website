import os, sys, webbrowser, pyperclip
from flask import Flask, url_for, render_template, request, redirect
from flask import flash, session
import pymysql
import urllib.request

web = Flask(__name__)

@web.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			flash("Logged In")
			session['username'] = request.form.get('username')
			return redirect(url_for('welcome'))
		else:
			error = 'Incorrect password or username'
	return render_template('login.html', error=error)

@web.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))

@web.route('/')
def welcome():
	if 'username' in session:
		#return render_template('welcome.html', username=session['username'], valid_login=valid_login)
		return render_template('about.html')
	else:
		return redirect(url_for('login'))

@web.route('/home')
def home_index():
	return render_template('index.html')

@web.route('/youtube')
def youtube():
	return redirect('https://www.youtube.com/watch?v=K4vQbBNLjfg')

@web.route('/ticketbox')
def see_sing_share():
	return redirect('https://ticketbox.vn/event/see-sing-share-concert-70214/46098')

@web.route('/shutterstock')
def getting_image():
	if len(pyperclip.paste()) > 1:
		id = pyperclip.paste()
		render_template('getimage.html', id = request.form['Photo ID'])
	return webbrowser.open('https://techblogup.com/ss-api.php?id=[{0}]&proxy=192.168.1.1:202'.format(id))
	
@web.route('/test')
def testing():
	return render_template('hello.html')

@web.route('/contact')
def contactus():
	return redirect('https://fb.com/StudentsWhoCode')

@web.route('/st3')
def download():
	return redirect('https://download.sublimetext.com/Sublime Text Build 3207 Setup.exe')

def valid_login(username, password):
	if username == 'admin' and password == 'admin':
		return True
	else:
		return False

'''
def getConnection():
	connection = pymysql.connect(
		host='0.0.0.0'
		user ='admin'
		password ='admin'
					)'''	


if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 2405))
	web.debug = True
	web.secret_key = '123.abc'
	web.run(host=host, port=port)