#!/bin/bash

echo -e "\n"
echo "Hey ${developer_name} we will start setting up the environment!"
echo -e "\n"

# installing/updating basic libraries
pip install --upgrade pip
pip install wheel

# Creating virtual environment
python -m venv test_env
source test_env/bin/activate
pip install -r requirements.txt
