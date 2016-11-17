from flask import Flask, render_template, request, url_for, redirect
import os, webbrowser

app = Flask(__name__)

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
		webbrowser.open('https://www.youtube.com/watch?v=3PsUJFEBC74')
		return redirect(url_for('signup'))
	
	return render_template('mars.html', name=name)


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/calculator')
def calculator():
	return render_template('calculator.html')



if __name__ == '__main__':
	
	# Debug Mode
	#############
	#app.run(debug=True)

	# final mode
	#############
	#app.secret_key = os.urandom(12)
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)