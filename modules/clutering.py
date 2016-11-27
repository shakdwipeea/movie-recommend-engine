from __future__ import print_function
import numpy as np
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.externals import joblib
import pandas as pd
import modules.moviIdtoName as mov

stopwords = nltk.corpus.stopwords.words('english')
stemmer = SnowballStemmer("english")

def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

def getClusterTags():

    #titles = open('/Users/raghav/Documents/minor_pro/modules/title_list_mod.txt').read().split('\n')
    titles = list(range(1,186))


    synopses_imdb = open('/Users/raghav/Documents/minor_pro/modules/synopses_list_imdb_mod.txt').read().split('\n BREAKS HERE')
    synopses_imdb = synopses_imdb[:185]

    synopses_clean_imdb = []

    for text in synopses_imdb:
        text = BeautifulSoup(text, 'html.parser').getText()
        synopses_clean_imdb.append(text)

    synopses_imdb = synopses_clean_imdb

    synopses = []

    for i in range(len(synopses_imdb)):
        item = synopses_imdb[i]
        synopses.append(item)

    ranks = []

    for i in range(0,len(titles)):
        ranks.append(i)

    totalvocab_stemmed = []
    totalvocab_tokenized = []
    for i in synopses:
        allwords_stemmed = tokenize_and_stem(i)
        totalvocab_stemmed.extend(allwords_stemmed)

        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)

    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                     min_df=0.2, stop_words='english',
                                     use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

    tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)

    print(tfidf_matrix.shape)

    terms = tfidf_vectorizer.get_feature_names()
    dist = 1 - cosine_similarity(tfidf_matrix)

    num_clusters = 5

    km = KMeans(n_clusters=num_clusters)

    km.fit(tfidf_matrix)

    clusters = km.labels_.tolist()

    joblib.dump(km,  'doc_cluster.pkl')
    km = joblib.load('doc_cluster.pkl')
    clusters = km.labels_.tolist()
    films = { 'title': titles, 'rank': ranks, 'synopsis': synopses, 'cluster': clusters}

    frame = pd.DataFrame(films, index = [clusters] , columns = ['rank', 'title', 'cluster'])

    print("Top terms per cluster:")
    print()
    cluster_info = {}
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    for i in range(num_clusters):
        cluster_tags = []
        print("Cluster %d words:" % i, end='')
        for ind in order_centroids[i, :6]:
            cluster_tags.append(str(vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore')))
            print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
        print()
        print()
        print("Cluster %d titles:" % i, end='')
        for title in frame.ix[i]['title'].values.tolist():
            print(title)
            #mId = mov.getMovieId(str(ti))
            cluster_info[title] = cluster_tags
            #cluster_titles.append(str(title))
            #print(' %s,' % title, end='')
        print()
        print()
    return cluster_info
