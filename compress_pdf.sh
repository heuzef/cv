#!/bin/bash

# Usage: ./compress_pdf.sh <input_file.pdf>
# This script compresses a PDF file using Ghostscript.
# The compressed output file will be named <input_file.min.pdf> and
# will be created in the same directory as the input file, regardless
# of the current working directory when the script is executed.

if [ -z "$1" ]; then
  echo "Error: No input file specified."
  echo "Usage: ./compress_pdf.sh <input_file.pdf>"
  exit 1
fi

input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
  echo "Error: Input file '$input_file' not found."
  exit 1
fi

# Get the absolute path of the input file.
# This ensures that we have the full path from the root directory.
absolute_input_file="$(realpath "$input_file")"

# Extract the directory containing the input file.
# This is where the compressed file should be saved.
input_directory="$(dirname "$absolute_input_file")"

# Extract the base name (file.pdf) and extension (.pdf) from the input file.
filename=$(basename -- "$input_file") # Use original input_file for basename to avoid potential issues with realpath's output formatting
extension="${filename##*.}"
filename_no_extension="${filename%.*}"

# Construct the full path for the output file.
# It will be in the same directory as the original input file.
output_file="${input_directory}/${filename_no_extension}.min.${extension}"

# echo "Input file: $input_file"
# echo "Absolute input file path: $absolute_input_file"
# echo "Input file directory: $input_directory"
# echo "Output file path: $output_file"
echo "Starting compression..."

# Execute the Ghostscript command
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$output_file" "$absolute_input_file"

if [ $? -eq 0 ]; then
  echo "Successfully compressed '$input_file' to '$output_file'"
else
  echo "Error: PDF compression failed for '$input_file'."
fi