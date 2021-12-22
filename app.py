import scrape_mars
import pymongo
from flask import Flask,jsonify,render_template,redirect

app = Flask(__name__)

@app.route("/")
def index():
    #  read data from mongodb
    conn = 'mongodb://localhost:27017'
    client =  pymongo.MongoClient(conn)
    db = client.marsDB
    results = db.mars_data.find_one()
   
    return render_template("index.html",  listings = results)
    
    #use data to populate index.html

@app.route("/scrape")
def scrape_rte():

    scrape_data = scrape_mars.scrape()
    conn = 'mongodb://localhost:27017'
    client =  pymongo.MongoClient(conn)
    db = client.marsDB
    lst = db.list_collection_names()
    if "mars_data" in lst:
        db.mars_data.delete_many({})
    db.mars_data.insert_one(scrape_data)
   
    return redirect("/")

   

if __name__ == "__main__":
    app.run(debug=True)