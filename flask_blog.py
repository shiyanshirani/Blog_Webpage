from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterationForm
from models import User, Post

app = Flask(__name__)

app.config['SECRET_KEY'] = '7b8549b703e554ac883b29c2ad68df22'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


posts = [
    {
        'author': 'Shiyan Shirani',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '25th May 2021'
    },
    {
        'author': 'Anandita Puria',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '26th May 2021'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f'Successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
