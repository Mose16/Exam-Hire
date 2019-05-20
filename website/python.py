from bottle import run, route, view, get, post, request, template, static_file
from datetime import *

class Bro:
    def __init__(self, name, description, img, cost, stock, booked_details=""):
        self.name = name
        self.description = description
        self.img = img
        self.stock = stock
        self.cost = cost
        self.booked_details = booked_details
       
       
months = {
    'January' : 1,
    'Febuary' : 2,
    'March' : 3,
    'April' : 4,
    'May' : 5,
    'June' : 6,
    'July' : 7,
    'August' : 8,
    'September' : 9, 
    'October' : 10,
    'November' : 11,
    'December' : 12
}
        
bros = [
    Bro("Tom","Generic british boi. Nice and smart so don't hire him if you don't want to feel bad about your IQ. Will colonise only if it brings glory to his queen.","tom.jpg", 970, True),
    Bro("Jerry","Good boi, will definatly tell us everything you did wrong. Cops might like this one.","jerry.jpg", 90, True),
    Bro("Moses","Slightly retarded, will do anything for you. Makes you feel better about your problems. Depressed people and bullies may want.", "moses.jpg", 20, True),
    Bro("John","Goes to the gym.","john.jpg", 100, True),
    Bro("Liam","Will serinade. Has guitar, good boi. Ideal for girls.","liam.jpg", 100, True),
    Bro("Fox","Will sit and play nintendo with you for as long as you like. Presence makes you feel good. Introvertes love.","laimf.jpg", 78, True),
    Bro("Dom","Will make you feel geneticaly inferior. Has good beauty products. Gays would buy again.","dom.jpg", 20, False)
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
    date_ = request.forms.get("date")
    
    date_alt = date_.split(" ")
    date_alt[1] = date_alt[1].strip(",")
    
    curr_date = datetime.now()
    d0 = date(curr_date.year, curr_date.month, curr_date.day)
    d1 = date(int(date_alt[2]), int(months[date_alt[0]]), int(date_alt[1]))
    delta = d1 - d0
    total_cost = current_bro.cost * delta.days
    total_cost = str(total_cost)
    current_bro.booked_details = [Fname, Lname, str(curr_date.strftime("%B")) + " " + str(curr_date.day) + ", " + str(curr_date.year), date_, total_cost]
    return dict(bro = current_bro)

#Purchase page
@route('/application.html')
@view('application.html')
def application():
    pass

#Purchase_success page
@route('/application_success', method = "POST")
@view('application_success')
def application_success():
    Fname = request.forms.get("first_name")
    Lname = request.forms.get("last_name")
    description = request.forms.get("description")
    cost = int(request.forms.get("cost"))
    
    bros.append(Bro(Fname, description, "empty.jpg", cost, True))
    return dict(bro = bros[-1])

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