import pickle
from os.path import join, dirname, realpath
from gensim.models import word2vec
import gensim
from sklearn import svm
import numpy as np

class SVM:
    def __init__(self):
        path = dirname(realpath(__file__))
        self.model_svm = pickle.load(open(path + '/sorteml.sav', 'rb'))
        self.modelo_w2v = pickle.load(open(path + '/corpus.sav', 'rb'))
        
    def getFV(self, document):    
        words = document.split()
        s = np.zeros(100)
        k = 1
        for w in words:
            if w in self.modelo_w2v.wv.vocab:
                s=s+ self.modelo_w2v[w]
                k=k+1
        
        return s/k
    
    def rateComment(self, document):
        data = []
        vector_dim = self.getFV(document)
        data.append(vector_dim)
        result = self.model_svm.predict(data)
        return result[0]