echo "[server-login]" > ~/.pypirc
echo "username:" $PYPI_USER >> ~/.pypirc
echo "password:" $PYPI_PASSWORD >> ~/.pypirc
echo "[distutils]" >> ~/.pypirc
echo "index-servers=pypi" >> ~/.pypirc
echo "[pypi]" >> ~/.pypirc
echo "username =" $PYPI_USER >> ~/.pypirc
echo "password =" $PYPI_PASSWORD >> ~/.pypirc
python3 setup.py sdist --formats=zip
python3 -m twine upload dist/* --skip-existing
