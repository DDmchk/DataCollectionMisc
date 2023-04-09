#!/bin/sh
date
cd /home/datacollection/DataCollectionMisc
git pull
git add .
git commit -m "Automatic commit"
git push origin master
