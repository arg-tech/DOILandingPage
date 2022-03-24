from flask import redirect, request
from . import application
import json



@application.route('/')
def index():
    return redirect('/noop')

@application.route('/noop', methods=['GET', 'POST'])
def amf_schemes():
    print('SERVICE CALLED')
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        ff = open(f.filename, 'r')
        content = ff.read()
        
        print(content)
    if request.method == 'GET':
        content = "HELLO WORLD"
        
    return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 
