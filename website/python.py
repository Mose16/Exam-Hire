from bottle import run, route, view, get, post, request, static_file
from itertools import count


###Pages###
#Index page
@route('/')
@view('index')
def index():
    pass

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='Css/')

@route('/Images/<filename>')
def upload_image(filename):
    return static_file(filename, root='Images/')

run(host='0.0.0.0', port = 399, reloader = True, debug = True)