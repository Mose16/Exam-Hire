from bottle import run, route, view, get, post, request, template, static_file
from datetime import *

class Bro:
    def __init__(self, name, description, img, stock, booked_details=""):
        self.name = name
        self.description = description
        self.img = img
        self.stock = stock
        booked_details = booked_details
       
bros = [
    Bro("Tom","Generic british boi. Nice and smart so don't hire him if you don't want to feel bad about your IQ.","tom.jpg", True),
    Bro("Jerry","Good boi, will definatly tell us everything you did wrong. Cops might like this one.","jerry.jpg", True),
    Bro("Moses","Slightly retarded, will do anything for you. Makes you feel better about your problems. Depressed people and bullies may want.","moses.jpg", True),
    Bro("John","Goes to the gym.","john.jpg", True),
    Bro("Liam","Will serinade. Has guitar, good boi. Ideal for girls.","liam.jpg", True),
    Bro("Fox","Will sit and play nintendo with you for as long as you like. Presence makes you feel good. Introvertes love.","laimf.jpg", True),
    Bro("Dom","Will make you feel geneticaly inferior. Has good beauty products. Gays would buy again.","dom.jpg", False)
]


current_bro = None

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

#Purchase page
@route('/purchase/<name>')
@view('purchase')
def purchase(name):
    global current_bro
    found_bro = None
    for bro in bros:
        if bro.name == name:
            found_bro = bro
            break
    found_bro.stock = False
    current_bro = found_bro
    return dict(bro = found_bro)

#Purchase_success page
@route('/purchase_success', method = "POST")
@view('purchase_success')
def purchase_success():
    Fname = request.forms.get("first_name")
    Lname = request.forms.get("last_name")
    date = request.forms.get("date")
    
    curr_date = datetime.now()
    current_bro.booked_details = [Fname, Lname, str(curr_date.month) + " " + str(curr_date.day) + ", " + str(curr_date.year), date]
    return dict(bro = current_bro)
    

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