#!/bin/sh
CONTAINER=uucona/groonga
docker build -t="${CONTAINER}" --rm=true .
docker run -t -d  -p 10041:10041 ${CONTAINER}


