from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index-calc.html")

#@app.route("/greet")
#def greet():
      #name = request.args.get("name")
      #return render_template("Layout.html", name=name)
