#!/bin/sh
python setup.py sdist
twine upload --skip-existing dist/* -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD}
pip3 install -r requirements.txt