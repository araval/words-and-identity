'''
Script to detect language of a text. Currently includes English, Spanish, Portuguese and Italian. 
Additional langauges can be added in the list 'languages', no other changes required. 
Although, if NLTK does not have stopwords for a language then need to download that language.  
'''

from nltk.corpus import stopwords
from string import punctuation

languages = ['english', 'spanish', 'portuguese', 'italian']

language_stopwords = {}
for language in languages:
    try:
        language_stopwords[language] = set(stopwords.words(language))
    except IOError as e:
        print e
        print "NLTK corpus does not contain %s\n" % language
        exit(1)

def detect_language(text):
    counter = {}
    for language in languages:
        counter[language] = 0

    for word in set(text.split()):
        word = filter(lambda char: char not in punctuation, word)
        word = word.lower()
        for language in languages:
            if word in language_stopwords[language]:
                counter[language] += 1

    max_count = max(counter.values())

    if max_count == 0:
        return None
    for key, value in counter.iteritems():
        if value == max_count:
            return key

if __name__ == '__main__':
    print 'Input text'
    text = raw_input()
    print detect_language(text)
