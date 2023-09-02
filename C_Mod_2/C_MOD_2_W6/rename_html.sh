#!/usr/bin/env bash 

for file in *.HTML; do 
    
    name=$(basename "$file" .HTML)
    # $basename index.HTML .HTML
    
    #echo mv "$file" "$name.html"
    mv "$file" "$name.html"
done