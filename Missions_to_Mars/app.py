from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app1"
mongo = PyMongo(app)

@app.route("/")
def index():
    marsing_data = mongo.db.collection.find_one()
    return render_template("indextwo.html", trip = marsing_data)

@app.route("/scrape")
def scrape():
    planet_data = scrape_mars.scrape()
    mongo.db.collection.update(
        {},
        planet_data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
