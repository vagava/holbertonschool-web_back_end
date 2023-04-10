#!/bin/bash
# ls > Infodir.txt
cat Infodir.txt | while read y
do
    if [[ "$y" != 'Infodir.txt' || "$y" != 'script_loadproyect.sh' ]];
    then
    git add $y
    git commit -m "add $y"
    git push origin main
    # sleep 5m
    fi
done
 
