#!/bin/sh

VIRTUAL_ENV="./venv"
PATH="./venv/bin:$PATH"
which python

echo "JOBID: $JOBID"
#mkdir JOBID
#cd JOBID


python predict.py
