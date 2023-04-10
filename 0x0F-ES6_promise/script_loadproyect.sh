#!/bin/bash
# ls > Infodir.txt
cat Infodir.txt | while read y
do
    git add $y
    git commit -m "add $y"
    git push origin main
    # sleep 5m
done
 
