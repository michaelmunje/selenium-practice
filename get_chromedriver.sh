#!/bin/bash
url = 'https://chromedriver.storage.googleapis.com/2.37/chromedriver_'
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	url += 'linux64'
    # Linux
elif [[ "$OSTYPE" == "darwin"* ]]; then
	url += 'mac64'
    # Mac
elif [[ "$OSTYPE" == "cygwin" ]]; then
	url += 'win32'
    # Windows
elif [[ "$OSTYPE" == "msys" ]]; then
	url += 'win32'
    # Windows
else
	echo "Could not find Operating System. Assuming linux..."
	url += 'linux64'
    # Unknown.
fi
url += '.zip'
wget -O ./chromedriver.zip $url
unzip chromedriver.zip
rm chromedriver.zip
# export PATH=$PATH:chromedriver # not working must use absolute path in python
