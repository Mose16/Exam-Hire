from bottle import run, route, view, get, post, request, template, static_file

class Bro:
    def __init__(self, name, description, img, stock):
        self.name = name
        self.description = description
        self.img = img
        self.stock = stock
       
bros = [
    Bro("Tom","Generic british boi. Nice and smart so don't hire him if you don't want to feel bad about your IQ.","tom.jpg", True),
    Bro("Jerry","Good boi, will definatly tell us everything you did wrong. Cops might like this one.","jerry.jpg", True),
    Bro("Moses","Slightly retarded, will do anything for you. Makes you feel better about your problems. Depressed people and bullies may want.","moses.jpg", True),
    Bro("John","Goes to the gym.","john.jpg", True),
    Bro("Liam","Will serinade. Has guitar, good boi. Ideal for girls.","liam.jpg", True),
    Bro("Fox","Will sit and play nintendo with you for as long as you like. Presence makes you feel good. Introvertes love.","laimf.jpg", True),
    Bro("Dom","Will make you feel geneticaly inferior. Has good beauty products. Gays would buy again.","dom.jpg", False)
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