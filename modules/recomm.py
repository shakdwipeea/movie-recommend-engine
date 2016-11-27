from sklearn.base import BaseEstimator
from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender

movies = {1:{1:3.0,2:4.0,3:5.0,4:4.5}, 2:{2:1.0,5:2.5}}

model = MatrixPreferenceDataModel(movies)
similarity = UserSimilarity(model, pearson_correlation)
recommender = UserBasedRecommender(model, similarity, with_preference=True)
recommender.recommend(2)
