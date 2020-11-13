#!/bin/bash


while read p; do
  echo "$p"
  curl -s -O "$p" &
done <harmonogram.urls.txt