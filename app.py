from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms.register_form import RegisterForm

import os


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "my_secret_key"


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
    if request.method == 'GET':
        return render_template("signin.html", title='Войти')
    else:
        # TODO: POST
        pass


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template("signup.html", title='Регистрация', form=form)
    else:
        # TODO: POST
        pass


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port)
    # app.run(host='127.0.0.1', port=port)


