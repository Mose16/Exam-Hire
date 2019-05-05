from bottle import run, route, view, get, post, request, template, static_file

class Bro:
    def __init__(self, name, description, img, num):
        self.index = num
        self.name = name
        self.description = description
        self.img = img
        
bros = [
    Bro("Jerry","Bla bla bla","jerry.jpg","1"),
    Bro("Moses","Ble ble ble","jerry.jpg","2"),
    Bro("Tom","Ble ble ble","jerry.jpg","2")
]



###Pages###
#Index page
@route('/')
@view('index')
def index():
    pass

#Product page
@route('/products.html')
@view('products.html')
def products():
    return dict(bros_list = bros)



##Static files###
#Images
@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./Images')
#Css files
@route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./Css')
#Script files
@route('/script/<filename>')
def server_static(filename):
    return static_file(filename, root='./Script')

run(host='0.0.0.0', port = 399, reloader = True, debug = True)