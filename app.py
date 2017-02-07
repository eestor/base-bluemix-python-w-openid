
import os
from flask import Flask, render_template, jsonify, session, flash, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'secret'

@app.route('/login', methods=['POST','GET'] )
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash("Welcome , {}".format(request.form['username']))
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
     session.pop('logged_in', None)
     flash('You were logged out')
     return redirect(url_for('homepage'))


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
