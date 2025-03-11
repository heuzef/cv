# Heuzef resume

This is my resume writed in LaTeX, it use the [AltaCV][l_alta] template.

You need  installed on your system or Docker en

## Build Procedure

It use Texlive to build Latex environment. For this you need to have "texlive-core texlive-bibtexextra texlive-latexextra texlive-fontsextra" or Docker installed on your system.

> Get Docker: https://docs.docker.com/get-docker/

Provide scripts for building the image and running the containers, 
so you should fine by simply running the script:

```shell
$ service docker start
$ git clone git@github.com:heuzef/cv.git && cd cv
$ ./create_image.sh
```

Then, for build PDF :
```shell
$ .docker/build.sh
```

This has originally been implemented by https://github.com/blang/latex-docker/tree/master