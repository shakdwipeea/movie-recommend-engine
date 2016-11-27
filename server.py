import os
from flask import Flask, request, redirect, url_for, render_template
import json
import urllib
from bs4 import BeautifulSoup
from random import randint
import modules.clutering as clust
import modules.moviIdtoName as movToName
#import pyCollaborativeFiltering.src.tes as recommend

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

# @app.route('/recommend', methods = ['GET'])
# def getRecommendation():
#     param = json.loads(request.data)
#     res = recommend.getRecommend(param['userId'])
#     return json.dumps()

@app.route('/getName', methods = ['GET'])
def getMovieName():
    param = json.loads(request.data)
    movName = movToName.getMovieName(str(param['movieId']))
    return json.dumps({'name' : movName})

@app.route('/randomMov', methods = ['GET'])
def getrandMov():
    x=[]
    for i in range(0,6):
        x.append(randint(1,186))
    return json.dumps({'init' : x})


if __name__ == "__main__":
	app.run(debug = False)
