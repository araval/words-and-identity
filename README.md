# What Your Words Say

Consider the most frequently words used by different classes of people on their twitter: 
<p>
<img src="https://github.com/araval/words-and-identity/blob/master/images/all.png" width = "1100px">
<em>Left to right: Scientists, Authors, Musicians, Entertainers, Athletes, and Politicians.</em>
</p>

The data is conclusive: Scientists think more, love a lot less. Authors think and love equally, Musicians and sporty-folks only love, don't think. Politicians do neither. 

All users say "thank you / thanks" and "new" way more that any other non-stopword word, so I added those two words to stopwords. 


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

```
USAGE:   bash who_is_it.sh <twitter-username>
```
