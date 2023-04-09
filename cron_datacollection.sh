#!/bin/sh
date
cd /home/datacollection/DataCollectionMisc
git add .
git commit -m "Automatic commit"
git pull
git push origin master
