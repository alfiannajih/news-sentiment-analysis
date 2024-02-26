from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/<query>", methods=["POST"])
def sentiment(query):
    #query = request.form["query"]
    
    return render_template("sentiment.html", query=query)