#!/usr/bin/env bash
cat testtime.log | awk -F' ' '{print $1" "$2}' | awk '{print substr($0,2,length($0)-2)}' > testtime-refine.log

python calculate.py testtime-refine.log
