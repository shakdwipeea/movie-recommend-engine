import os
from flask import Flask, request, redirect, url_for, render_template
import json
import urllib
from bs4 import BeautifulSoup
import modules.clutering as clust
import pyCollaborativeFiltering.src.tes as recommend

app = Flask(__name__)

@app.route('/list', methods = ['GET'])
def getListOfMovies():
    with open('modules/movList.json', 'r') as json_data:
        d = json.load(json_data)
    return json.dumps(d)

@app.route('/clusterTags', methods = ['GET'])
def getTags():
    res = clust.getClusterTags()
    print(res)
    return json.dumps(res)

@app.route('/recommend', methods = ['GET'])
def getRecommendation():
    param = json.loads(request.data)
    res = recommend.getRecommend(param['userId'])
    return json.dumps()

if __name__ == "__main__":
	app.run(debug = False)
