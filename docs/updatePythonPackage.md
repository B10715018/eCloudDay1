# This is documentation for updating python package

- After changing content of python package, don't forget to update the `CHANGELOG.txt`

- Next, change the version of your package in `setup.py` and change the version of your package in `requirements.txt`

- Then, execute:
```
python setup.py sdist
```

- Upload your package to the PYPI repositories:
```
twine upload --skip-existing dist/*
```

- Enter the username `__token__` and enter the API access token given by PYPI

-  Then after that to update our package in the virtual environment, execute:
```
pip3 install -r requirements.txt
```

- Then the package is ready to use