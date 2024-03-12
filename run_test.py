
from werkzeug.datastructures import FileStorage
import sys
sys.path.append('/Users/debelagemechu/projects/amf/dam')  # Add the parent directory of 'src' to the Python path

from src.ArgumentRelationAnalyser.dam import DAM

from src.data import Data
from werkzeug.datastructures import FileStorage

local_file_path = '/Users/debelagemechu/projects/amf/AMF-modularized/ova3-example-3.json'

# Create a FileStorage object from the local file path
file_obj = FileStorage(stream=open(local_file_path, "rb"), filename='file.json')
print(file_obj)

# Reset the file pointer to the beginning of the file
file_obj = file_obj.stream.seek(0)

# Save the file
f_name = file_obj.filename
file_obj.save(f_name)

print("==========saved==================")


from werkzeug.datastructures import FileStorage
import json

local_file_path = '/Users/debelagemechu/projects/amf/AMF-modularized/ova3-example-3.json'

# Create a FileStorage object from the local file path
file_obj = FileStorage(stream=open(local_file_path, "rb"), filename='file.json')

# Now you can pass this FileStorage object to a function or class method
# that expects a file-like object, such as one handling a POST request

# For example, you can read the JSON data from the file_obj
data = json.load(file_obj)

# Now you can work with the 'data' variable, which contains the contents of the JSON file
print(data)  # Example: print the contents of the JSON file




data = Data(file_obj)
dam3 = DAM(file_obj,"3")
print(dam3.get_argument_structure())