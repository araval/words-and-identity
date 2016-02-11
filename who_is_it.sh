#!/bin/bash

username0=$1
username=$(echo $username0 | awk '{print tolower($0)}')

curl "http://greptweet.com/create.php?id=$username"
for i in `seq 1 10`
    do
        url="http://greptweet.com/u/$username/tweets.txt"
        wget $url
        if [[ "x$?" = "x0" ]]
            then break
        fi
        rm tweets.txt
        sleep 10 
    done

mv tweets.txt tweets.txt.gz
gunzip tweets.txt.gz
awk -F '|' '{print $3}' tweets.txt > tmp
mv tmp tweets.txt
python predict.py tweets.txt
#mv tweets.txt $username".txt"
rm tweets.txt
