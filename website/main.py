from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/", methods=["POST"])
def sentiment():
    query = request.form["query"]
    
    return render_template("sentiment.html", query=query)