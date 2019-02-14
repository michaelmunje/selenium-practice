if conda env list | grep -q "selenium_env"; then
echo 'Launching script..'
else
  ./setup.sh
fi
cd utils
source activate_env.sh
cd ../src
python bad_csun_hack.py

