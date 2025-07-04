#!/bin/sh
IMAGE=jankapunkt/latexcv:1.0
CV_FILE_NAME=heuzef_cv_AIjusTeX

echo "Génération du CV en cours ..."
echo ""

python3 $1/AIjusTeX.py > $1/"$CV_FILE_NAME".tex

# docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" pdflatex --output-directory=$1 $1/"$CV_FILE_NAME".tex

# Create a compressed light weight copy
# gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$1/"$CV_FILE_NAME".min.pdf $1/"$CV_FILE_NAME".pdf

echo "Génération du CV terminée !"