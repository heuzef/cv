#!/bin/sh
IMAGE=jankapunkt/latexcv:1.0
CV_FILE_NAME=heuzef_cv_AIjusTeX

echo "CV generation in progress ..."
echo ""

python3 $1/AIjusTeX.py > $1/"$CV_FILE_NAME".tex

# Need PDF files too ? Uncomment the following lines :

# docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" pdflatex --output-directory=$1 $1/"$CV_FILE_NAME".tex
# echo "Create a compressed light weight copy"
# echo ""
# gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$1/"$CV_FILE_NAME".min.pdf $1/"$CV_FILE_NAME".pdf

echo "DONE !"
echo "-----"
ls -lArth fr | grep "$CV_FILE_NAME"