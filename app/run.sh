#!/bin/sh

VIRTUAL_ENV="./venv"
PATH="./venv/bin:$PATH"               
which python

python predict.py
