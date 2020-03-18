from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(ssl_context='adhoc')


