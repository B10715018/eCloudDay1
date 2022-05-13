# Publish `clouday1_extract_aws_metadata` into python package

1. To Publish python package file make sure you have `twine` in your virtual environment: execute 
```
pip3 install setuptools twine
```
2. Create a distribution folder for our python package by executing 
```
python3 setup.py sdist
```
3. Upload your package folder into PyPi repository by executing : 
```
twine upload --repository-url https://upload.pypi.org/legacy dist/* 
```
4. You will be asked to insert your username and password for PyPi account to upload the package to PyPi repositories
5. Then you can view our package here:[Own Built Clouday1 Package](https://pypi.org/project/clouday1-extract-aws-metadata/0.0.1/)

Reference Video can be found here : [Reference Video Tutorial](https://www.youtube.com/watch?v=zhpI6Yhz9_4)