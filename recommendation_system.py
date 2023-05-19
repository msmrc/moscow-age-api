import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class RecommendationSystem:
    def __init__(self): 
        self.dataset = pd.read_csv('')
        tfidf = TfidfVectorizer(stop_words='russian')
        self.dataset['overview'] = self.dataset['overview'].fillna('')
        tfidf_matrix = tfidf.fit_transform(self.dataset['overview'])

        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    def get_recommendations(self):
        pass