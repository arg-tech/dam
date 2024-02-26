from flask import Flask, request, send_file
from flask import json
import json
from src.dam1.dam1 import DAM1
from src.dam1.dam1 import DAM2
from src.dam3.dam3 import get_argument_reletion_dam3
from src.get_AIF import aif
from src.utility import get_file
from src.data import Data


import logging
logging.basicConfig(datefmt='%H:%M:%S', level=logging.DEBUG)


app = Flask(__name__)

@app.route('/json-aif', methods = ['GET', 'POST'])
def json_aif():
	if request.method == 'POST':
		file_obj = request.files['file']
		f_name = file_obj.filename
		file_obj.save(f_name)
		file = open(f_name,'r')
		file_content = file.read()
		result=aif(f_name)
	return result


@app.route('/dam-03', methods = ['GET', 'POST'])
def dam3():
	if request.method == 'POST':	
		dam3 = DAM2()
		file_obj = request.files['file']
		data = Data(file_obj)
		return dam3.get_argument_structure(file_obj)
	if request.method == 'GET':
		info = "Inference identifier is an AMF compononet that identifies the argument relations exsiting between propositions.  This is the  implementation that combines DAM-01 and DAM-02 to improve perfromance.  It takes xIAF as an input to return xIAF as an output. The component can be conected to a segmenter in the argument mining pipeline."
		return info	

@app.route('/dam-02', methods = ['GET', 'POST'])
def dam2():
	if request.method == 'POST':
		dam2 = DAM2()
		file_obj = request.files['file']
		data = Data(file_obj)
		return dam2.get_argument_structure(file_obj)
	if request.method == 'GET':
		info = "Inference identifier is an AMF compononet that identifies the argument relations exsiting between propositions.  This is the  implementation of decompositional argument mining (DAM) that decomposes propositions into four functional components and uses deep learning techniques to identify the relations between the functional components to detect argument relations.  It takes xIAF as an input to return xIAF as an output. The component can be conected to a segmenter in the argument mining pipeline."
		return info	

@app.route('/dam-01', methods = ['GET', 'POST'])
def dam1():
	if request.method == 'POST':
		# Instantiate DAM1 class
		dam1 = DAM1()
		file_obj = request.files['file']
		data = Data(file_obj)
		return dam1.get_argument_structure(file_obj)
	if request.method == 'GET':
		info = "Inference identifier is an AMF compononet that identifies the argument relations exsiting between propositions.  This is the  implementation of decompositional argument mining (DAM) that decomposes propositions into four functional compoenents and uses the semantic similarity and sentiment category between those components to detect argument relations.  It takes xIAF as an input to return xIAF as an output. The component can be conected to a segmenter in the argument mining pipeline to populate."
		return info	
	
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5003"), debug=False)	  
