#!/bin/bash
set -e

cd "$(dirname "$0")"

# Always recreate venv
rm -rf venv
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# Run your script
./venv/bin/python app.py

