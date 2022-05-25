from flask import redirect, request, render_template
from . import application
import json



@application.route('/noop', methods=['GET', 'POST'])
def amf_schemes():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        ff = open(f.filename, 'r')
        content = json.load(ff)
        return content
    elif request.method == 'GET':
        return render_template('index.html')
        
 
 
