#!/bin/sh
IMAGE=jankapunkt/latexcv:1.0
CV_FILE_NAME=heuzef_cv
docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" pdflatex --output-directory=$1 $1/"$CV_FILE_NAME".tex

# Create a compressed light weight copy
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$1/"$CV_FILE_NAME".min.pdf $1/"$CV_FILE_NAME".pdf