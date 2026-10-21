from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/omoss")
def omoss():
    return render_template("omoss.html")


if __name__=="__main__":
    app.run(debug = True)