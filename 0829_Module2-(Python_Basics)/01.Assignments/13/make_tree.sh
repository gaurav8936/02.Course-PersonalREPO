#!/bin/bash

mkdir s1
#cd s1
mkdir s1/s3
touch s1/s3/conf.txt
echo "Virtual (conda) environments are my favorite new technology" >> s1/s3/conf.txt
mkdir s1/s2
#cd s2
touch s1/s2/text_chunk1.txt
echo "Virtual environments are good for managing package versions" >> s1/s2/text_chunk1.txt
mkdir s1/s2/Advanced
#cp text_chunk1.txt /Advanced/text_chunk2.txt
#cp text_chunk1.txt text_chunk2.txt
#cd Advanced
cp s1/s2/text_chunk1.txt s1/s2/Advanced/text_chunk2.txt
echo "I like them because ..." >> s1/s2/Advanced/text_chunk2.txt