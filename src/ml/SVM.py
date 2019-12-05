import pickle
from os.path import join, dirname, realpath
from gensim.models import word2vec
#from ..models.constant.Constant import Constant
import gensim
from sklearn import svm
import numpy as np
import re
from stop_words import get_stop_words

class SVM:
    def __init__(self):
        path = dirname(realpath(__file__))
        self.model_svm = pickle.load(open(path + '/sorteml.sav', 'rb'))
        self.modelo_w2v = pickle.load(open(path + '/corpus.sav', 'rb'))
        self.stop_words = get_stop_words('spanish')
        self.stop_words.append("n")
        self.pattern = re.compile(r'[^A-Za-zñÑáéíóúÁÉÍÓÚ0-9]+')
        
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
        tempDocument = document.lower()
        tempDocument = self.clean_documents(tempDocument)
        vector_dim = self.getFV(tempDocument)
        data.append(vector_dim)
        result = self.model_svm.predict(data)
        return result[0]
    
    def clean_documents(self, text):
        response = ""
        tokens = text.split(" ")
        i = 0
        for ti in tokens:
            ti = self.replace(ti)
            if len(ti) == 0:
                continue
            elif(ti in ["no"]):
                if i == 0:
                    response = ti
                else:
                    response = response + " " + ti
            elif(ti in self.stop_words):
                continue
            else:
                if i == 0:
                    response = ti
                else:
                    response = response + " " + ti
            i = i + 1
        return response
    
    def replace(self, text):
        return self.pattern.sub("", text)