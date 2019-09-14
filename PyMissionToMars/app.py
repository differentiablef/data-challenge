# imports/config ###############################################################

from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# methods/endpoints ############################################################

@app.route('/')
def main():
    info = client.marsdb.front_page.find()
    return render_template('index.html', info=info[0])

@app.route('/scrape')
def do_scrape():
    from scrape_mars import scrape
    out = scrape()
    client.marsdb.front_page.insert_one( out )
    return "done."

# script entry-point ###########################################################

if __name__ == "__main__":
    app.run(debug=True)
