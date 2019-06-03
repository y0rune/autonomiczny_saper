#!/bin/bash

cat sampleDatas/* > sampleDatasAll
vw sampleDatasAll -l 10 -c --passes 1000000 --holdout_off -f ./models/walking.model --holdout_off 8  
rm -rf sampleDatasAll
rm -rf sampleDatasAll.cache
