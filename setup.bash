#!/bin/bash

mkdir venv/
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt

unzip -o -d data/raw data/raw/ml-100k.zip
mkdir -p data/interim/
