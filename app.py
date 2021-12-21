import scrape_mars
import pymongo
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    #  read data from mongodb

    #use data to populate index.html

@app.route("/scrape")
def scrape_rte():

    scrape_data = scrape_mars.scrape()

    #store data into mongo

    # go back to index route

if __name__ == "__main__":
    app.run(debug=True)