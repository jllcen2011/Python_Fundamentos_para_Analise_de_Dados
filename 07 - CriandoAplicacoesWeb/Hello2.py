from flask import Flask
app = Flask(__name__)       #importei o flask e criei o nome da app (__name__)

@app.route("/")             # criei a rota que é a raíz da aplicação. Se eu chamar http...5000/, vai retornar index
def index():                # pra cada rota, eu tenho uma função, conforme visto abaixo
    return "Index!"

@app.route("/hello")        # aqui a rota indica que vai além da raíz da aplicação, ou seja,
def hello():                # se eu chamar o http....5000/hello, vai ser retornado hello world
    return "Hello, World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()