from sklearn.externals import joblib
import numpy as np
import requests
import sys
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from clean_text import *

wordnet = WordNetLemmatizer()

def my_tokenize(doc):
   tok = word_tokenize(doc)
   return[wordnet.lemmatize(x) for x in tok]

def main(argv):

    if len(argv) == 1:
        filename = argv[0]
        with open(filename, 'r') as f:
            text = f.read()

    elif len(argv) == 0: 
	print "Input text:", 
        text = raw_input()

    else: 
        print "Error: Too many arguments"
        print "USAGE: python predict.py <filename> \n \n OR \n \n python predict.py"
        exit(1)

    text = text.lower()

    text = clean_input_text(text)

    if text == None:
        print 'Please input English text, or if it is already English, please input longer text.'
        exit(1)


    #Load vectorizer and model:
    count_vect = joblib.load('pickledModel/count_vect.pkl')
    tfidf_tranformer = joblib.load('pickledModel/tfidf_tranformer.pkl')
    model = joblib.load('pickledModel/logistic_model.pkl')

    #prepare data for prediction
    counts = count_vect.transform([text])
    article_tfidf = tfidf_tranformer.transform(counts)

    #predict and print
    classes =  model.classes_
    probas = model.predict_proba(article_tfidf)[0]
        
    indicies = np.argsort(probas)

    # Two highest probabilities
    prob_max = probas[indicies[-1]] 
    prob_next = probas[indicies[-2]]

    # and the two corresponding classes
    class1 = classes[indicies[-1]][:-1]
    class2 = classes[indicies[-2]][:-1]

    #Prepare for printing:
    vowels = ['a','e','i','o','u']
    if class1[0] in vowels:
        class1 = 'an '+ class1
    else:
        class1 = 'a ' + class1

    if class2[0] in vowels:
        class2 = 'an '+ class2
    else:
        class2 = 'a ' + class2

    print '\n\n'
    if prob_max - prob_next < 0.2:
        print '         This person could be either %s or %s.\n' %  (class1, class2)
    else:
        print '         This person is most likely %s.\n' % class1

if __name__ == "__main__":
    main(sys.argv[1:])
