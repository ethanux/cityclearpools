from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import db, Project
import os
app = Flask(__name__)
app.secret_key = "super secret key"
# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://victor:aTGv9sS4d7hBhJ56SGDcsCxqfoBSHHjQ@dpg-d37tbqruibrs739b5of0-a.oregon-postgres.render.com/cityclearpools'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


db.init_app(app)

# Create database tables


# Home route - show all items
@app.route('/')
def home():
	projects = Project.query.all()  # get all projects from DB
	return render_template('index.html',projects=projects)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/services')
def services():
	return render_template('service.html')

@app.route('/projects')
def projects():
	projects = Project.query.all()  # get all projects from DB
	return render_template('blog.html',projects=projects)

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


@app.route("/dashboard")
def dash():
	projects = Project.query.all()  # get all projects from DB
	return render_template("dash/earnings.html",projects=projects)


@app.route("/add/projects",methods=["GET", "POST"])
def upload_project():
	if request.method == "POST":
        # Get form data
		image = request.files["image"]
		work_type = request.form["type"]
		comment = request.form["comment"]

		if image:
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
			
			new_project = Project(
				image=filename,   # store filename only, not full path
				ptype=work_type,
				comment=comment
			)
			db.session.add(new_project)
			db.session.commit()

			flash(f"Project uploaded successfully! Work Type: {work_type}, Comment: {comment}", "success")
			return redirect(url_for("dash"))


	return redirect(url_for('dash'))

@app.route("/delete/<int:project_id>")
def delete_project(project_id):
	project = Project.query.get(project_id)
	if project:
		db.session.delete(project)
		db.session.commit()
	return redirect(url_for("dash"))

if __name__ == "__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True)
