from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from scrape import scrapeArticles

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/nasaArticles'
mongo = PyMongo(app)

@app.route("/")
def index():
    article_list = mongo.db.articles.find()
    return render_template("index.html", article_list = article_list)

@app.route("/scrape")
def scrapePage():
    mongo.db.drop_collection(mongo.db.articles)
    articles = mongo.db.articles
    scrape_articles = scrapeArticles()
    articles.update({},scrape_articles, upsert = True)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)