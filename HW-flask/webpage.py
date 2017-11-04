from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\\lessons\\HW-flask\\blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telephone = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route("/")
def main ():
    return render_template("about.html")

@app.route("/about")
def about ():
    return render_template("about.html")

@app.route("/skills")
def skills ():
    return render_template("skills.html")

@app.route("/pygame")
def pygame ():
    return render_template("pygame.html")

@app.route("/addcontact")
def addcontact ():
    return render_template("addcontact.html")

@app.route("/mycontacts")
def mycontacts ():
    contacts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template("mycontacts.html" , contacts=contacts)

@app.route("/addcontactpost", methods = ['POST'])
def addcontactpost ():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    telephone = request.form['phone']
    content = request.form['content']
    contact = Blogpost(name=name, surname=surname, email=email, telephone=telephone, content=content, date_posted=datetime.now())
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for('mycontacts'))

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)

if __name__  == "__main__":
    app.run(debug=True)