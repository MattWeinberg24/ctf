#!/bin/bash
chmod +x ltdis.sh
./ltdis.sh static
cat static.ltdis.strings.txt | grep "pico"
