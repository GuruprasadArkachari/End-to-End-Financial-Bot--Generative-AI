import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# asc time => fetsches log time and log history is created INFO level log,,


list_of_files = [
    "src/__init__.py", #constructor is magic function link : https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/__init__.py/ Python folder will have modular strcuture having various functions kept in files ot be called and INIT will be initated
  # so when ENV is called, it assumes Github/python as local environement 

    "src/helper.py", # to write all functiona, ingest, extract, loading ops
    "src/prompt.py", # to write system promptr 
    ".env",
    "setup.py", # to install these folders as 
    "app.py",
    "research/trials.ipynb",
   " test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)  # path file used to interprete forward path (linux based / MAC and winodws based path i.e. backword slashing)..other wise need to give path manual for win and linux based system
    # this will be exampple of robust app to run on any OS having no issues in production ver
    
    filedir, filename = os.path.split(filepath)
#split differfentiate between file name and folder name

    if filedir !="": #check if folder is empty..
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")