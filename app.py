from flask import Flask, render_template, request, redirect
from models import db, Item

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create database tables


# Home route - show all items
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/services')
def services():
	return render_template('service.html')

@app.route('/projects')
def projects():
	return render_template('blog.html')

@app.route('/features')
def features():
	return render_template('feature.html')

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/testimonial')
def testimonial():
	return render_template('testimonial.html')

@app.route('/FAQ')
def FAQ():
	return render_template('FAQ.html')


# Add item route


if __name__ == "__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True)
