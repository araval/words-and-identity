#!/bin/bash

username0=$1
username=$(echo $username0 | awk '{print tolower($0)}')

curl "http://greptweet.com/create.php?id=$username"
for i in `seq 1 10`
    do
        url="http://greptweet.com/u/$username/tweets.txt"
        wget $url 2> .wgetResults
        if [[ "x$?" = "x0" ]]
            then break
        fi
            
        echo "rm $(cat .wgetResults | grep "Saving to:"| awk -F'‘' '{print $2}'| sed s/.$//g)"
        sleep 10 
    done
echo "$username dowloaded ..."
mv $(cat .wgetResults | grep "Saving to:"| awk -F'‘' '{print $2}'| sed s/.$//g) tweets.txt.gz
#mv tweets.txt tweets.txt.gz
ls
gunzip tweets.txt.gz
awk -F '|' '{print $3}' tweets.txt > tmp
rm tweets.txt
mv tmp "${username}.txt"
