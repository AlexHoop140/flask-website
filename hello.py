import os
#import pdb; pdb.set_trace() #Xem giá trị từng dòng (debug)

from flask import Flask, url_for, request, render_template, redirect
from flask import flash, make_response
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/link')
def link():
    return url_for('show_user_name', username='Trung')
#url_for dùng để truy cập vào function '...', hiện đường link của function đó
#url_for('show_user_name', username='Trung')

@app.route('/user/<username>')
def show_user_name(username):
    return 'User name: ' + str(username)
#Có thể dùng 'User name %s' % username khỏi chuyển str() như trên

@app.route('/ID/<int:no_id>')
def show_user_id(no_id):
    return 'User ID: ' + str(no_id)
#Có thể dùng 'User ID %d' % ID khỏi chuyển str() như trên

@app.route('/index')
def index():
	return 'Index Page'

#Login và GET methods
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST": #lần đầu vào link sẽ là GET, get xong nó POST
	#if request.values:	#Nếu value có giá trị thì thực hiện dòng trên. Auto update
		return 'Welcome back, %s' % request.form['username']
	else:
		return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'
					#method="get" nó sẽ show username trên url
					#secure hơn thì dùng method=="POST"

@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
	error = None
	if request.method == "POST":
		if valid_login(request.form['username'], request.form['password']):
			flash('Succesfully Logged In')
			# return redirect(url_for('welcome', username=request.form.get('username')))
			response = make_response(redirect(url_for('welcome')))
			response.set_cookie('username', request.form.get('username'))
			return response
		else:
			error = 'Incorrect username or password'			
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	response = make_response(redirect(url_for('login_user')))
	response.set_cookie('username','', expires=0)
	return response

def valid_login(username, password):
	if username == 'Trung' and password == '24052002':
		return True
	elif username == 'Hoop' and password == 'abc.xyz':
		return True
	elif username == 'admin' and password == 'admin':
		return True
	else:
		return False

@app.route('/')
def welcome():
	username = request.cookies.get('username')
	if username:
		return render_template('welcome.html', username=username)
	else:
		return redirect(url_for('login_user'))

#@app.route('/welcome/<username>')
#def welcome(username):
#	return render_template('welcome.html', username=username)

if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	#app.debug = True
	#app.secret_key = 'Admin'
	app.run(host=host, port=port)