from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/imageid")
def imageid():
    return render_template("imageid.html")

@app.route("/TVshows")
def webscraping():
    return render_template("TVshows.html")

if __name__ == "__main__":
    app.run(debug=True) 