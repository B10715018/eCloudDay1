from flask import Flask, request
import os
from os.path import exists

app=Flask(__name__)

@app.route('/')
def root_route():
    return 'Hello World'

@app.route('/collect', methods=['POST'])
def collectMetadata():

    # data = request.get_json()
    try:
        os.system('python ./command/collect.py')  
    except:
        return{
            'status': 'Error',
            'code': 500,
            'message':'Bad Request Error'
        }


    return {  
        'status': 'Success',
        'code': 200,
        'message': 'Succeed collecting metadata'
    }

@app.route('/prepare',methods=['POST'])
def prepareJSONFile():
    try:
        os.system('./job2.sh')
        if(not exists('./data/data.json')):
            raise Exception('No JSON file exist')
    except Exception as e:
        return{
            'status': 'Error',
            'code': 500,
            'message':'Bad Request Error',
            'detail': str(e)
        }

    return {  
        'status': 'Success',
        'code': 200,
        'message': 'Succeed prepare JSON file'
    }

@app.route('/request',methods=['DELETE'])
def clearJSONMetadata():
    try:
        os.system('./jobClearJSON.sh')
    except:
        return{
            'status': 'Error',
            'code': 500,
            'message':'Bad Request Error'
        }
    return {  
        'status': 'Success',
        'code': 200,
        'message': 'Succeed erasing metadata file'
    }
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)