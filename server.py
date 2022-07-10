from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def welcome():
    return "Welcome to the Playground!"


@app.route("/play/", methods=['GET'])
def play():
    return render_template("index.html", num=3)


@app.route("/play/<int:num>/", methods=['GET'])
def play_num(num):
    return render_template("index.html", num=num)


@app.route("/play/<int:num>/<string:color>/", methods=['GET'])
def play_num_color(num, color):
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
