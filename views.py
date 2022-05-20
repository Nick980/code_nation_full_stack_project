from flask import Blueprint, render_template, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route("/index")
@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/worlds")
def worlds():
    return render_template("worlds.html")

@my_view.route("/factions")
def factions():
    return render_template("factions.html")

@my_view.route("/racesalliance")
def racesalliance():
    return render_template("racesalliance.html")

@my_view.route("/raceshorde")
def raceshorde():
    return render_template("raceshorde.html")

@my_view.route("/classes")
def classes():
    return render_template("classes.html")

@my_view.route("/expansions")
def expansions():
    return render_template("expansions.html")