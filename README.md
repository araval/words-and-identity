# What Our Words Say

Note: The service I was using to fetch old tweets (greptweet) has been retired. This no longer works.


Consider the most frequently used words by different classes of people on their twitter:
<p>
<img src="https://github.com/araval/words-and-identity/blob/master/images/all.png" width = "1100px">
<em>Left to right: Scientists, Authors, Musicians, Entertainers, Athletes, and Politicians.</em>
</p>

The data is conclusive: Scientists think more, love a lot less; authors think and love equally; musicians and athletes only love, don't think; politicians apparently do neither. All of them are very *thank*ful and share *new* things, so I removed those two words from the word clouds in order to see more interesting words. 

Our words tell others who we are. So we can take a person's written words and have a model make a prediction about their identity. This little project is an attempt in that direction, with the training data coming from twitter. The final model of course will work with any kind of text, but it will not do well in non-normal-speech like contexts, for example research-papers or Wikipedia. 

## Data
For *athletes*, *musicians*, and *entertainers*, I got the hundred most followed users from <a href="http://twittercounter.com/pages/100/">twittercounter</a>. I got popular *scientists* from 
<a href="http://www.teachthought.com/uncategorized/100-scientists-on-twitter-by-category/">teachthought</a> and 
<a href="http://www.sciencemag.org/news/2014/09/top-50-science-stars-twitter">sciencemag</a>, popular *authors* from 
<a href="http://mashable.com/2009/05/08/twitter-authors/#qP2pNIxiomqZ">mashable</a>, and US-politicians from <a href="http://www.davemanuel.com/the-most-popular-us-politicians-by-twitter-followers-163/">here</a> and 
<a href="http://www.socialseer.com/resources/us-senator-twitter-accounts/">here</a>.

If _musicians_ and _entertainers_ look the same, it is because they mostly are. _Entertainers_ includes most musicians plus additional comedians such as John Oliver. Considering this overlap, I chose to keep only *musicians*, and didn't use *entertainers* for modelling. 

The training data consists of 922,231 tweets, with 72,040,820 words of which 312,605 are unique. 

There are some users who tweet in English, as well as additional languages such as Spanish or Portuguese. I filtered the tweets to keep only the English tweets, with the help of *detect_language.py*, which uses stopwords for language detection. 

## Model 
With five classes - Scientists, Authors, Musicians, Athletes, and Politicians, I trained a logistic regression model for classification. The script predict.py loads the model and classifies text, which can be input via either file or *raw_input()*. The bash script *who_is_it.sh* takes a twitter- username, fetches tweets and outputs the class.

## Examples

Recent article from NYtimes on LIGO:
```
$ python predict.py
Input text: A team of scientists announced on Thursday that they had heard and recorded the sound of two   
black holes colliding a billion light-years away, a fleeting chirp that fulfilled the last prediction of   
Einstein’s general theory of relativity.  
 
         This person is most likely a scientist.

```

Amy Goodman's twitter:
```
$ ./who_is_it.sh amygoodman_dn

         This person could be either an author or a politician.

```
