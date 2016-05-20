#!/bin/bash
for URL in ` cat ./url_list.txt`
do
    echo $URL
    python vnc_screen.py $URL
done
