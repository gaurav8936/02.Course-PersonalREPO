#!/bin/bash

mkdir s1
cd s1
mkdir s3
touch conf.txt
echo "Virtual (conda) environments are my favorite new technology" >> conf.txt
mkdir s2
cd s2
touch text_chunk1.txt
echo "Virtual environments are good for managing package versions" >> text_chunk1.txt
mkdir Advanced
cd Advanced
cp ./test_chunk1.txt test_chunk2.txt
echo "I like them because ..." >> test_chunk2.txt