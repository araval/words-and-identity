import re
from detect_language import *
from string import punctuation

def clean_text(line):
    '''
    input: line
    This function removes hyperlinks, mentions and hashtags.  
    returns lowercase text with only alpha-numeric characters.
    '''

    line = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', line)
    line = re.sub('&amp;', ' ', line)
    line = line.lower()
    words = line.split()
    for i, word in enumerate(words):
        if '@' in word:
            words[i] = ''
        else:
            words[i] = filter(lambda char: char.isalnum() or char == '#', word)
    line = ' '.join(words)

    return line 

def clean_tweets(tweet_list, class_label):
    '''
    take a list of tweets, returns a list of clean tweets
    '''
    cleaned_tweets = []
    for tweet in tweet_list:
        if "RT" not in tweet:
            tweet = clean_text(tweet) 
            if detect_language(tweet) == 'english':
                cleaned_tweets.append((tweet, class_label))

    return cleaned_tweets

def clean_input_text(text):
    if detect_language(text) == 'english':
        text = clean_text(text)
        return text
    else:
        return None
