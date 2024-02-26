

import re
from flask import json




####################

def is_json(myjson):
  try:
    data=open(myjson)
    data2=data.read()
    #json_dict = json.loads(data2)
    json_object = json.loads(data2)
  except ValueError as e:
    print(e)
    return False
  return True



	
def aif(path):
	is_json_file=is_json(path)
	if is_json_file: 
		file=open(path)
		data=file.read()		
		extended_json_aif = json.loads(data)
		json_dict = extended_json_aif['AIF']
		json_dict = extended_json_aif['AIF']
		return json.dumps(json_dict)
	else:
		return("Invalid json-aif")

	






  
