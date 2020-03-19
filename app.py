from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Главная')


@app.route('/about')
def about():
    return render_template("about.html", title='О нас')


@app.route('/right')
def right():
    return render_template("sidebar-right.html", title='1')


@app.route('/contact')
def contact():
    return render_template("contact.html", title='Контакты')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html", title='Войти')


@app.route('/signup')
def signup():
    return render_template("signup.html", title='Регистрация')


if __name__ == "__main__":
    app.run()


