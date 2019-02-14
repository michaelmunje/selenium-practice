#!/bin/bash
conda create -y -n selenium_env selenium requests
cd utils
./get_chromedriver.sh
echo 'Setup complete.'