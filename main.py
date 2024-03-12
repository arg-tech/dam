from prometheus_flask_exporter import PrometheusMetrics
import logging

from flask import Flask, request
from src.ArgumentRelationAnalyser.dam import DAM

from src.data import Data

logging.basicConfig(datefmt='%H:%M:%S', level=logging.DEBUG)
app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/dam-03', methods = ['GET', 'POST'])
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def dam3():
	if request.method == 'POST':	
		file_obj = request.files['file']
		data = Data(file_obj)
		dam3 = DAM(data,"3")
		return dam3.get_argument_structure()
	if request.method == 'GET':
		info = "Inference identifier is an AMF compononet that identifies the argument relations exsiting between propositions.  This is the  implementation that combines DAM-01 and DAM-02 to improve perfromance.  It takes xIAF as an input to return xIAF as an output. The component can be conected to a segmenter in the argument mining pipeline."
		return info	
	

@app.route('/dam-02', methods = ['GET', 'POST'])
def dam2():
	if request.method == 'POST':
		file_obj = request.files['file']
		data = Data(file_obj)
		dam2 = DAM(data,"2")
		return dam2.get_argument_structure()
	if request.method == 'GET':
		info = "Inference identifier is an AMF compononet that identifies the argument relations exsiting between propositions.  This is the  implementation of decompositional argument mining (DAM) that decomposes propositions into four functional components and uses deep learning techniques to identify the relations between the functional components to detect argument relations.  It takes xIAF as an input to return xIAF as an output. The component can be conected to a segmenter in the argument mining pipeline."
		return info	

@app.route('/dam-01', methods = ['GET', 'POST'])
def dam1():
	if request.method == 'POST':		
		file_obj = request.files['file']
		data = Data(file_obj)
		dam1 = DAM(data,"1")
		return dam1.get_argument_structure()
	if request.method == 'GET':
		info = """Inference identifier is an AMF compononet that identifies the argument relations exsiting between propositions.  
		This is the  implementation of decompositional argument mining (DAM) that decomposes propositions into four functional compoenents and uses the semantic similarity and sentiment category between those components to detect argument relations.  
		It takes xIAF as an input to return xIAF as an output. The component can be conected to a segmenter in the argument mining pipeline to populate."""
		return info	
	
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5003"), debug=False)	  
