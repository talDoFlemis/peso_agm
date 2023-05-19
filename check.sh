#!/bin/bash

for i in {0..17}; do
	echo "Processando arquivo $i.in"
	diff --unified=0 "io/$i.out" <(./main.py <"io/$i.in")
done
