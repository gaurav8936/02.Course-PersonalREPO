#! /bin/bash

mkdir s1
mkdir s1/s3
touch s1/s3/conf.txt
echo "Virtual (conda) environments are my favorite new technology" >> s1/s3/conf.txt
mkdir s1/s2
touch s1/s2/text_chunk1.txt
echo "Virtual environments are good for ..." >> s1/s2/text_chunk1.txt
mkdir s1/s2/Advanced
cp s1/s2/text_chunk1.txt s1/s2/Advanced/text_chunk2.txt
echo "I like them because ..." >> s1/s2/Advanced/text_chunk2.txt