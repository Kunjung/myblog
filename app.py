from flask import Flask, render_template, request, url_for, redirect
import os, webbrowser

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#####################
# Setup Database
#######################
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Mars(db.Model):
	__tablename__ = 'mars'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)

	def __init__(self, name, password):
		self.name = name
		self.password = password


####################
# Routes and URLS
###################
@app.route('/')
def home():
	return render_template('home.html')
		
@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/signup')
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	

@app.route('/mars', methods=['POST'])
def mars():
	name = request.form['name']
	secret = request.form['password']

	if name == '' or secret == '':
		return redirect(url_for('signup'))

	# Sign up a new Person
	human = Mars(name, secret)
	db.session.add(human)
	db.session.commit()

	webbrowser.open('https://www.youtube.com/watch?v=3PsUJFEBC74')
	return render_template('mars.html', name=name)


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/calculator')
def calculator():
	return render_template('calculator.html')

@app.route('/applicants')
def applicants():
	applicants = Mars.query.all()
	return render_template('applicants.html', applicants = applicants)



if __name__ == '__main__':
	
	# Debug Mode
	#############
	#app.run(debug=True)

	# final mode
	#############
	#app.secret_key = os.urandom(12)
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)