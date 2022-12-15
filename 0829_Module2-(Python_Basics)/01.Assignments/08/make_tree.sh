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
cp text_chunk1.txt /Advanced/text_chunk2.txt
cd Advanced
echo "I like them because ..." >> text_chunk2.txt