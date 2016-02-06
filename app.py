from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs4
import requests
import urllib2, urllib, json


app = Flask(__name__)

results_dict = {}

@app.route("/", methods=["GET", "POST"])
def index():
  results = []
  if request.method == "POST":
    api_key = "8ac945a4cdb9dda7157ce9baad2c1a6f:14:69396910"
    query = request.form['query']
    base_url = "http://api.nytimes.com/svc/movies/v2/reviews/search.json?query={}&api-key={}".format(query, api_key)
    url_response = requests.get(base_url).json()
    results = url_response['results']
    print results

  return render_template("index.html", results=results)

@app.route("/check_review/<query>", methods=["GET", "POST"])
def check_review(query):
  results = []
  soup = bs4(requests.get(query).text, 'html.parser')
  soup = soup.findAll('p')
  for paragraph in soup:
    paragraph = str(paragraph).replace('<p>','')
    paragraph = str(paragraph).replace('</p>','')
  return soup

if __name__ == '__main__':
  app.run('0.0.0.0', debug="True")
