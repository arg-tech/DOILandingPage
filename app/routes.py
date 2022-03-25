from flask import redirect, request
from . import application
import json



@application.route('/noop', methods=['GET', 'POST'])
def amf_schemes():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        ff = open(f.filename, 'r')
        content = ff.read()
        
        print(content)
        
    return content
 
