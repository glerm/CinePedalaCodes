#!/bin/bash
# creme de barbear ~ http://automata.cc
#
# usage ~ ./creme.sh <input video> <slice duration (in seconds)>

file=$1
slice=$2

filename=`echo "$file" |  cut -d '.' -f1`
duration=`ffmpeg -i "$file" 2>&1 | grep Duration | awk '{print $2}'`
seconds=`echo "scale=4; ${duration:6:5} + ${duration:3:2}*60" | bc`

for i in $(seq 0 $slice $seconds)
do
    # creating wav slice
    ffmpeg -ss $i -t $slice -i $file -vn -acodec pcm_s16le -ar 44100 -ac 2 $(echo "${filename}_${i}.wav")
    # creating mov slice
    ffmpeg -ss $i -t $slice -i $file -an $(echo "${filename}_${i}.mov")
done