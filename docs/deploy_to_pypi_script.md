# Script to deploy to PYPI Package

## Motivation

This script shell is used to help shorten the process to upload package to PYPI repositories

##  Prerequisites
- Change the [Setup Package Files](../setup.py) in the `version` field

- Update the [Change Log Files](../CHANGELOG.txt), make sure that date is up to date and changes are clearly explained

- Next make sure to update the [Requirement Files](../requirements.txt) and update the `clouday1-extract-aws-metadata==0.0.x` into the latest version

## Instruction on initialization of the script (only for first time configuration)

- Make sure to export the environment variable to the bash CLI:
```
export PYPI_USERNAME={YOUR_USERNAME}
```
```
export PYPI_PASSWORD={YOUR_PYPI_PASSWORD}
```
## Instruction on How to use the script

- Activate your virtual environment:
```
source venv/bin/activate
```

- Give permission to our script to execute the command
```
chmod u+x ./tools/shell/deploy_to_pypi.sh 
```

- To use the script:
```
./tools/shell/deploy_to_pypi.sh
```
