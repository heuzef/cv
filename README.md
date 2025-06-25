# Heuzef resume

This is my resume writed in LaTeX, it use AltaCV template : https://github.com/liantze/AltaCV

You need Texlive installed on your system or Docker to build with Latex environment. 

## Build Procedure

For this you need to have "texlive-core texlive-bibtexextra texlive-latexextra texlive-fontsextra" or Docker installed on your system.

> Get Docker: https://docs.docker.com/get-docker/

I use scripts for building the image and running the containers, this has originally been implemented by https://github.com/blang/latex-docker/.

So you should fine by simply running the script:

```shell
# Start Docker
$ service docker start

# Clone the repo and move into
$ git clone git@github.com:heuzef/cv.git && cd cv

# Create image container
$ docker build -t jankapunkt/latexcv:1.0 .

# Install Ghostscript (for PDF compression)
$ dnf install ghostscript

# Then, run to build PDF :
$ sh build.sh fr
$ sh build.sh en
```

To use AIjustTeX tool (work with Mistral by the way):

```shell
# Setup your API Key
$ echo "MISTRAL_API_KEY=<API_KEY>" > .env

# Paste the job offer in the <language>/job.txt
# Then, run to build your custom PDF :
$ sh build_AIjustTeX.sh fr
$ sh build_AIjustTeX.sh en
# Wait a minute and check the result in "_custom" files.
```