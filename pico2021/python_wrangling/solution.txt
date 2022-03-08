#!/bin/bash
wget "https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py"
wget "https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt"
wget "https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en"
cat pw.txt | python ende.py -d flag.txt.en
